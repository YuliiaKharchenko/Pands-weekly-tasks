# The program reads in a text file and outputs the number of e's it contains. 
# (I assume that we need to count the total number of "e" letters in the text, 
# both small and capital letters.)
# Autor: Yuliia Kharchenko 

Filename="Escount.txt" # the name of file

# create a function that reads the file in format "read text" and does calculations 
def readFile():
   # use block try...except to handle the error if file doesn't exist
   try:
    with open(Filename,'rt') as f:  # open a file in text fofmat 
      data = f.read()             # read a file
      # print(type(f))            # i was checking the type
      escount = data.count("e")+data.count("E")  # do calculations 
    print(escount)      # print out the result 

   except FileNotFoundError:
    print(Filename, "does not exist!") # output the message when an error occurs
   # except 
readFile() # run the function