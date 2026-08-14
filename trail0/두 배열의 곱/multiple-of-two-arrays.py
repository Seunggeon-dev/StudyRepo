l1=[list(map(int,input().split())) for _ in range(3)]
input()
l2=[list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(l1[i][j]*l2[i][j],end=' ')
    print()