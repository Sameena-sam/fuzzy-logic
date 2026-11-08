#increasing membership

import numpy as np
import matplotlib.pyplot as plt

def increase_membership(x, a, b):
    if x <= a:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return 1
    
a = 5
b = 20 
y = [increase_membership(x, a, b) for x in range(0, 26)]

#decreasing membership

def decrease_membership(x, a, b):
    if x <= a:
        return 1
    elif a < x <= b:
        return (b - x) / (b - a)
    else:
        return 0
    
a = 5
b = 20
y = [decrease_membership(x, a, b) for x in range(0, 26)]

#triangular membership
def triangular_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)
    
a = 5
b = 15
c = 25
y = [triangular_membership(x, a, b, c) for x in range(0, 31)]

def anme(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1
    else:
        return (d - x) / (d - c)
    
a = 5
b = 10
c = 20
d = 25
y = [anme(x, a, b, c, d) for x in range(0, 31)]

import numpy as np
import matplotlib.pyplot as plt
 
def inc(x,a,b):
    if(x<=a):
        y= 0
    elif(x>=b):
        y=1
    else:
        y=(x-a)/(b-a)
    return(y)
 
def dec(x,a,b):
    return(1-inc(x,a,b))
 
def gauss(x,mu,sig):
    y=np.exp(-(x-mu)**2/sig**2)
    return(y)
 
x = np.linspace(0,20,100)
y=[gauss(x1,5,4) for x1 in x]
 
