#print(classname.__doc__)
#help(classname)
class student:
    '''This is student class with required data'''
    def __init__(self):
        self.name = 'sandhya'
        self.age = 27
        self.marks = 85
    def talk(self):
        print("Hello I am: ",self.name)
        print("My age is  :",self.age)
        print("My marks are :",self.marks)
print(student.__doc__)
s = student()
s.talk()
