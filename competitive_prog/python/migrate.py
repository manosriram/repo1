b = []
arr = []
n = int(input())

arr=list(map(int,input().split()))

for t in range(len(arr)-1):
    b.append(arr.count(arr[t]))

c = max(b)

for t in range(len(b)-1):
    if b[t] == c:
        print(arr[t])
        break
    