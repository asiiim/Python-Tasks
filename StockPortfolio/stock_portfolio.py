import matplotlib.pyplot as plt

''' Prompt for the file names '''
# TODO: Test with another file names
# TODO: Handle exception if file name is not matched or not found
trade_history_filename = input("Trade history file (trades.txt): ") or 'trades.txt'
print(trade_history_filename)
live_pricedata_filename = input("Live price data file (live-prices.txt): ") or 'live-prices.txt'
client_ann_income_filename = input("Client's annual income records (income.txt):") or 'income.txt'


''' File handling '''
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
trade_history_new_list = []
for data in trade_history_list:
    sublist = list(data.split(','))
    trade_history_new_list.append(sublist)

# Get the unique list of stocks appeared in the trade history file
stock_list = []
for data in trade_history_new_list:
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
print('{:<20} {:<20}'.format(*['Total Worth', str(total_worth)]))
print("\n(2) Pie chart of portfolio opens in new window")
print("\n(3) CGT Report")

# Close the files
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