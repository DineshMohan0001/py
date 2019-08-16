class Inheritance:
    def rectangle(self,Name,age):
        self.__Name=Name
        self.__age=age
    def get(self):
        return self.__Name
    def getage(self):
        return self.__age
class square(Inheritance):
    def cal(self):
        return self.get()
        return self.getage()
s=square()
s.rectangle('dinesh',21)
print(s.cal())



class data:
    a=10
    b=20
    c=30
class sum(data):
    def sum(self,):
        print(self.a+self.b+self.c)
s=sum()
