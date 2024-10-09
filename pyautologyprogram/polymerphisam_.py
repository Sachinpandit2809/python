class animal:
    def speak(self):
        pass
class dog(animal):
    def speak(self):
        print('bark')
class cow(animal):
    def speak(self):
        print('moo0')
class cat(animal):
    def speak(self):
        print('meaw')
        
ob1=cat()
ob2=cow()
ob3=dog()
ob1.speak()
ob2.speak()
ob3.speak()