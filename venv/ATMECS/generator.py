def cal():
    n=2
    yield n
    n+=1
    yield n
    n+=1
    yield n
class myclass:
    def hi():
        n=2
        return n
        print("hi")


m=myclass
x=cal()
print(m.hi())
print(next(x))
print(next  (x))
print(next(x))