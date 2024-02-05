# Bank 
# This program adds two amounts and prints out the result in a readable format 
# Autor Yuliia Kharchenko 


number1 = int(input('Enter amount1(in cent): '))
Newnumber1 = number1/100
number2 = int(input('Enter amount2(in cent): '))
Newnumber2 = number2/100
answer = Newnumber1 + Newnumber2
currency = '€'
print (f'The summ of these is {currency}{answer:.2f}')
