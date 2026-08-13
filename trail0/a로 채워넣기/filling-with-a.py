a=input()
al=list(a)
al[1]=al[-2]='a'
print(''.join(al))