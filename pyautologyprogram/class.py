class student:
    def set_name(self,name):
        self.name=name
        
    def get_name(self):
        return self.name
    
s1 = student()
s1.set_name("sachin")
print(s1.get_name())