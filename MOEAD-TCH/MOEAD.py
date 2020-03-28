# local functions Imports (Same Folder)
from BenchmarkFunctions import ZDT
from GeneticOperators import SBX_with_repair as SBX, PLM_with_repair as PLM
#Python modules Imports
import numpy as np 
import matplotlib.pyplot as plt
from itertools import  combinations_with_replacement, product
import math
import random 


# ------------------------------ Functions -----------------------
# s1 dominates  s2 ? 
def dominates(s1,s2):
    return  any(s1<s2) and all(s1<=s2)

def checkDominance(cost):

    isDominated = np.zeros(len(cost))

    for i in range(len(cost)):
        for j in range((i+1),len(cost)):
            if dominates(cost[i],cost[j]):
                isDominated[j] = 1
            elif dominates(cost[j],cost[i]):
                isDominated[i] = 1
                
    return isDominated

#Step 0, generate weight vectors 
def generateVectors(nProb, H):

    vet=np.linspace(0,1,H+1)
    perm = product(vet, repeat=nProb)
    # perm = permutations(vet,nProb)
    vectors = []
    sums = []
    for i in list(perm):
    #    vectors.append(i)
        if round(sum(i),2) == 1:
            vectors.append(i)  

    return (vectors)
 
#Step 1.2 Neighborhood - Euclidiean Distances
def calcNeighborhood(vets,T):
    #Calculate distances
    neighborhood = []
    for num1 in vets:
        dist = np.zeros((len(vets),2))
        #dist = np.zeros(len(vets))
        for idx, num2 in enumerate(vets):
            # Calculates all distance from num1
            dist[idx, :] = idx, (math.sqrt(sum(np.subtract(num1,num2)**2))) 

        neighborhood.append(dist[dist[:,1].argsort()][0:T, 0])

    return neighborhood

# Decomposition Function of TCH
def decomposition_TCH(lb, z, cost):
    return max(np.multiply(lb,abs(z - cost)))

### ============== Code ===================

## === Problem Characteristcs
# Type of Cost functions (ZDT(Type))
Ftype = 1
# Number of variables
nVar = 3
#Number of problems
nProb = 2

# === Configurations for Evolution ====
#Number of Generations to Run
generation = 2000
# simplex-lattice parameter
H = 299

#Genetic operators parameters
eta_c = 20
eta_m = 20

# === Initialization ====

#Generating Weight Vectors
vectors = generateVectors(nProb, H)
size = len(vectors)

#Size of external population
maxSizeEP = size

#Size of neighborhood
T = int(0.10*size)
# Defining Neighborhood
neighborhood = calcNeighborhood(vectors, T)

#Generating Random population
pop = np.around(np.random.rand(size,nVar), decimals= 4)

#Calculating Initial Costs 
cost = np.zeros((size,nProb))
for idx, x in enumerate(pop):
    cost[idx,:] = ZDT(x, Ftype)
#z
z = cost.min(axis = 0)

# cost, m1, m2 = normalizeCosts(cost)
#Initial Decomposed Costs (called g)
g = []
for i in range(len(cost)):
    g.append(decomposition_TCH(vectors[i],z,cost[i]))


#External population initialization 
isDominated = checkDominance(cost)
EP = pop[isDominated != 1]

# === Main Loop ===
for gen in range(generation):

    print(f"Generation: {gen+1} / {generation} - Size of EP: {len(EP)}")
    
    for i in range(len(pop)):
        
        #Selection of parents
        n1, n2 = np.random.choice(neighborhood[i],size= 2, replace = False)
        #SBX
        c1, c2 = SBX(pop[int(n1)],pop[int(n2)],eta_c)
        #PM
        c1 = PLM(c1,eta_m)
        
        costChild = ZDT(c1, Ftype)
        
        #Step 2.4) Update Neighboring Solutions
        #Check neighborhood and change for best solution with best g
        for n in neighborhood[i]:
            n = int(n) # temporary!!!FIX LATER
            gChild = decomposition_TCH(vectors[n], z, costChild)
            if gChild <= g[n]:
                pop[n] = c1
                cost[n] = costChild
        #Update z
        z = np.vstack((z,cost)).min(axis = 0)

    isDominated = checkDominance(cost)
    EP_temp = pop[isDominated != 1] 
    EP = np.vstack([EP,EP_temp])
    EP = np.unique(EP,axis = 0)

    cost_EP = np.zeros((len(EP),nProb))
    for idx, x in enumerate(EP):
        cost_EP[idx,:] = ZDT(x, Ftype)    

    isDominated = checkDominance(cost_EP)
    EP = EP[isDominated != 1]

    #limit EP size 
    if len(EP) > maxSizeEP:
        remove = list(np.random.randint(len(EP),size = ( len(EP) - maxSizeEP)))
        EP = np.delete(EP, (remove),0)


#End Summary
print(f"\nSummary: \n-Number of generations: {generation} \n-Size of EP: {len(EP)}")


    
