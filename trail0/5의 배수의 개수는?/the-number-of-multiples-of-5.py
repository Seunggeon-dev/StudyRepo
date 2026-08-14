l=[list(map(int,input().split())) for _ in range(4)]
cnt=0
for rows in l:
    for e in rows:
        if e%5==0:
            cnt+=1
print(cnt)