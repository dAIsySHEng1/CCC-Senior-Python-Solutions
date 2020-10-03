N = int(input())
count_t=0
count_s=0
for i in range(N):
    l = input()
    count_s+= l.count('s')+l.count('S')
    count_t+= l.count('t')+l.count('T')

if count_s>count_t or count_s==count_t:
    print('French')
else:
    print('English')
