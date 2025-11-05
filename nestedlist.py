n= [[10,20,30] , [40,50,60],[70,80,90]]
print(n)
print("Elements by Row wise:")
for r in n:
    r.reverse()
    print(r)
print("Element by Matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])-1,-1,-1):
        print(n[i][j] ,end=' ' )
    print()
a =[10,20,'a']
print(a)
