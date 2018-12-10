probA = {1: 0.8, 0: 0.2}
probBA = {(1, 0): 0.8, (0,0): 0.2, (1, 1): 0.1, (1, 0): 0.9}
probC = {1: 0.9, 0: 0.1}
probDBC = {(1, 0, 0): 0.1, (0, 0, 0): 0.9, (1, 0, 1): 0.5, (0, 0, 1): 0.5, (1, 1, 0): 0.15, (0, 1, 0): 0.85, (1, 1, 1): 0.9, (0, 1, 1): 0.1}
probEC = {(1, 0): 0.8, (0, 0): 0.2, (1, 1): 0.5, (0, 1): 0.5}
probFD = {(1, 0): 0.9, (0, 0): 0.1, (1, 1): 0.45, (0, 1): 0.55}
probGD = {(1, 0): 0.9, (0, 0): 0.1, (1, 1): 0.75, (0, 1): 0.25}
probH = {1: 0.15, 0: 0.75}
probIF = {(1, 0): 0.75, (0, 0): 0.25, (1, 1): 0.45, (0, 1): 0.55}
probJEG = {(1, 0, 0): 0.25, (0, 0, 0): 0.75, (1, 0, 1): 0.25, (0, 0, 1): 0.85, (1, 1, 0): 0.25, (0, 1, 0): 0.75, (1, 1, 1): 0.15, (0, 1, 1): 0.85}
probKHI = {(1, 0, 0): 0.25, (0, 0, 0): 0.75, (1, 0, 1): 0.15, (0, 0, 1): 0.85, (1, 1, 0): 0.5, (0, 1, 0): 0.5, (1, 1, 1): 0.75, (0, 1, 1): 0.25}
probLJ = {(1, 0): 0.15, (0, 0): 0.85, (1, 1): 0.25, (1, 0): 0.75}

prob = {'A': probA, 'BA': probBA, 'C': probC, 'DBC': probDBC, 'EC': probEC, 'FD': probFD, 'GD': probGD, 'H': probH, 'IF': probIF, 'JEG': probJEG, 'KHI': probKHI, 'LJ': probLJ}

graph = [(1, 'DCB', 'AB'), (1, 'DGE', 'DF'), (1, 'IF', 'DF'), (1, 'IHK', 'IF'), (1, 'JL', 'JEG'), (2, 'DCE', 'DCB'), (2, 'DGE', 'DCE'), (2, 'JEG', 'DGE')]
V = ['AB', 'DCB', 'DGE', 'DF', 'IF', 'IHK', 'JL', 'JEG', 'DCE']

probToV = {'AB': [], 'DCB': [], 'DGE': [], 'DF': [], 'IF': [], 'IHK': [], 'JL': [], 'JEG': [], 'DCE': []}
for p in prob: 
    for v in V:
        if p[0] in v:
            probToV[v] += [p]

print probToV

result = {'AB': 1, 'DCB': 1, 'DGE': 1, 'DF': 1, 'IF': 1, 'IHK': 1, 'JL': 1, 'JEG': 1, 'DCE': 1}
for p in probToV:
    aux = 1
    for i in probToV[p]:
        for j in prob[i]:
            print j
