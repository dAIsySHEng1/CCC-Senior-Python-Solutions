N = int(input())

def enumerate(string):
    global nodes
    encountered_strings = []
    result = []
    for i in string:
        if i in encountered_strings:  # check if you already seen this string
            result.append(encountered_strings.index(i))
        else:
            encountered_strings.append(i)
            result.append(encountered_strings.index(i))
    nodes = len(encountered_strings)
    return result

#bfs to find number of layers
def levels(graph, V, src):
    # array to store level of each node
    level = [None] * V  # V - number of vertices
    visited = [False] * V

    queue=[]
    queue.append(src)
    level[src] = 0
    visited[src] = True

    while len(queue)>0:
        curnode = queue[0]
        queue.remove(curnode)
        # traverse neighbors of node x
        for i in range(len(graph[curnode])):
            # b is neighbor of node x
            b = i
            # if b is not marked already
            if (not visited[b]) and graph[curnode][i]==1:
                queue.append(b)
                # level of b is level of x + 1
                level[b] = level[curnode] + 1
                # mark b
                visited[b] = True
    return max(level)

for k in range(N):
    L = int(input())
    ppl = []
    for i in range(L):
        ppl.append(input())
    ppl.reverse()
    nodes = 0
    ppl = enumerate(ppl)

    ppl = ppl+[0]

    graph=[]
    for i in range(nodes):
        cur = []
        for j in range(nodes):
            cur.append(0)
        graph.append(cur) #connectivity
    old = 0
    for i in range(len(ppl)-1):
        graph[ppl[i]][ppl[i+1]] = 1
        old += 1
    #print(graph,old)
    new = levels(graph,nodes,0)*20
    print(old*10-new)
