''' Prompt for the file names '''
# TODO: Test with another file names
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


''' Learn about string formatting '''
formatted_row = '{:^15} {:^15} {:^15} {:^15} {:^15}'

# Create list of tuples
list_of_tuples = []
for lst in trade_history_list:
    tple = tuple(lst.split(','))
    list_of_tuples.append(tple)
header = ("Code |", "Buy/Sell |", "Date |", "Stock Held |", "Stock Rate")
print(formatted_row.format(*header))
separator = ""
for item in header:
    separator += ("-" * (len(item) + 7))
print(separator)
for row in list_of_tuples:
    print(formatted_row.format(*row))


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
                raise ValueError(f'Unknown data in the file: {trade_data_list[3]}')
            
            # Get the live price rate of the share
            for live_pricedata in live_pricedata_list:
                # Check if stock is contained in the live price data string
                if stock in live_pricedata:
                    # Get the list from the live price string data
                    live_list = list(live_pricedata.split(','))
                    share_price_rate = float(live_list[2])

                    # Compute the share value
                    if units_held:
                        value = units_held * share_price_rate

        # TODO Append the computed values in the list of potfolio



# Get the latest share price per unit from the live-prices file
# Compute the value of each stock

# Close the files
trade_history_file.close()
live_pricedata_file.close()
client_ann_income_file.close()