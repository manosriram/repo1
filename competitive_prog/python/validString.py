res1 = []
res2 = []
count=0
inp = str(input())

res = list(set(inp))

for t in range(0,len(res)):
    res1.append(inp.count(res[t]))

res2 = list(set(res1))

if len(res2)==2:
    if res1.count(res2[0])==1 or res1.count(res2[1])==1:
        print("YES")

    if res1.count(res2[0])>1 and res1.count(res2[1])>1:    
        print("NO")

if len(res2)==1:
    print("YES") 

if len(res2)>2:
    print("NO")
