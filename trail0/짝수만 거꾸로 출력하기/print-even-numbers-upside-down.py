n=int(input())
l=list(map(int,input().split()))
l=reversed(l)
for i in l:
    if i%2==0:
        print(i,end=' ')