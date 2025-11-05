n = [1,2,3,4,5]
n.insert(3,12)
n.insert(-1,24)
n.insert(-2,22)
n.insert(-5,21)
print(n)
order1 = ["chicken" , "mutton", "prawns"]
order2= ["gulabjamun", "kheer", "rasmalai"]
order1.extend(order2)
print(order1)
order1.extend("Mushroom")
print(order1)
n = [10,20,10,30]
n.remove(10)
print(n)
print(n.pop())
print(n.pop())
print(n)
n = [10,20,30,40,50,60]
print(n.pop())
print(n.pop(1))
#print(n.pop(10)) #index

n = [10,20,30,40]
n.reverse()
print(n)

n = [50,30,20,40]
n.sort()
print(n)
s = ["Dog" , "Banana", "cat", "Apple" ]
s.sort(reverse=True)
s.sort(reverse=False)
print(s)
c = [10,20,30,40,50]
b = [60,70,80,90,100]
d=c+b
print(d)
x = [10,20,30]
y = x*3 #repetition operator
print(y)
x = ["Dog", "Cat", "Rat"]
y = ["Dog", "Cat", "Rat"]
z = ["DOG","CAT", "RAT"]
print(x==y)
print(y==x)
print(x==z)
print("Dog" in x)
print("Rabbit" in x)
x.clear()
print(x)




