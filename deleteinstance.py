class Employee:
    def __init__(self,empid,name):
        self.name=name
        self.empid=empid
        self.salary=50000
        print("inside constructor")
        print(self.__dict__)
    def remove_salary(self):
        del self.salary
        print("\n After Deleting 'slary within class:")
        print(self.__dict__)
e1=Employee("Anil Kumar",10001)
del e1.empid
print("\n After deleting 'emp_id' from outside the class:")
print(e1.__dict__)
e1.remove_salary()
e2=Employee("Aloha",30039)
del e2.empid
print("\n After deleting 'emp_id-2' from outside the class:")
print(e2.__dict__)
