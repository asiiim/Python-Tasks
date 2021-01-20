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
# Get the latest share price per unit from the live-prices file
# Compute the value of each stock

# Close the files
trade_history_file.close()
live_pricedata_file.close()
client_ann_income_file.close()