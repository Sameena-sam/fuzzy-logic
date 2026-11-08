import membership as memb
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,100,200)
Y = [memb.gauss(x1,20,30) for x1 in x]
VY = [memb.gauss(x1,10,15) for x1 in x]
M = [memb.gauss(x1,30,40) for x1 in x]
O = [memb.inc(x1,50,30) for x1 in x]

#x = np.linspace(0,100,200)
#Y = [memb.gauss(x1,25,32) for x1 in x]
#VY = [memb.gauss(x1,15,32) for x1 in x]
#M = [memb.gauss(x1,35,32) for x1 in x]
#O = [memb.gauss(x1,50,32) for x1 in x]


plt.figure(0)
plt.plot(x,VY,label="VY")
plt.plot(x,Y,label="Y")
plt.plot(x,M,label="M")
plt.plot(x,O,label="O")
plt.legend()
plt.xlabel("Age")
plt.ylabel("Membership")
plt.show()
 

