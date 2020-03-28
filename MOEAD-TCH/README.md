## MOEA/D: Multiobjective Evolutionary Algorithm Based on Decomposition
-This is a python implementation of MOEA/D [1] with tchebycheff decomposition function, "MOEAD.py".  
-As in the original paper, was used Simulated Binary Crossover and Polynomial Mutation, "GeneticOperators.py".  
-It was tested on ZDT 1-4 [2], "BenchmarkFunctions.py".  
-For 3 Objectives test, it was used the module benchmarks from deap [3] and the DTLZ1 [4] 


## Experiments Results
### ZDT1-4
-H = 299  
-Generations = 2000  

![](Figure/Result.png)

### DTLZ1
-H = 30  
-Generations = 5000  

![](Figure/DTLZ1.png)


## References
[1] Q. Zhang and H. Li, "MOEA/D: A Multiobjective Evolutionary Algorithm Based on Decomposition," 
    in IEEE Transactions on Evolutionary Computation, vol. 11, no. 6, pp. 712-731, Dec. 2007.  
[2] Zitzler, E., Deb, K., Thiele, L.: “Comparison of Multiobjective Evolutionary Algorithms: 
    Empirical Results”, Evolutionary Computation, vol. 8, n° 2, pp. 173-195, 2000  
[3] Deap library Website - https://deap.readthedocs.io/en/master/index.html  
[4] K. Deb, L. Thiele, M. Laumanns, and E. Zitzler, “Scalable multiobjective optimization test 
    problems,” in Proc. Congr. Evol. Comput.,May 2002, vol. 1, pp. 825–830
