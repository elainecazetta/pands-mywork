# This program displays a histogram of a normal distribution 
# of a 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function h(x)=x3 in the range 0 to 10
# Source: W3Schools (libraries, histogram, normal distribution, title, labels and grid)
# Source: AI models (np.linspace, function h(x)=x3, figure and figsize)
# Author: Elaine Cazetta

import numpy as np
import matplotlib.pyplot as plt

# Histogram:
# Number 5 is the mean, 2 is the STD and 1000 is the number of values
# using functions 'normal' and 'random' to get a randomic normal distribution
x_hist = np.random.normal(5, 2, 1000) 

# Plot:
# Generate x values for the function h(x) = x^3 in range 0 to 10
# Got help from AI to create x and y:
x = np.linspace(0, 10, 100)
y = x ** 3  # h(x) = x^3 

# Customize Figure Size
plt.figure(figsize=(8, 6))

# plot histogram and plot
plt.hist(x_hist, edgecolor='black', label='Normal Distribution (mean=5, std=2)') 

plt.plot(x, y, color='red', label='h(x) = x^3')

plt.title("Histogram & Plot") # Add a title to the histogram
plt.xlabel("Distribution")  # Add x axis label
plt.ylabel("Frequency") # Add y axis label
plt.grid(axis = 'y', linestyle = '--', linewidth = 0.5) # Add grid lines
plt.legend() # Add legend

plt.show() # Displays the chart

plt.savefig('plottask.png') # Saves the chart as a .png file




