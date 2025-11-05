class Student:
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks =z
    def display(self):
        print("student Name : {} \n rollno:{} \n marks: {} \n ".format(self.name,self.rollno,self.marks))
s1 = Student('rr',12,44)
s1.display()
#use self keyword for instance variables
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        print("Inside the constructor")
        print("Name:",self.name)
        print("Rollno:",self.rollno)
    def updated_marks(self,marks):
        self.marks = marks
        print("\n  Inside Instance method")
        print(f"{self.name}' s marks updated to :",self.marks)
s1 = Student('pani', 111)
print("\n outside the class:")
print("Name (before):", s1.name)
s1.name = "Panipuri"
print("Name(after) :",s1.name)
s1.updated_marks(100)
print("Marks(outside):",s1.marks)

#del self.var_name , del objectreference.var_name
class Employee:
    def __init__(self,name,empid):
        self.name= name
        self.empid = empid
        self.salary = 50000
        print("Inside constructor")
        print(self.__dict__)
    def remove_salary(self):
        del self.salary
        print("\n After deleting 'salary' within class:")
        print(self.__dict__)
e1 = Employee("mushroom",1001)
del e1.empid
print("\n After deleting empid from outside the class")
print(e1.__dict__)
e1.remove_salary()
e2  = Employee("paneer", 1002)
del e2.empid
print("\n After deleting empid from outside the class")
print(e2.__dict__)
#method with no para is static


 

