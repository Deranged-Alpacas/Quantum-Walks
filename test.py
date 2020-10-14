from GluedTrees import ReducedGluedTree, GluedTree
from QuantumWalk import QuantumWalk
import numpy as np
import scipy as sp
from heapq import nsmallest
from matplotlib import pyplot as plt

def eff_res(n):
    # returns the effective resistance
    r = 0
    for i in range(n-1):
        r += 2.*2.**(-i-1)
    r += 2.**(-n)
    print("EFFECTIVE RESISTANCE: {}".format(r))
    return r

n = 2
#print(2*(2**n - 1) - 1)
g = GluedTree(n, {0}, {2*(2**n - 1) - 1})
#print(np.array2string(g.adjacencyMatrix, max_line_width=np.infty))

qw = QuantumWalk(g, eff_res(2)/2, eff_res(2)/2)
print(np.array2string(qw.modifiedAdjacencyMatrix, max_line_width= np.infty))
print(np.array2string(np.round(qw.quantumWalkOperator, 3), max_line_width=np.infty))
print(sp.linalg.eigvals(qw.quantumWalkOperator))


#phase_gaps = []
#num_qubits = []
#for i in range(2, 3):
    #print("{}%".format(i))
 #   psi_s = np.zeros((2*i+1, 1))
  #  psi_s[0] = 1
   # redg = GluedTree(i, {0}, {2*(2**i-1)-1})
    #qw = QuantumWalk(redg, eff_res(i)/2., eff_res(i)/2.)
    #eigvals, eigvects = np.linalg.eig(qw.quantumWalkOperator)
    #phases = np.imag(np.log(eigvals))
    #print(phases)
    #phase_gap = nsmallest(2, np.abs(phases))[1]
    #print(phase_gap)
    #NOTE: This estimation of overlap seems to be FAULTY!!!!!
    #np.absolute(eigvects[list(phases).index(phase_gap)].dot(psi_s)))
    #phase_gaps.append(phase_gap)
    #num_qubits.append(2*i)
#plt.plot(num_qubits, phase_gaps)
#plt.title("Phase gap vs. number of edges")
#plt.ylabel("Phase gap of quantum walk operator")
#plt.xlabel("Number of edges")
#plt.show()

#g = GluedTree(2)
#print(g.adjacencyMatrix)
#qw = QuantumWalk(g)
#print(qw.quantumWalkOperator)
#print("\n")
