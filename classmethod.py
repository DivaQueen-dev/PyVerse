'''class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noOfObjects(cls):
        print('the no.of objects created for test class:',cls.count)
t1=Test()
t2=Test()
Test.noOfObjects()
t3=Test()
t4=Test()
t5=Test()
Test.noOfObjects()'''
class ADITYA:
    @staticmethod
    def add(x,y):
        print("The Sum Value is:",(x+y))
    @staticmethod
    def sub(x,y):
        print("The Subtraction value is:",(x-y))
    @staticmethod
    def avg(x,y):
        print("The Average Value is:",(x+y)/2)
ADITYA.add(200,100)
ADITYA.add(200,150)
ADITYA.add(100,150)
