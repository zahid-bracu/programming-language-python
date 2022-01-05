class parent:
    def __init__(self,name):
        self.name=name
        print(name)
        
    def printCheck(self,value):
        self.value=value
        print("This is "+value)