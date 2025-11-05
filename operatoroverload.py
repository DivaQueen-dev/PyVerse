
#__add__(), __sub__() using these methods we perform operator overloading
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return point(self.x+other.x, self.y+other.y)
    def __str__(self):
        return f'({self.x},{self.y})'
p1 = point(1,2)
p2  = point(3,4)
p3 = point(0,0)
p3 = p1+p2
print(p3)
    
