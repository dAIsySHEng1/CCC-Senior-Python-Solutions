def tides():
    N = int(input())
    s = input().split()
    x = []
    for i in s:
        x.append(int(i))
    x.sort()
    ans = []
    if N%2 ==0:
        n = N//2
        low = x[:n]
        low.reverse()
        high = x[n:]
        i = 0
        while i<=n-1:
            ans.append(low[i])
            ans.append(high[i])
            i+=1
    else:
        n = N//2 + 1
        low = x[:n]
        low.reverse()
        high = x[n:]
        i = 0
        while i <= n-2:
            ans.append(low[i])
            ans.append(high[i])
            i += 1
        ans.append(low[-1])

    for x in ans:
        print(x, end=' ')

tides()
