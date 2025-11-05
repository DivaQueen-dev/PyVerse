import time
class Test:
    def __init__(self):
        print("Object initialization")
    def __del__(self):
        print("Fulfilling Last wish and performing cleanup activities...")
t1 = Test()
t1 = None

        
