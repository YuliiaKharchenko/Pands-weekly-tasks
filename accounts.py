# Accounts 
# This program reads in a 10 character account number 
# and outputs the account number with only the last 4 digits 
# showing (and the first 6 digits replaced with Xs).
# Autor Yuliia Kharchenko 

accountnumber = str(input ("Please enter a 10 digit account number: "))

# print(accountnumber)

# lenghtofaccountnumber = len(accountnumber)
# print(lenghtofaccountnumber)

# print(accountnumber.replace(accountnumber[:6], "XXXXXX"))

print(accountnumber.replace(accountnumber[:6], "XXXXXX")) if len(accountnumber)==10 else print("Incorrect number of digits")

# it may be necessary to notify the user that the length of the account number is incorrect if it is not equal to 10?