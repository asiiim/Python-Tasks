# Write a function that receives a sequence of whitespace separated words as a
# parameter and prints the words after removing all duplicate words and sorting
# them alphanumerically. Suppose the following string is supplied to the
 
# function: 'hello world and practice makes perfect and hello world again' Then,
# then it should print: 'again and hello makes perfect practice world'.

def get_unique_alphanumeric(text):
    text_list = text.split(" ")
    text_list = list(dict.fromkeys(text_list))
    text_list.sort()
    print(" ".join(text_list))

text = input("Write some whitespace separated words !\n")
get_unique_alphanumeric(text)