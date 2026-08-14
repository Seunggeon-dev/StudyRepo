n=int(input())
l=[[0 for _ in range(n)]for _ in range(n)]

for i in range(n):
    if i%2==0:
        cnt=1
    else:
        cnt=n
    for j in range(n):
        l[j][i]=cnt
        if i%2==0:
            cnt+=1
        else:
            cnt-=1
for rows in l:
    for e in rows:
        print(e,end='')
    print()