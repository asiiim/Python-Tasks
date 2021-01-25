import matplotlib.pyplot as plt
from datetime import date

def compute_tax_rate(list_of_income, year):
    ''' Compute the tax rate by getting the income of the given year and 
        respective tax rate group
    '''
    annual_gross_income = 0.0

    # Get the annual gross income in that year
    income_splitted_list = []
    for income_str in list_of_income:
        income_splitted_list.append(income_str.split(','))
    
    for data in income_splitted_list:
        if data[0] == year:
            annual_gross_income = int(data[1])
            break

    # Return the tax rate
    if annual_gross_income in range(18201, 37001):
        return 0.19
    elif annual_gross_income in range(37001, 90001):
        return 0.325
    elif annual_gross_income in range(90001, 180001):
        return 0.37
    elif annual_gross_income >= 180001:
        return 0.45
    else:
        return 0

''' Prompt for the file names '''
# TODO: Test with another file names
# TODO: Handle exception if file name is not matched or not found
trade_history_filename = input("Trade history file (trades.txt): ") or 'trades.txt'
live_pricedata_filename = input("Live price data file (live-prices.txt): ") or 'live-prices.txt'
client_ann_income_filename = input("Client's annual income records (income.txt):") or 'income.txt'


''' File handling '''
# TODO: Make a function that handles file
# Open files
trade_history_file = open(trade_history_filename, "r")
live_pricedata_file = open(live_pricedata_filename, "r")
client_ann_income_file = open(client_ann_income_filename, "r")

# Get file content to the respective list
# Read the files
trade_history_text = trade_history_file.read()
live_pricedata_text = live_pricedata_file.read()
client_ann_income_text = client_ann_income_file.read()

# Insert those read content in the list
trade_history_list = trade_history_text.splitlines()
live_pricedata_list = live_pricedata_text.splitlines()
client_ann_income_list = client_ann_income_text.splitlines()


''' Build Tabular Data of Client's Portfolio '''
# Get lists of each ',' comma delimited data from the trade history list
trade_history_splitted_list = []
for data in trade_history_list:
    sublist = list(data.split(','))
    trade_history_splitted_list.append(sublist)

# Get the unique list of stocks appeared in the trade history file
stock_list = []
for data in trade_history_splitted_list:
    stock_list.append(data[0])
unique_stock_list = list(set(stock_list))

# Compute units held of each unique stock from the trade file
portfolio = []          # Create a list to store the portfolio
total_worth = 0.0       # Total worth of all the stocks
for stock in unique_stock_list:

    # Initiate the variable for the portfolio
    units_held = 0
    share_price_rate = 0.0
    value = 0.0

    for trade_data in trade_history_list:
        # Check if the stock is contained in the trade data str
        if stock in trade_data:
            # Delimit the trade data str in to the list
            trade_data_list = list(trade_data.split(','))

            # Check if the trade data list contains buy or sell of the share
            if trade_data_list[1] == 'buy':
                units_held += int(trade_data_list[3])
            elif trade_data_list[1] == 'sell':
                units_held -= int(trade_data_list[3])
            else:
                # TODO: Test this exception
                raise ValueError(f'Unknown data in the file: {trade_data_list[3]}')
            
    # Get the live price rate of the share and its value
    for live_pricedata in live_pricedata_list:
        # TODO: Check if there are more same stock in the livestock
        # Check if stock is contained in the live price data string
        if stock in live_pricedata:
            # Get the list from the live price string data
            live_list = list(live_pricedata.split(','))
            share_price_rate = float(live_list[2])

            # Check if there is any units held for the stock and compute the share value
            if units_held > 0:
                value = round(units_held * share_price_rate, 2)

    # Append the computed values in the list of potfolio whose numbers of units are non zero
    if units_held > 0:
        portfolio.append([stock, units_held, value])

    # Sum up the value of all the stocks
    total_worth += round(value, 2)

# Build tabular data of client's portfolio
# TODO: Add $ in the amounts in the portfolio values. Example: $500
formatted_row = '{:>15} {:>15} {:^15}'
header = ["Stock |", "Units Held |", "Value"]
print("\n(1) Client's Portfolio")
print(formatted_row.format(*header))
separator = ""

for item in header:
    separator += ("-" * (len(item) + 7))
print(separator)

for row in portfolio:
    # Add bar between each data in row
    row_1 = str(row[0]) + ' |'
    row_2 = str(row[1]) + ' |'
    print(formatted_row.format(*[row_1, row_2, row[2]]))
print(separator)

# Print the total worth of the stocks
# TODO: Check the rounding precession of the total worth variable
print('{:>15} {:>15} {:^15}'.format(*['Total Worth', '', str(total_worth)]))
print("\n(2) Pie chart of portfolio opens in new window")


''' CGT Report Section '''
print("\n(3) CGT Report")

# Get year to generate file of CGT Report
cgt_report_year = input("Enter a year to generate CGT Report: ")

# Get the fy_start_date and fy_end_date with given year
fy_start_date = date.fromisoformat(str(int(cgt_report_year) - 1) + '-07-01')
fy_end_date = date.fromisoformat(cgt_report_year + '-06-30')


fy = str(int(cgt_report_year) - 1) + "-" + cgt_report_year[2] + cgt_report_year[3]
# TODO: Check if random value is input
print(f"CGT report for the {fy} financial year successfully generated and saved in file cgt-report.txt")

# TODO: Get a list of stock sold during the given year
cgt_list = []
for trade_data in trade_history_splitted_list:
    # Check if the share is sold:
    if trade_data[1] == 'sell':
        # Get date of the trade
        trade_date = date.fromisoformat(trade_data[2])
        
        # Check if the date is in the given fiscal year
        if (trade_date >= fy_start_date) and (trade_date <= fy_end_date):
            # Get the cost base of the stock
            stock_cost_base = 0.0
            for data in trade_history_splitted_list:
                
                # Ensure the selected stock
                if data[0] == trade_data[0]:
                    # Check if share is bought
                    if data[1] == 'buy':
                        stock_cost_base = float(data[4])

            # Calulate the capital gains rate
            # TODO: Check for decimal rounding in each computed values
            capital_gain_rate = float(trade_data[4]) - stock_cost_base
            
            # Get the number of shares sold
            qty_share_sold = trade_data[3]

            # Calculate Capital Gains
            capital_gains = capital_gain_rate * float(qty_share_sold)

            if capital_gains > 0:
                # Get the tax_rate
                tax_rate = compute_tax_rate(client_ann_income_list, cgt_report_year)

                # Calculate tax payable
                tax_payable = capital_gains * tax_rate

                # Append the data in the cgt list
                cgt_list.append([trade_data[0], stock_cost_base, capital_gains, tax_payable])

# Generate formatted string before storing in the file
cg_report_row_format = '{:>15} {:>15} {:>15} {:>15}'
cg_report_header = cg_report_row_format.format(*['| Share', '| Cost Base', '| Capital Gains', '| Tax Payable'])
cg_report_content = cg_report_header + '\n'
for content in cgt_list:
    formatted_content = cg_report_row_format.format(*content)
    cg_report_content += (formatted_content + '\n')
cg_report_content += '\n'

# TODO: Handle the condition if the created file is already existed
cg_report_file = open("cg-report.txt", "a")
if cg_report_file:
    cg_report_file.write(cg_report_content)
else:
    cg_report_file = open("cg-report.txt", "x")
    cg_report_file.write(cg_report_content)

print("All tasks finished. Have a nice day.")

# Close the files
cg_report_file.close()
trade_history_file.close()
live_pricedata_file.close()
client_ann_income_file.close()


''' Draw Piechart of the Portfolio Data '''
# Practice with pie charts
labels = []
explode = []
# Get the sized of the pies of stock for the pie chart
sizes = []

# TODO: Ensure the stocks in the labels list is in respect with the computed sizes
for folio in portfolio:
    labels.append(folio[0])
    explode.append(0)
    pie_size = (folio[2] / total_worth) * 100
    sizes.append(pie_size)

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=90)
ax.axis('equal')
plt.show()