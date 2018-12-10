graph = {'A': set(['C']),
         'B': set(['C', 'D']),
         'C': set(['A', 'B', 'D', 'E']),
         'D': set(['B', 'C']),
         'E': set(['C'])}
arce = {'A': ['C'], 'B': ['C', 'D'], 'C': ['E', 'D'], 'D': [], 'E': []}


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def path_type(path):
    order = {}
    for p in path:
        order[p] = []
    for p in path:
        for q in path:
            if p in arce[q]:
                if p not in order[q]:
                    order[q] += [p]
            elif q in arce[p]:
                if q not in order[p]:
                    order[p] += [q]
    return order

def rule_efect_comun(order):
    values = order.values()
    result = []
    for v in values:
        for x in v:
            if x in result:
                #print("Efect comun")
                return True
            else:
                result.append(x)
    return False

def rule_cauza_comuna(order, Z):
    values = order.values()
    for v in values:
        if len(v) == 2:
            #print("Cauza comuna")
            for v1 in v:
                if v1 in Z:
                    return True
    return False
        

def rule_cauzalitate(order, Z):
    for k in order.keys():
        values = order[k]
        if values != []:
            for v in values:
                if v in Z:
                    return True
    return False


def main():
    # test 1
    X = ['A', 'B']
    Y = ['E']
    Z = []

    #test 2 
    X = ['A', 'B']
    Y = ['E']
    Z = ['C']

    #test 3
    #X = ['E']
    #Y = ['D']
    #Z = []

    #test 4
    #X = ['E']
    #Y = ['D']
    #Z = ['B']

    #test 5
    #X = ['A']
    #Y = ['B']
    #Z = []

    result = []
    path = []
    for x in X:
        for y in Y:
            path.append(list(dfs_paths(graph, x, y)))
    for p in path:
        order = path_type(p[0])
        r1 = rule_efect_comun(order)
        r2 = rule_cauza_comuna(order, Z)
        r3 = rule_cauzalitate(order, Z)
        #print(r1, r2, r3)
        if r1 or r2 or r3 == True:
            result.append(False)
        else:
            result.append(True)
    #print(result)
    if True in result:
        return False
    else:
        return True

print(main())
