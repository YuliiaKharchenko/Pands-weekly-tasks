# The program takes a positive floating-point number as input 
# and outputs an approximation of its square root.

# Autor: Yuliia Kharchenko 

number = abs(float(input("Please enter a positive number: ")))
# allows the user to enter a floating-point number, 
# the abs command ensures that only a positive number is entered 

# print(number)

# create a function sqrt, which calculates the most approximate value of the square root of a number. 
# deviation can be set to whatever the user needs for the calculation. Here the default is 0.01

def sqrt(number, deviation=0.01):
 answer = number/2 # the output answer is assumed to be equal to the input variable divided by two
 while (answer*answer-number)>=deviation: # run a loop to calculate the square root of a number using Newton's method until the answer is the closest to the loop condition.
   answer = (answer+number/answer)/2
  
 print(f"The square root of ",number, "is approx. ",answer) # print out the answer in the readable format 

sqrt(number) # run a function 