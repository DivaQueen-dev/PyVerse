class test:
    x =10
    def __init__(self):
        self.y = 20
t1 = test()
t2 = test()
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)
test.x = 888
t1.y  = 999
print("t1:",t1.x,t1.y)
print("t2:",t2.x,t2.y)


def student:
    college_name = "Aditya College"
    def __init__(self):
        student.college_name = "Aditya Engineering college"
    def show_details(self):
        print("Accessed ")
