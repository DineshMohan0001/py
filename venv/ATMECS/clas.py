class rectangle:
    def __init__(self,length,breath):
        #print(length*breath)
        self.__length=length

        self.__breath=breath
    def get(self):
        return self.__length
    def set(self):
        return self.__breath
    def print(self):
        print(self.__length*self.__breath)


ford=rectangle(20,23)
ford.print()
audi=rectangle(20,20)
ford=rectangle(10,10)
ford.print()
# print(ford.__length,ford.__breath)
# print(ford.__length*ford.__breath)
