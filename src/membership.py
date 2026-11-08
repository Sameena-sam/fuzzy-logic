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
    y=np.exp(-(x-mu)**2/sig)
    return(y)
 
def trapezoid(x,a,b,c,d):
        if(x<=a):
            y=0
        elif(a<x<=b):
            y=(x-a)/(b-a)
        elif(b<x<=c):
            y=1
        elif(c<x<=d):
            y=(d-x)/(d-c)
        elif(d<x):
             y=0
        return y
 
 
