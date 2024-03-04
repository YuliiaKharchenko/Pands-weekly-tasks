# Bank 
# This program adds two amounts and prints out the result in a readable format 
# Autor Yuliia Kharchenko 

number1 = int(input('Enter amount1(in cent): ')) #allows the user to enter the first amount, type integer

number2 = int(input('Enter amount2(in cent): ')) #allows the user to enter the second amount, type integer

numberincent= number1 + number2

# print(numberincent)
Euro = numberincent//100 #use division without remainder to get only euros
Cent = numberincent%100 #get the remainder separately to avoid floating-point variables


print (f'The summ of these is €',Euro,".",Cent)
# output the result to the user in a readable format
