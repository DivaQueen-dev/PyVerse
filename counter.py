'''class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.X=888
t1.y=999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)'''
class student:
    clg_name="Aditya college"
    def __init__(self):
        student.clg_name="Aditya University"
    def show_details(self):
        print("Accessed in instance method:",student.clg_name)
    @classmethod
    def change_clg_name(cls,new_name):
        cls.clg_name=new_name
        


