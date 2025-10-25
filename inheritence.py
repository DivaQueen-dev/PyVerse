'''
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def bark(self):
        print("Bark")
d=Dog()
d.sound()
d.bark()
'''
class A:
    def methodA(self):
        print("Method A")
class B:
    def methosB(self):
        print("Method B")
class C(A,B):
    pass
c=C()
c.methodA()
c.methodB()
