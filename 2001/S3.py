paths = []
graph= []

for i in range(26):
    graph.append([])

while True:
  road = input()
  if road == '**':
    break
  c1 = ord(road[0])-65
  c2 = ord(road[1])-65
  graph[c1].append(c2)
  graph[c2].append(c1)
  paths.append(road)
#print(graph)
ans = []
for i in range(len(paths)):
  queue = [0] #A
  visited = [False] * 26
  visited[0] = True
  found = False #finding B
  curr = paths[i]
  while len(queue)>0 and not found:
    c = queue.pop(0)
    for j in graph[c]:
      #if not visited[j] and c+j!=curr and j+c!= curr:
      if visited[j]==False and chr(c+65)+chr(j+65)!=curr and chr(j+65)+chr(c+65) != curr:
        queue.append(j)
        visited[j] = True
        if chr(j+65)=='B':
          found = True
          break
  if not found:
    ans.append(curr)
for i in ans:
  print(i)
print("There are",len(ans),"disconnecting roads.")
