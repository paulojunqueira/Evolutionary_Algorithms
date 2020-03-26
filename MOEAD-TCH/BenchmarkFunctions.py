import math
import numpy as np
#Cost Function Bi-objective 
# x = Solution variable
# Ftype = ZDT problem option 
def ZDT(x, Ftype,pRound = 2):
    n = len(x)

    if Ftype == 1:
        f1 = x[0]
        g = 1 + 9* sum(x[1:]/(n-1))
        h = 1- math.sqrt(f1/g)
        f2 = g*h
    elif Ftype == 2:
        f1 = x[0]
        g = 1 + 9* sum(x[1:]/(n-1))
        h = 1 - (f1/g)**2
        f2 = g*h
    elif Ftype == 3:
        f1 = x[0]
        g = 1 + 9* sum(x[1:]/(n-1))
        h = 1- math.sqrt(f1/g) - (f1/g)*math.sin(10*math.pi*f1)
        f2 = g*h
    elif Ftype == 4:
        f1 = x[0]
        g = 1 + 10*(n-1) + sum(x[1:]**2 - 10*np.cos(4*math.pi*x[1:]))
        h = 1- math.sqrt(f1/g)
        f2 = g*h

    return round(f1,pRound),round(f2,pRound)