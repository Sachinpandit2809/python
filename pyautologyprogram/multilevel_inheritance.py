class grandfather:
    def gf(self):
        print("gf")
class father():
    def f(self):
        print("f")
class son(father,grandfather):
    def s(self):
        print("s")
ob=son()
ob.s()
ob.f()
ob.gf()
        