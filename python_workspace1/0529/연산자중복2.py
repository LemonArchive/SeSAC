class MyList:
    def __init__(self,data):
        self.data = list(data)

    def __str__(self):
        return f"MyList({self.data})"
    
    m1 = MyList((1,2,3,4,5,6))
    print(m1)