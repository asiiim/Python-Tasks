# Write a function to check if a password (received as parameter) matches the
# following criteria:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Examples:
# f(‘ABd1234@1’) returns True
# f(‘2w3E*’) returns False
# f(‘abcd’) returns False

import re

def f(password):
    if len(password) in range(6, 13):
        if re.search('[a-z]', password):
            if re.search('[A-Z]', password):
                if re.search('[0-9]', password):
                    if re.search('[$#@]', password):
                        print(True)
    else:
        print(False)

password = input("Enter password: ")
f(password)
