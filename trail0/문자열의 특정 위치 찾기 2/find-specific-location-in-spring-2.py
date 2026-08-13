s=["apple", "banana", "grape", "blueberry", "orange"]
n=input()
t=0
for i in s:
    if i[2]==n or i[3]==n:
        print(i)
        t+=1
print(t)
