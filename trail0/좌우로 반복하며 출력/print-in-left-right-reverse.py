n=int(input())
l=[]
for i in range(1,n+1):
    row=[]
    for j in range(1,n+1):
        row.append(j)
    if i%2==0:
        row.reverse()
    l.append(row)
for row in l:
    for e in row:
        print(e,end='')
    print()
