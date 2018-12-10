from copy import deepcopy
import networkx as nx
import kruskal

def findCommunEffect(graph):
    nodes = {}
    result = []
    for node in graph.keys():
        nodes[node] = 0
    for node in graph:
        for n in graph[node]:
            nodes[n] += 1
            if nodes[n] == 2:
                result += [n]
    return result

def findParents(graph, nodeCommun):
    parents = []
    for node in graph:
        for n in graph[node]:
            if n == nodeCommun:
                parents += [node]
    return parents

def makeGraph(graph):
    for node in graph:
        for n in graph[node]:
            if node not in graph[n]:
                graph[n] += [node]
    return graph

def minfill(oldGraph):
    result = []
    addEdge = []
    graph = deepcopy(oldGraph)
    V = graph.keys()
    for i in V:
        F = []
        adds = {}
        for u in V:
            if u in graph:
                adds[u] = []
            if u in graph and len(graph[u]) >= 2:
                for a in graph[u]:
                    for b in graph[u]:
                        if a!= b:
                            if a in graph and b not in graph[a]:
                                if u in adds:
                                    if (a, b) not in adds[u] and (b, a) not in adds[u]:
                                        adds[u] += [(a, b)]
                                else:
                                    adds[u] = [(a, b)]
        minVal = len(graph) + 1
        minNode = ''
        for add in adds:
            if len(adds[add]) < minVal:
                minVal = len(adds[add])
                minNode = add
        if minVal != 0:
            addEdge += [adds[minNode]]
        result += minNode
        graph.pop(minNode, None)
        for source in graph:
            for dest in graph[source]:
                if dest == minNode:
                    graph[source].remove(minNode)
    
    return addEdge

def moralizeGraph(graph):
    communEffectNodes = findCommunEffect(graph)
    parents = []
    for node in communEffectNodes:
        parents += [findParents(graph, node)]
    
    for parent in parents:
        graph[parent[0]] += parent[1]
            
    newGraph = makeGraph(graph)
    return newGraph
    
def findMaximalClique(graph):
    G = nx.Graph()
    E = []
    for v in graph:
        for u in graph[v]:
            E += [[u,v]]
    
    G.add_edges_from(E)
    clique = list(nx.find_cliques(G))
    return clique

def createCliqueGraph(clique):
    V = []
    E = []
    G = {}
    for c in clique:
        V += [''.join(c)]
        for cc in clique:
            if c != cc:
                edge = list(set(c) & set(cc))
                if edge != []:
                    e = ''.join(edge)
                    c = ''.join(c)
                    cc = ''.join(cc)
                    if c in G.keys() and G[c]:
                        if cc not in G[c] and c != cc:
                            G[c] += [(cc, len(e))]
                            E += [(len(e), c, cc)]
                    else:
                        G[c] = [(cc, len(e))]
                        E += [(len(e), c, cc)]
                    if cc in G.keys() and G[cc]:
                        if c not in G[cc] and c != cc:
                            G[cc] += [(c, len(e))]
                            E += [(len(e), cc, c)]
                    else:
                        G[cc] = [(c, len(e))]
                        E += [(len(e), cc, c)]
    return {'vertices': V, 'edges': set(E)}


def main():
    graph = {'A': ['B'], 'B': ['D'], 'C': ['D', 'E'], 'D': ['F', 'G'], 'E': ['J'], 'F': ['I'], 'G': ['J'], 'H': ['K'], 'I': ['K'], 'J': ['L'], 'K': [], 'L': []}

    newGraph = moralizeGraph(graph)
    addEdge = minfill(newGraph)
    for edge in addEdge:
        a = edge[0][0]
        b = edge[0][1]
        newGraph[a] += [b]
        newGraph[b] += [a]
    
    clique = findMaximalClique(newGraph)
    print clique
    print '================================'

    cliqueGraph = createCliqueGraph(clique)
    print cliqueGraph
    print '================================'

    cliqueTree = kruskal.kruskal(cliqueGraph)
    print cliqueTree
    print '================================'
    

main()
