# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Xin Wang
#
# Date: 2/25/25
# 
##################################################
#
# Sample Script for Midterm Examination: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for another script that would
# execute the scripts (to run the doctests)
# and imports the modules to test the functions.
##################################################
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module
import numpy as np
import doctest


##################################################
# Function Definitions
##################################################


# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

def total_revenue(num_units: float, unit_price: float) -> float:
    """
    """
    revenue = num_units * unit_price
    return revenue

def total_cost(num_units: float, multiplier: float, fixed_cost: float) -> float:
    """
    """
    cost = multiplier * (num_units ** 2) + fixed_cost
    return cost

#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 1
def total_profit(num_units:float,unit_price:float,multiplier:float,fixed_cost:float) -> float:
    """
    >>> total_profit(10,10,.5,100)
    -50.0
    >>> total_profit(10,2,.1,100)
    -90
    >>> total_profit(2,2,.1,100)
    -96.4
    """
    profit = total_revenue(num_units, unit_price) - total_cost(num_units, multiplier, fixed_cost)
    return profit

# Exercise 2
def max_profit_calc(unit_price:float,multiplier:float, fixed_cost:float) -> float:
    """
    >>> max_profit_calc(10,.5,1)
    10
    >>> max_profit_calc(2,.1,100)
    0
    >>> max_profit_calc(2,11,100)
    0
    """
    q_max = unit_price/(2*multiplier)
    if total_profit(q_max, unit_price, multiplier, fixed_cost) > 0:
        return q_max
    else:
        return 0

# Exercise 3
def profit_max_q(q_max:float,step:float,unit_price:float,multiplier:float,fixed_cost:float):
    """
    >>> profit_max_q(100,10,12.4,.2,100)
    [-100,    4,   68,   92,   76,   20,  -76, -212, -388, -604]
    >>> profit_max_q(10,1,12.4,.2,100)
    array([-100,  -87,  -76,  -64,  -53,  -43,  -32,  -23,  -13,   -4])
    >>> profit_max_q(100,5,12.4,.2,100)
    array([-100,  -43,    4,   41,   68,   85,   92,   89,   76,   53,   20,
            -23,  -76, -139, -212, -295, -388, -491, -604, -727])
    """
    q_list = np.arange(0,q_max,step)
    profit_list = q_list
    for i in range(len(q_list)):
        profit_list[i] = total_profit(q_list[i], unit_price, multiplier, fixed_cost)
    return profit_list

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 
if __name__ == "__main__":
    doctest.testmod()

# Make sure to include examples in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 

    
    



##################################################
# End
##################################################
