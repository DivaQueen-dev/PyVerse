'''
class student:
    "This is student class with required data"
print(student.__doc__)
help(student)
'''
'''
class student:
        """class demo on student class"""
        def __init__(self):
            self.name=input("Enter name")
            self.age=int(input("Enter age"))
            self.nombre=input("Enter other name")
        def talk(self):
            print("hola yo soy :" , self.name)
            print("mi age es :",self.age)
            print("¿Come te lamas?",self.nombre)
s=student()
s.talk()
'''
class Test:
    def __init__(self):
        print("constructor")
    def m1(self):
        print("Method execution")
t1=Test()
t2=Test()
t3=Test()
t1.m1()
