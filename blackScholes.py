import time
import datetime as dt
from math import sqrt, pi

import numpy as np
import matplotlib as mat


import matplotlib.pyplot as plt
plt.style.use("ggplot")

import scipy
from scipy.stats import norm

from mpl_toolkits.mplot3d import Axes3D

#underlying stock price
S = 65.0

# series of underlying stock prices to demonstrate a payoff profile
sSeries = np.arange(S - 10, S + 10, 0.01)

# strike price
K = 65.0

# risk free rate
r = 0.015

# volatility 
vol = 0.3

atm_call_prem = 3.30

# def call_payoff(S, K_): 
    # return np.maximum(S - K, 0.0)
call_payoff = lambda S, K: np.maximum(sSeries - K, 0.0)

#Normal cumulative density function
def N(z):
    
    return norm.cdf(z)

def black_scholes_call_value(S, K, r, t, vol):
    d1 =  (np.log(S / K) + (r + (vol ** 2.0) / 2.0) * t) * (1.0 / (vol * np.sqrt(t)))
    d2 = d1 - (vol * np.sqrt(t))
    
    return N(d1) * S - N(d2) * K * np.exp(-r * t)


#get call payoff at expiration
call_value_at_expiration = call_payoff(sSeries, K) - atm_call_prem

# get the value of the call option with one month left
call_value_one_month = black_scholes_call_value(sSeries, K, r, 1 / 12, vol) - atm_call_prem

# get the value of the call and put option with two months left to expiration
call_value_two_months = black_scholes_call_value(sSeries, K, r, 1 / 6, vol) - atm_call_prem

# get the value of the call and put option with three months left to expiration
call_value_three_months = black_scholes_call_value(sSeries, K, r, 1 / 4, vol) - atm_call_prem

# get the value of the call and put option with six months left to expiration
call_value_six_months = black_scholes_call_value(sSeries, K, r, 1 / 2, vol) - atm_call_prem

print(call_value_at_expiration)
print(call_value_one_month)
print(call_value_two_months)
print(call_value_three_months)
print(call_value_six_months)

# plot the call payoffs
plt.figure(3, figsize=(7, 4))
plt.plot(sSeries, call_value_at_expiration)
plt.plot(sSeries, call_value_one_month)
plt.plot(sSeries, call_value_two_months)
plt.plot(sSeries, call_value_three_months)
plt.plot(sSeries, call_value_six_months)
plt.axhline(y=0, lw=1, c="grey")
plt.title("Black-Scholes price of call option through time")
plt.xlabel("Underlying stock price, S")
plt.legend(["t=0", "t=0.083", "t=0.166", "t=0.25", "t=0.5"], loc=2)



    
    
    
    