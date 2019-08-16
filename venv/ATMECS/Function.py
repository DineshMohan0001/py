def sum(a,b):
    if(type(a)!=type(b)):
        return "ERROR"
    return(a+b)
def student(a='UNKNOWN',b='UNKNOWN'):
    print( " Name : ",a, "\n" ,"AGE : ",b)

print(sum(10,9))
a=sum('dinesh','mohan')
print(a)
print(sum(12,'dine'))
student('Dinesh',21)
student()