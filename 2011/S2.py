num = int(input())
s_lst = []
for i in range(num):
    a = input()
    s_lst.append(a)
c_lst = []
for i in range(num):
    b = input()
    c_lst.append(b)
counter = 0
for i in range(num):
    if s_lst[i]==c_lst[i]:
        counter+=1
print(counter)
