def soccer():
  N = int(input())
  if N<4:
    print(0)
  elif N==4:
    print(1)
  else:
    a = (N-1)*(N-2)*(N-3)
    print(a//6)

soccer()
