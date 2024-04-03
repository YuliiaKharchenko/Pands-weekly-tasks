# The program reads in a text file and outputs the number of e's it contains. 
# (I assume that we need to count the total number of "e" letters in the text, 
# both small and capital letters.)
# Autor: Yuliia Kharchenko 

# Filename="Escount.txt" # the name of the file

# call module sys that provides functions and variables used 
# to manipulate different parts of the Python runtime environment
import sys 
# create a function that reads the file in format "read text" and does calculation
def readFile():
   # use block try...except to handle the errors if file doesn't exist and if it's missing as a command line argument 
   try:
      Filename = sys.argv[1] # the list of command line arguments passed to a Python script.Index 1 points to the first value after the programme name
      # print(Filename)
      with open(Filename,'rt') as f:  # open a file in text fofmat 
           data = f.read()             # read a file
           # print(type(f))            # i was checking the type
           escount = data.count("e")+data.count("E")  # do calculation 
           print(escount)      # print out the result 
   
   except IndexError: # the error type
         print("Please enter the Filename as an argument") # output the message when an error occurs
   except FileNotFoundError: #the error type 
         print(Filename, "does not exist!") # output the message when an error occurs
   
readFile() # run the function