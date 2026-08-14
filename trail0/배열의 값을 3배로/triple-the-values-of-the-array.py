l=[list(map(int,input().split())) for _ in range(3)]
l3=[[element*3 for element in row] for row in l]
for row in l3:
    print(*row)