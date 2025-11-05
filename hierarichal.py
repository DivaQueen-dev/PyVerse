class parent:
    def showA(self):
        print("A")
class child1(parent):
    def showB(self):
        print("B")
class child2(parent):
    def showC(self):
        print("c")
c = child2()
c.showA()
c.showC()
