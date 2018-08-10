a = []
n,r = map(int,input().split())

for t in range(n):
    a = list(map(int, input().split()))


for t1 in range(0,r):
    for t2 in range(1,n+1):
        a[t2] = a[t2-1] | a[t2]

for t in a:
    print(t)
