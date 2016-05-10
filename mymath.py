#This module implement some simple math operations:

import numpy as np

#-------MYCEIL_DIV2 -> take an integer number and return the ceiling of its division by 2

def myceil_div2(i):
    return i/2 + i % 2


#-------MYFLOOR_DIV2 -> take an integer number and return the floor of its division by 2

def myfloor_div2(i):
    return i/2 

#----- MYMOD_ABS -> take an integer number and return mod_2 of its anbsolute value

def mymod_abs(i):
    return abs(i) % 2

#-----MYNORM -> take the norm of an array "x"

def mynorm(x):
    return np.max(np.abs(x))


#print np.abs([1,2])
