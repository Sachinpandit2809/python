class rectangle:
    def sides(self,height ,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
    def parameter(self):
        return 2*(self.height+self.width)
   
ob=rectangle()
ob.sides(10,20) 
print(ob.area())
print(ob.parameter())