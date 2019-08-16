class mul_inheri:
    def shape():
        print("SHAPE")
        #return shape
class size:
    def size():
        print("SIZE")

class total(mul_inheri,size):
    def total(self):
        print("adaf")
        total.shape()
       # self.shape()
        size.size()
t = total()
t.total();
#total()
# t.size()
# t.shape()