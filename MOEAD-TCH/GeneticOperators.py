import numpy as np
import random
#Genetic Operators
#Check local parameters


#SBX with repair option 
def SBX_with_repair(n1,n2,eta, a = 0, b = 1): 

    def calcBeta(mu, eta):
        if mu <= 0.5:
            beta =  (2*mu)**(1/(eta+1))
        else:
            beta = (1/(2*(1-mu)))**(1/(eta+1))
        
        return beta
    
    # a = 0 # Lower
    # b = 1 # Upper
    repair = True

    while repair:
        beta = np.zeros(len(n1))
        mu = np.random.rand(len(n1))
        for i in range(len(beta)):
            beta[i]= calcBeta(mu[i],eta)
        

        c1 = 0.5*((1+beta)*n1 + (1-beta)*n2)
        c2 = 0.5*((1-beta)*n1 + (1+beta)*n2)

        #Repair option
        for i in range(len(c1)):
            if(a < c1[i]  and c1[i] < b):
                repair = False
            else:
                repair = True
                break
        
    return c1,c2

#DE Genetic Operator
def DE_with_repair(r1,r2,r3, CR = 1, a = 0, b = 1, F = 0.5):

    # a = 0 # lower 
    # b = 1 # Upper
    repair = True
    while repair: 
        y = np.zeros(len(r1))

       
        for idx, num in enumerate(r1):
            rand = round(random.random(),3)
            if rand <= CR:
                y[idx] = r1[idx] + F * (r2[idx] - r3[idx])
            else:
                y[idx] = r1[idx]
        
        #Repair option
        for i in range(len(r1)):
            if(a < y[i]  and y[i] < b):
                repair = False
            else:
                repair = True
                break

    return (y) 




def PLM(c1, eta):

    mu = np.random.rand(len(c1))
    for idx, num in enumerate(c1):
        r = mu[idx]
        if r <= 0.5:
            c1[idx] = (2*r + (1-2*r)*(1-num)**(eta+1))**(1/(eta+1))
        else:
            c1[idx] = 1 - (((2*(1-r)+2*(r-0.5)*(1-num))**(eta+1))**(1/(eta+1)))

    return c1 

#Use this mutation function
def PLM_with_repair(c1,eta, a = 0, b = 1):
    # a = 0 # lower 
    # b = 1 # Upper
    repair = True
    while repair: 
        mu  = np.random.rand(len(c1))
        c_m = np.zeros(len(c1))
        for idx, num in enumerate(c1):
            r = mu[idx]
            if r < 0.5:
                c_m[idx] = c1[idx] + ((((2*r)**(1/(eta+1)))-1)*(b-a))
            else:
                c_m[idx] = c1[idx] +  (1 - (2-2*r)**(1/(eta+1))*(b-a))   
        
        #Repair option
        for i in range(len(c1)):
            if(a < c_m[i]  and c_m[i] < b):
                repair = False
            else:
                repair = True
                break

    return (c_m) 

