import sys
input=sys.stdin.readline
n_sensors = int(input())
#sensor = {}
list1 = [0]*1001
list2 = [0]*1001
for i in range(n_sensors):
    a = int(input())
    list1[a] += 1
    list2[a] += 1

list2.sort()
mx = list2[-1]
sx = list2[-2]

mlist = []
slist = []

for i in range(1001):
    if list1[i] == mx:
        mlist.append(i)
    if list1[i] == sx:
        slist.append(i)

mlist.sort()
slist.sort()
if len(mlist) > 1:
    print(abs(mlist[-1] - mlist[0]))
else:
    m1 = abs(mlist[0] - slist[0])
    m2 = abs(mlist[0] - slist[-1])
    print(max(m1,m2))
