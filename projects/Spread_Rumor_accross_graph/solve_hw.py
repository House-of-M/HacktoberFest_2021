import sys
from collections import deque



"""
Prends comme inputs:
		-adj: liste d'adjacence du graphe dirigé décrivant la dynamique de dispersion des rumeurs
	output:
		-nombre solution du problème pour la dynamique donnée par adj
"""

def solve(adj):
    list_scc=kosaraju(adj) #retourne une liste de taille n (n le nombre de noeuds) ou iste_scc[i] = j signifie que i appartient a la scc numéro j
    sol=SCC_to_min_kot(list_scc,adj) #utilise la liste de scc pour trouver le nombre min de kots
    return sol


def kosaraju(adj): #DIRECT APPLICATION OF THE KOSARAJU ALGORITHM (IN ITERATIVE FORM)

    # postorder DFS on G to transpose the graph and push root vertices to L
    N = len(adj)
    T= [[] for _ in range(N)]
    L= []
    U= [False] * N
    for u in range(N):
        if not U[u]:
            U[u], S = True, [u]
            while S:
                u, done = S[-1], True
                for v in adj[u]:
                    T[v].append(u)
                    if not U[v]:
                        U[v], done = True, False
                        S.append(v)
                        break
                if done:
                    S.pop()
                    L.append(u)

    # postorder DFS on T to pop root vertices from L and mark SCCs
    sol = [None] * N
    while L:
        r = L.pop()
        S = [r]
        if U[r]:
            U[r], sol[r] = False, r
        while S:
            u, done = S[-1], True
            for v in T[u]:
                if U[v]:
                    U[v] = done = False
                    S.append(v)
                    sol[v] = r
                    break
            if done:
                S.pop()
    return sol

def SCC_to_min_kot(sol,adj):
    unique= len(set(sol)) # number of scc in graph
    tmp = [0 for _ in range(max(sol)+1)]  #tmp is used to keep track of the SCC which have an incoming node

    for i in range(len(adj)): #we loop over the edges knowing it starts from node i
        for x in adj[i]: #This means that there is an edge from i to x
            if (sol[x] != sol[i]): #If they are not in the same SCC
                tmp[sol[x]]=1
    return(unique-sum(tmp)) #(nb min kot) = (nb SCC) - (nbr SCC which have incoming edge)


"""
    codes pour les tests
"""

def read_and_solve_tests(input_file, output_file):
    f_in = open(input_file, "r")   #OPEN INPUT FILE TO READ DATA
    f_out = open(output_file, "w") #OPEN OUTPUT FILE TO WRITE RESULT

    nProb = int(f_in.readline()) #READS FIRST LINE OF THE FILE AKA THE NUMBER OF INPUTS K
    for p in range(nProb): # LOOP OVER K THE NUMBER OF INPUTS
        adj = load_graph(f_in) #CALL FUNCTION FOR
        f_out.write(str(solve(adj))+"\n") # WRITE SOLUTION FOR Ième INPUT
    f_in.close() #CLOSE FILE
    f_out.close() #CLOSE FILE

def load_num(f_in):
    num_str = f_in.readline() #READ LINE FROM FILE

    return list(map(int, num_str.split())) #EXTRACT ELEMENT OF THE LINE, TRANSFORM THEM TO INT, PUT THEM IN LIST

def load_graph(f_in):
    N,E = load_num(f_in) #N NUMBER OF KOTS AND E NUMBER OF LINES

    # Load each edge an construct adjcency  list
    adj = [list() for v in range(N)] #CREATE LIST OF N LISTS

    for i in range(E): #ITERATING OVER E LINES OF SAMPLE
        x,y = load_num(f_in) #EXTRACTING NUMBERS OF LINE
        adj[x-1].append(y-1) # ADDING Y AS NEIGHBOR OF KOT X IN ADJ LIST

    return adj


if __name__ == '__main__':


    exit(0)
