n,m=map(int,input().split())
l1=[list(map(int,input().split())) for _ in range(n)]
l2=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if l1[i][j]==l2[i][j]:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()