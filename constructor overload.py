class student:
    def __init__(self, name = None, age = None):
        if name and age:
            print(f"Name :{name}, Age: {age}")
        elif name:
            print(f"Name:{name}")
        else:
            print("No details")
s1 = student()
s2 = student('ravi')
s3  = student("Anil", 20)
