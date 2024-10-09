class overloading:
    def sum(self,a,b,c):
        return a+b+c 
    def sum(self,a,b):
        return a+b
    
ob=overloading()
print(ob.sum(1,2,3))