# A study revealed the following.
# Alcohol consumption in a population is measured on a scale of 0 - 100.
# (0 - minimum  100 - maximum)
#
# Water consumption in the population is measured on a scale of 0 - 10.
# (0 - minimum  10 - maximum)
#
# The life span of the population is defined on a scale of 10 - 50
# (10 - maximum    50 - minimum)
#
# Given the drinks consumption of an individual determine the lifespan
#
# R1 : Less water and more alcohol implies poor life span
# R2 : More water and less alcohol implies good life span
# R3 : More water and average alcohol or less water and less alcohol implies average life span
 
import numpy as np
import matplotlib.pyplot as plt
 
def inc(x,a,b):
    if(x<a):
        return 0
    elif (x>b):
        return 1
    else:
        return((x-a)/(b-a))
   
def dec(x,a,b):
    return (1-inc(x,a,b))
 
def trapz(x,a,b,c,d):
    if(x<c):
        return(inc(x,a,b))
    else:
        return(dec(x,c,d))
 
def gauss(x,m,s):
    r = np.exp(-(x-m)**2/s**2)
    return r
 
def sig(x,a,b):
    r = 1/(1+np.exp(-a*(x-b)))
    return r
 
# Model the input and output variables
alc = np.linspace(0,100,200)
m_alc = np.array([inc(x,50,70) for x in alc])
l_alc = np.array([dec(x,20,40) for x in alc])
a_alc = np.array([gauss(x,45,15) for x in alc])
 
water = np.linspace(0,10,100)
m_water = np.array([sig(x,1.5,6) for x in water])
l_water = np.array([sig(x,-1,4) for x in water])
 
life = np.linspace(10,50,100)
good_l = np.array([sig(x,-0.6,20) for x in life])
avg_l = np.array([trapz(x,18,25,35,45) for x in life])
poor_l = np.array([sig(x,0.5,40) for x in life])
 
 
#Read input and evaluate the memberships
inp_water = 5
m_inp_water = sig(inp_water,1.5,6)
l_inp_water = sig(inp_water,-1,4)
 
inp_alc = 75
m_inp_alc = inc(inp_alc,50,70)
a_inp_alc = gauss(inp_alc,45,15)
l_inp_alc = dec(inp_alc,20,40)
 
# Rule Evaluation
# R1 : Less water and more alcohol implies poor life span
antec1 = np.min((l_inp_water,m_inp_alc))
R1 = np.fmin(antec1,poor_l)
 
# R2 : More water and less alcohol implies good life span
antec2 = np.min((m_inp_water,l_inp_alc))
R2 = np.fmin(antec2,good_l)
 
# R3 : (More water and average alcohol) or (less water and less alcohol) implies average life span
a1 = np.min((m_inp_water,a_inp_alc))
a2 = np.min((l_inp_water,l_inp_alc))
antec3 = np.max((a1,a2))
R3 = np.fmin(antec3,avg_l)
 
# Rule Summarization and Defuzzification
R = np.maximum(np.maximum(R1,R2),R3)    #R = R1+R2+R3
 
output_life = np.trapezoid(R*life,life)/np.trapezoid(R,life)
print("Expected Life : ",output_life)
 
 
# Plots
plt.figure(0)
plt.subplot(1,2,1)
plt.plot(alc,l_alc,label="Less Alc")
plt.plot(alc,a_alc,label="Avg Alc")
plt.plot(alc,m_alc,label="More Alc")
plt.scatter([inp_alc,inp_alc,inp_alc],[l_inp_alc,a_inp_alc,m_inp_alc])
plt.legend()
 
plt.subplot(1,2,2)
plt.plot(water,l_water,label="Less Water")
plt.plot(water,m_water,label="More Water")
plt.scatter([inp_water,inp_water],[l_inp_water,m_inp_water])
plt.legend()
 
plt.figure(1)
plt.plot(life,good_l,label="Good Life")
plt.plot(life,avg_l,label="Avg Life")
plt.plot(life,poor_l,label="Poor Life")
plt.fill_between(life,R1,label="R1")
plt.fill_between(life,R2,label="R2")
plt.fill_between(life,R3,label="R3")
# plt.scatter(output_life,0)
plt.legend()
plt.show()