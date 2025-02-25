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

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

#--------------------------------------------------
# Question 1
# Functions from Previous Assignments
#--------------------------------------------------
def CESutility(x: float, y: float, r: float) -> float:
    """Return the theoretical degree of satisfaction a customer may get from goods x and y 
    using r, the degree which the goods are complements or substitutes.
    
    >>> CESutility(40, 30, .5)
    8.615612366938898
    >>> CESutility(40, 30, -.5)
    139.28
    >>> CESutility(5, 5, 1)
    10
    """

    # function fails at r = 0 (-1)

    answer = (x ** r + y ** r) ** (1/r)
    return answer

def CESutility_valid(x:float, y:float, r:float) -> float:
    """CESutility_valid finds the Constant Elasticity of Substitution utility function,
    it calculates the two goods x and y, and the elasticity parameter r, when given 
    non-negative numbers for x and y and a strictly positive number for r.
    
    >>> CESutility_valid(3, 2, 1)
    5.0
    >>> CESutility_valid(-3, 2, 1)
    Error! x cannot be negative.
    None
    >>> CESutility_valid(3, -2, 1)
    Error! y cannot be negative.
    None
    """
    # precondition checks
    if x < 0:
        print("Error! x cannot be negative.")
        return None
    if y < 0:
        print("Error! y cannot be negative.")
        return None
    if r <= 0:
        print("Error! r must be positive")
        return None
    # calc
    else:
        answer = CESutility(x, y, r)
        return answer

def CESutility_in_budget(x:float, y:float, r:float, p_x:float, p_y:float, w:float) -> float:
    """CESutility_in_budget is a wrapper of CESutility_valid, making sure that the purchase is
    withing budget by checking on the total expenditures of the first two goods x and y and checking
    to see if it exceeds the budget w, within the prices set by p_x and p_y.
    
    >>> CESutility_in_budget(5, 4, .5, 6, 2, 56)
    17.95
    >>> CESutility_in_budget(2, 4, .5, 6, 2, 12)
    Error! Not in budget.
    None
    >>> CESutility_in_budget(-2, 4, 5, 6, 2, 12)
    Error! x cannot be negative.
    None
    """
    # precondition checks for new variables not found in CESutility_valid
    if p_x < 0 or p_y < 0: # missed checking for a negative price (-1)
        # if either p_x or p_y is < 0
        # AND does not work b/c AND can only check if both ops are True, thus does not work for is only 1 op is < 0
        print("Error! Cannot have negative prices.")
        return None
    elif w < ((p_x * x) + (p_y * y)):
        print("Error! Not in budget.")
        return None
    # calc, relies on CESutility_valid as a wrapper
    else:
        return CESutility_valid(x, y, r)


#--------------------------------------------------
# Question 2
# New Functions
#--------------------------------------------------

# Exercise 4


# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


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
