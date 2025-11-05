#iterative
n = int(input("enter number:"))
for x in range(1,n+1):
    if x%2==0:
        print(x)
for y in range(10,0,-1):
    if y%2==0:
        print(y)
s = input("enter string:")
for ch in s:
    print(ch,end='')
print()
for i in range(1,5):
    for j in range(1,5):
        print(j,end=" ")
    print()
n = int(input("enter number of rows:"))
for i in range(1,n+1):
    print("*" *i)

        
    
