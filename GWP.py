#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:31:18 2021

@author: BenSmith
"""
import numpy as np
import scipy 
from scipy.stats import norm
import math
import matplotlib.pyplot as plt
import pandas as pd


##### Parameters #####
periods = 20 # Periods to simulate
delta_t = 1 # Interval
p_0 = 60000 # Initial price 
mu = 0 # Mean 
sd = 5 # Standard deviation
drift = 1 # Drift of process
diffusion = 100 # Diffusion 


time = list(range(0, periods + 1)) #Vector of times t 

p = [0] * (periods + 1)
p[0] = p_0

delta_p = np.random.normal(mu,
                           sd,
                           periods)

def prediction():
 for t in time[1:periods+1]:
    p[t] = p[t-1] + (drift * delta_t) + (diffusion * math.sqrt(delta_t) * delta_p[t-1])


prediction()

plt.plot(time, p)






