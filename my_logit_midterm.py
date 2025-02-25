# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Xin Wang
#
# Date: 02/25/25
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
from typing import List
import numpy as np
import math
import doctest


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------

def logit(x:float, b_0:float, b_1:float) -> float:
    # calc
    p = math.exp(b_0 + x * b_1)
    return p/(1 + p) # just in case there is a rounding issue

def logit_like(y_i:int, x_i:float, b_0:float, b_1:float) ->float:
     # precondition check
    if y_i != 0 and y_i != 1: # if y_i is not 0 and y_i is not 1 at the same time
        #using OR does not work b/c OR shortcircuits for the left operand, and returns immediate True if y!=0 is True even if y=1
        print("Error! y_i must be equal to 1 or 0.")   
    # calc
    elif y_i == 1:
        x = x_i # necessary for wrapper, but it is also possible to write it as logit(x_i)
        return math.log(logit(x, b_0, b_1)) # missed taking the log of the function (-2)
    elif y_i == 0:
        x = x_i
        return math.log(1 - logit(x, b_0, b_1))

def logit_like_sum(y:list, x:list, b0:float, b1:float) -> float: # expected output? (-1)
    # precondition checks
    error = 0
    if len(y) != len(x): # CHECK if y and x lengths are not equal
        print("Error! y and x must contain same number of items")
        error += 1
    if not all(observation in [0,1] for observation in y): # CHECK if items in y are not only 0 or 1
        print("Error! y must be 0 or 1 only")
        error += 1
    if error > 0:
        print("Number of errors: " + str(error))
        return None
    # calc
    likelihood_sum = 0 # initialize variable before forloop

    for i in range(len(y)): # for all items in range the length of y
        p = math.exp(b0 + x[i]*b1)
        logit = p/(1 + p) # logit must be inside loop to iterate x[i]
        
        # special inside loop check that relies on x[i] and y[i]
        if y[i] == 0 and logit >= 1 : # CHECK if log of 0 or negative number, edge case which only occurs when y=0
            print("Cannot take log of nonpositive number. When y=1, logit must be less than or equal to 1")
            return None
        else:
            likelihood_sum += math.log(1 - y[i] + logit*(-1)**(1-y[i]))
            # if y[i]=1, takes the log of 1-1 + logit*1
            # if y[i]=0, takes the log of 1-0 + logit*-1
    
    # answer
    return likelihood_sum


#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------


# Exercise 6


def max_logit(y: List[float], x: List[float], 
        beta_0_min: float, beta_0_max: float, 
        beta_1_min: float, beta_1_max: float, 
        step: float) -> float:
    """
    Calculates the estimated coefficients 
    by grid search on the value of the logit_like_sum function
    for the logistic regesssion model 
    given two lists of data y and x.
    
    The search is taken over a grid of candidate values
    of beta_0 and beta_1 defined over
    np.arange(beta_0_min, beta_0_max, step) and
    np.arange(beta_1_min, beta_1_max, step), respectively.
    
    
    >>> max_logit([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], \
                  -2.0, 2.0, -2.0, 2.0, 0.10)
    [0.0, 0.0]
    >>> max_logit([1, 0, 1], [15.0, 10.0, 5.0], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.69, 0.0]
    >>> max_logit([1, 0, 1, 0, 1], [0, 0, 1, 1, 1], \
                  -1.0, 1.0, -1.0, 1.0, 0.01)
    [0.0, 0.69]
    """
    
    # Code goes here.
    beta_0_list = np.arange(beta_0_min,beta_0_max,step)
    beta_1_list = np.arange(beta_1_min,beta_1_max,step)
    
    max_logit_sum = float("-inf")
    
    for i in range(len(beta_0_list)):
        for j in range(len(beta_1_list)):
            value = logit_like_sum(y, x, beta_0_list[i], beta_1_list[j])
            if value > max_logit_sum:
                i_max = i
                j_max = j
                max_logit_sum = value
    
    answer = [float(round(beta_0_list[i_max],2)), float(round(beta_1_list[j_max],2))]
    return answer




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
