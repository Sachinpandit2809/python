class constructor:
    def __init__(self,h,w):
        self.h=h
        self.w=w
    def area(self):
        return self.h*self.w
    def parameter(self):
        return 2*(self.h+self.w)
   
ob=constructor(1,2)
a=10
print( ob.area())
print(ob.parameter())
