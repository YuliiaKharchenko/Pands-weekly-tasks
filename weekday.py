# A program that outputs whether or not today is a weekday. 

# Autor: Yuliia Kharchenko 


# Import module datetime to get the current date

from datetime import datetime
current_date = datetime.now().date() # use this command to output current date

# print(current_date.weekday())
# use command weekday to get the number of current day as an integer and check the condition
 
if current_date.weekday() < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!") 
