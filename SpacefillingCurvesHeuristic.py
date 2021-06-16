# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 23:25:43 2021

@author: jfb2444
"""

# Imports
import numpy as np
from scipy.stats import rankdata
import matplotlib.pyplot as plt

# Code based on Bartholdi (1995)


# Data
maxInput = 1
n = 5
np.random.seed(42)

xCoord = [np.random.uniform(0, maxInput) for i in range(n)]
yCoord = [np.random.uniform(0, maxInput) for i in range(n)]



###############################################################################
############################## Sierpinski Index ###############################
###############################################################################
# Get postions of each node along the sierpinski curve

# Copy coordiantes
x = xCoord[:]
y = yCoord[:]

loopIndex = maxInput
results = np.zeros((n))

tmpSet = set(results)
#    print(len(tmpSet))

for i in range(n):
    if(x[i] > y[i]):
        results[i] = results[i] + 1
        x[i] = maxInput - x[i]
        y[i] = maxInput - y[i]
    
while len(tmpSet) < n:
    
    for i in range(n):
        results[i] = results[i] + results[i]
        
        if(x[i] + y[i] > maxInput):
            results[i] = results[i] + 1
            x_old = x[i]
            x[i] = maxInput - y[i]
            y[i] = x_old
            
        x[i] = x[i] + x[i]
        y[i] = y[i] + y[i]
        results[i] = results[i] + results[i]
        
        if(y[i] > maxInput):
            results[i] = results[i] + 1
            x_old = x[i]
            x[i] = y[i] - maxInput
            y[i] = maxInput - x_old
        
    loopIndex = loopIndex + 1  
    tmpSet = set(results)      
        
# Get sequence/position based on results vector
positions = rankdata(results) - 1   
positions = positions.tolist()


###############################################################################
################################## Plot tour ##################################
###############################################################################

plt.xlim(0, 1)
plt.ylim(0, 1)
fig = plt.scatter(xCoord, yCoord, c='k')

initIndex = positions.index(0)
currIndex = initIndex
count = 0
#print('init:', currIndex)

while count < n-1:
    
    # Find next element
    for i in range(n):
        if(positions[i] == count + 1 ):
            nextIndex = i
            #print(nextIndex)
            count = count + 1
            break
    
    # Plot line segment    
    x_values = [xCoord[currIndex], xCoord[nextIndex]]
    y_values = [yCoord[currIndex], yCoord[nextIndex]]
    plt.plot(x_values, y_values, 'grey')
    
    # Update current element
    currIndex = nextIndex

# Plot last line segment
x_values = [xCoord[currIndex], xCoord[initIndex]]
y_values = [yCoord[currIndex], yCoord[initIndex]]
plt.plot(x_values, y_values, 'grey')
