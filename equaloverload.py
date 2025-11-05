class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll= roll
    def __eq__(self,other):
        return self.roll == other.roll
s1 =student("Anil" , 101)
s2  =student("Ravi",102)
print(s1==s2)
