

def parseFile():
    f = open('bn1')
    lines = f.readlines()
    vals = lines[0].replace('\n', '').split(' ')

    prob = {}
    rules = {}

    for n in range(1, int(vals[0])):
        tokens = lines[n].replace('\n', '').split(' ')
        prob[tokens[0]] = {'vars': [], 'p': []}
        index = [i for i, e in enumerate(tokens) if e == ';']
        if index:
            for i in range(index[0] + 1, index[1]):
                prob[tokens[0]]['vars'] += [tokens[i]]
        for i in range(index[1] + 1, len(tokens)):
            prob[tokens[0]]['p'] += [float(tokens[i])]
     
    #print prob

    for r in range(0, int(vals[1])):
        tokens = lines[r + int(vals[0]) + 1].replace('\n', '').split('|')
        rules[tokens[0].strip()] = tokens[1].strip()
    
    #print rules
    return prob
    
def parseFileSample():
    f = open('samples_bn1')
    var = f.readline().replace('\n', '').split(' ')
    lines = []
    for l in range(10000):
        lines += [f.readline().replace('\n', '').split(' ')]
       
    #print var
    #print lines
    return {'var': var, 'lines': lines}

def main():
    prob = parseFile()
    sample = parseFileSample()
    letters = sample['var']
    lines = sample['lines']
    
    for p in prob:
        V = p
        pa = prob[p]['vars']

        index = []
        for v in [V] + pa:
            index.append(letters.index(v))
        
        count = 0
        
        poss = []
        if len(index) == 1:
            poss = [0, 1]
        elif len(index) == 2:
            poss = [(1, 0), (1, 1)]
        elif len(index) == 3:
            poss = [(1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

        possLines = [0 * x for x in range(len(poss))]
        if len(poss) == 1:
            total = len(lines)
        else:
            total = [0 * x for x in range(len(poss))]
            if len(poss) == 2:
                t = [0, 1]
            else:
                t = [(0, 0), (0, 1), (1, 0), (1, 1)]

        for l in lines:
            aux = []
            auxTotal = []
            for i in index:
                aux += [l[i]]
            if len(aux) == 1:
                aux = int(aux[0])
            else:
                aux = tuple([int(a) for a in aux])
                auxTotal = tuple([int(a) for a in aux[1:]])
            if aux in poss:
                possLines[poss.index(aux)] += 1
            if auxTotal != []:
                if len(auxTotal) == 1:
                    total[int(auxTotal[0])] += 1
                else:
                    total[t.index(auxTotal)] += 1
            else:
                total = [len(lines) for x in range(len(poss))]

        print [V] + pa,
        for ind, pl in enumerate(possLines):
            print pl * 1.0 / total[ind], 
        print ''

main()

