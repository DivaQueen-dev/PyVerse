#dynamic,mutable,heterogeneous,indexing and slicing concepts not allowed,insertion is not preserved
d = {}
d[100] ="sundar"
d[200] = "radhaaaa"
d[300] = "shyam"
print(d)
d = {100:'sri', 200:'deep', 300:'sandy' }
print(d)
d[300] = "sandeep"
print(d)
d = {100:'rupa',200:'saraswathi',300:'rupaaaaa'}
del d[100]
print(d)
d.clear()
print(d)

del d
#print(d) error
print("-----")
d = {100:'sri', 200:'deep', 300:'sandy' }
print(d.get(100))
print(d.get(400,"guest"))

