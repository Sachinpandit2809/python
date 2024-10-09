class parents:
    attribute=0
    def __init__(self) :
        print("parent")
        
class child(parents) :
    def __init__(self):
        super().__init__()
        print(self.attribute)

ob=child()
