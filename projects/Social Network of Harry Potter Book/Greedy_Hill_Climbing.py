import numpy as np
import pandas as pd


# TRANSFORM CSV FILE BACK INTO ADJ_MATRIX
def get_matrix_from_csv(path): # ++
    df=pd.read_csv(path)
    characters=df.columns.values.tolist()
    df=df.iloc[:,1:]
    adj_matrix=df.to_numpy()
    return adj_matrix,characters
#BUILD LIST OF VERTICES
def vertices(G): # ++
    #number of lines = number of nodes
    return [i for i in range(120)]
#GENERATE RANDOM PROBABILITY DISTRIBUTIONS FOR ICM
def generate_X(G): # ++
    print("generate large number of realisations X of the ICM on G")
    nb_edges=len(G.flatten())
    k_realisations=100 #Hyper parameter: number of simulations of the ICM
    X=[]
    Px=np.random.dirichlet(np.ones(k_realisations),size=1)  #random distriction of P(X)
    for i in range(k_realisations):
        rand=np.random.dirichlet(np.ones(nb_edges),size=1) #create a proba distribution over edges
        X.append(rand[0]) #add the realisation to the list of ICM simulations
    print(X[0])
    return Px[0],X

def best_node(G,A,V,X_list,Px):
    print("find v in V sans A that maximizes sum( P(Xi) * sigma(A U {v})")
    V_list=list(set(V)-set(A)) #element remaining
    results=0
    max=0
    for v in V_list: #for remaining vertices in V - A
        sum = 0
        for i,x in enumerate(X_list): # sum over all realisations X
            p=Px[i] #retrive probability P(Xi)
            sum=sum + ( p* influence_x(G,A,x,v)) #compute value
        if sum>results:
            results=sum
            max=v

    return max #return the best

def influence_x(G,A,x,v=None): # the influence of A unfer realization X
    temp_A=A.copy()
    if(v != None):
        temp_A.append(v)
    G=ICM(G,x) #activate and desactivate edges according to flip coin event
    nb_active=0
    for node in temp_A:
        nb_active=nb_active+ (G.sum(axis=0))[node]  #number of vertices reached by "node" through an active edge
    return nb_active

def ICM(G,x): #percolation of the graph based on X realisation
    icm=G.copy()
    cpt=0
    for i in range(120):
        for j in range(120):
            cpt=cpt+1
            if(np.random.random() > x[cpt] ):#x[cpt]): FIX THIS LATER
                icm[i,j]=1
            else:
                icm[i,j]=0
    #for i,element in enumerate(icm.flatten()):
     #   icm[i]= 1 if np.random.random() < x[i] else 0
        #flipping biased coin with proba x from ICM distribution
    return icm


def greedy_hill_climbing(G): #apply greedy algorithm on a graph G with set size k
    k=6 #5% of nodes
    Px,X_list = generate_X(G)

    V=vertices(G) #V holds the vertices of the graph
    A=[]
    for i in range(k):
        v= best_node(G,A,V,X_list,Px)
        A.append(v)
        print(f"A gets node {v}")

    return A


G,characters= get_matrix_from_csv(r'D:\SINF2M\LINMA-2472\adjacency_matrix.csv')
#print(vertices(G))
Px, X_list = generate_X(G)
#print(f"proba of {len(Px)} sums to {Px.sum()}")
#for x in X_list:
#    print(f"proba of {len(x)} sums to {sum(x)}")

#print(X_list[3])
#print(np.random.random())
A=greedy_hill_climbing(G)
print("done")
print(len(set(A)))
print(set(A))
for i in set(A):
    print(characters[i+1])

print(influence_x(G,set(A),X_list[3]))