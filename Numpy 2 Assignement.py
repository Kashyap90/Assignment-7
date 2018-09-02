
# coding: utf-8

# In[1]:


# The Moving Avereage Sequence with 7 values

import numpy as np

dataset = [25, 35, 45, 55, 65, 75, 85]

def movingaverage(values, window):
    weights = np.repeat(7.0, window)/window
    smas = np.convolve(values,weights,'valid')
    return smas

print(movingaverage(dataset,4))


# In[2]:


# Moving Average in an array over a window, window=3

import numpy as np

dataset = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]

def movingaverage(values, window):
    weights = np.repeat(1.0, window)/window
    smas = np.convolve(values,weights,'valid')
    return smas

print(movingaverage(dataset,3))

