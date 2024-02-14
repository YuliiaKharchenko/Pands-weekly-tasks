# The program that asks the user to input any positive integer 
# and outputs the successive values of the following calculation.

# Autor Yuliia Kharchenko 

numbers=[] # Create a List
# ask the user to input any positive integer, use function abs 
# to eliminate the error when entering a negative integer 
Number = abs(int(input("Please enter a positive integer: ")))

# run the loop for a given condition (Have the program end if the current value is one)
while Number != 1:
  numbers.append(Number) # Add each received value to the list
  # start the calculation
  if (Number % 2) == 0:
    Value = Number//2
    # print(Value)
  else:
    Value = Number*3+1
    # print (Value)
  Number=Value # At each step calculate the next value

numbers.append(1) # add 1 to the list as the last element 
print(*numbers) # output the obtained values in a list without brackets and separators using 


