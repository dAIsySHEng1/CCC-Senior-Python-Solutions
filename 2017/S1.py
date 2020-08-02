def basket():
    N = int(input())
    swift = input().split()
    sema = input().split()
    sw = [int(swift[0])]
    se = [int(sema[0])]
    for i in range(N-1):
      sw.append(0)
      se.append(0)
    for i in range(1,N):
        sw[i]=sw[i-1]+int(swift[i])
        se[i]=se[i-1]+int(sema[i])
    for i in range(N-1,-1,-1):
        if se[i]==sw[i]:
            return i+1
    return 0

print(basket())
