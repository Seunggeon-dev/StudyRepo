s=list(map(int,input().split()))+[0 for _ in range(8)]

for i in range(2,10):
    s[i]=(s[i-2]+s[i-1])%10
print(*s)