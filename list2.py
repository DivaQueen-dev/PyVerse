n = [10,20,30,40]
print(n)
n[1] = 333
print(n)
n = [1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print (n[8:2:-2])
print(n[4:100])
n = [0,1,2,3,4,5,6,7,8,9,10]
i = 0
while i<len(n):
    print(n[i])
    i = i+1
n = [0,1,2,3,4,5,6,7,8,9,10]
print("")
for n1 in n:
    print(n1)
print("")
n = [1,2,2,2,2,3,3]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))
print("")
print(n.index(1))
print(n.index(2))
print(n.index(3))
if 4 in n:
    print(n.index(4))
else:
    print("4 is not present in the list")
    



