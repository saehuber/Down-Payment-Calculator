# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# This calculator is designed to calculate the optimal investment strategy over time, comparing home equity growth vs. investment growth.
# 
# Many wild assumptions ahead, but hopefully at least the math is correct.
# 
# We should also answer a couple of questions, like:
# Should you pay your mortgage as quickly as possible, or invest additional available income instead?
# 
# Should make it so that you can start at a later year. Plots over a variety of values

#%%
import numpy as np
import matplotlib.pyplot as plt

#%% [markdown]
# Some important variables:
# note: do we also want to consider their uncertainty?
# We probably want to separate these into their own cells, each with sources/derivation
# 
# Also: compare rental costs?
# 
# All of these are per year costs, except for a couple which are one time costs

#%%
# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'config/')

import credentials


### Import FRED data
#%%
data = fred.get_series_first_release('GDP')
data.tail()

#%%
initial_savings = 50000 #amount available to spend in year 0
home_cost = 200000 #cost of a home
yearly_surplus = 5000 #amount set aside for investment
expected_interest_rate = 3.5 #assumed average interest rate per year
expected_inflation_rate = 3 #assumed average inflation per year
expected_investment_growth_rate = 7.5 #expected growth rate per year for investments
expected_home_equity_growth_rate = 7.5 #expected growth in value of home per year
home_purchase_costs = 5000 #costs of buying a home
#home_maintainance_costs = 1000 #average amount spend per year on home 
#capital_gains_tax = 5 #tax rate on contributions over tax free amount?
#property_tax = 2 #tax rate for property
down_payment = 20 #percentage of home you pay initially
prime = 1
mortgage_rate = expected_interest_rate + prime # Should we assume rental income = mortgage here? 
#can maintainance costs be ommitted then too?
yearly_invested = yearly_surplus #could be a percentage; extra goes to mortgage
years = 30
years_arr = np.arange(0,years)
mortgage_years = 30

#%% [markdown]
# The cost of home ownership per year: TODO should this really be an additional factor? Assuming a house is purchaced, it's kind of a fixed cost.

#%%


#%% [markdown]
# Mortgage payments are calculated as the mortgage rate $\times$ outstanding debt
# 
# Here we calculate the mortgage payments for each year, assuming a fixed rate mortgage with the interest rate defined above

#%%
principal = home_cost - down_payment
yearly_mortgage_payment = principal * ( (expected_interest_rate / 100) * np.power(1 + expected_interest_rate / 100, mortgage_years) / (np.power(1 + expected_interest_rate / 100, mortgage_years) - 1))
mortgage_payments = mortgage_rate * years_arr

#%% [markdown]
# Home equity: home value increases per year, home equity grows with home value and with decreased debt due to mortgage payments

#%%
home_value = home_cost*np.power(1+(expected_home_equity_growth_rate-expected_inflation_rate)/100,years_arr)
debt = (home_cost - down_payment) - mortgage_payments
home_equity_value = home_value - debt


#%%
print (home_equity_value)


#%%
plt.plot(years_arr,home_equity_value)
plt.ylabel("$ home equity value")
plt.xlabel("years")

#%% [markdown]
# Value of investments:

#%%
initial_investment = initial_savings - home_cost * down_payment / 100 - home_purchase_costs


#%%
print (initial_investment)


#%%
print (yearly_invested) 
print (yearly_surplus  * np.power(1+(expected_investment_growth_rate) - (expected_inflation_rate)/100,years_arr))
sum = np.cumsum(yearly_invested*np.power(1+(expected_investment_growth_rate-expected_inflation_rate)/100,years_arr)) 
print (sum)


#%%
investment_value = initial_investment*np.power(1+(expected_investment_growth_rate-expected_inflation_rate)/100,years_arr)+sum


#%%
print (investment_value)


#%%
plt.plot(years_arr,investment_value,"ro")
plt.ylabel("$ investment value")
plt.xlabel("years")

#%% [markdown]
# Showing everything together....

#%%
plt.plot(years_arr,investment_value,"r-", label="Investment value")
plt.plot(years_arr,home_equity_value,"b-",label="Home value")
plt.plot(years_arr,home_equity_value,"k-",label="Total value")
plt.ylabel("$ value")
plt.xlabel("years")
plt.legend()


#%%



