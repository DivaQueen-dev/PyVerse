s = {10.2,30,45,3,"yooooo"}
print(s)
print(type(s))
s = {10}
print(s)
print(type(s)) #dict
s.add(20)
print(s)
s = {10,20,30,40}
l = [220,60,90,11.422222,122,"dd"]
s.update(l,range(5)) #order vary in set ==> and doesnt accept duplicates
print(s)
d = set('apple')
print(d)
s1 = s.copy()
print(s1)
s= {40,10,30,20}
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
s = {40,30,20,10}
s.remove(30)
print(s)

s = {10,20,30}
s.discard(10)
print(s)
s.discard(50)
print(s)
s = {10,20,30}
print(s)
s.clear()
print(s)
#Mathematical operations on set
x = {10,20,30,40,50}
y = {20,10,44,60,50}

print(x.union(y))
print(x|y)
x= {10,3.4,'fff'}
y = {10,'fff',333333,'ff'}
print(x.intersection(y))
print(x&y)
print(x.difference(y))
print(x-y)
print(y-x)
x = {10,20,30,40}
y = {30,40,50,60}
print(x.symmetric_difference(y))
print(x^y)




