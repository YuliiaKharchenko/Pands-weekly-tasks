# The program displays a histogram and a plot with different display conditions 
# on the one set of axes.

# Autor: Yuliia Kharchenko 

import numpy as np    # call the module 
import matplotlib.pyplot as plt   # call the module

normdist = np.random.normal(5,2,1000)  # get the variables according to the first condition
# print(normdist)

xpoint = np.array(range(1,10)) # get the variables according to the second condition
xpoint = pow(xpoint,3) # use the function to calculate the variables
# print(xpoint)

plt.hist(normdist,color='g',label= "normal_dist_of_1000_values") # histograms function, colour of greens, label name
plt.plot(xpoint, 'o-r', label=" h(x)=x**3")    # plots function, colour of reds with marckers, label name
plt.title("Visualisation of two types of plots") # Title name 
plt.grid() # add grid lines to the plot
plt.legend() # run the legend 
plt.show() # show the result 
# plt.savefig('visualisation.png')