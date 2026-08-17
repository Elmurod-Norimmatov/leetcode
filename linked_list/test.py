t = int(input())
while t:
  n, k = map(int, input().split())
  n -= 1
  if n//2 == k:
    print(n)
  elif n//2 > k:
    print(k*2+1)
  else:
    print(2*(n-k))
  t -= 1