n=int(input())
l=list(map(int,input().split()))

print(*[i**2 for i in l])