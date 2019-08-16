f = open('data.txt')
g = f.read()
print(g)
f.close()
print("------------------****************-------------------")
with open('data.txt','r') as d:
    v = d.read()
    print(v)
    print(d.mode)
    #d.close()
    content = d.readlines()
    print(content)

with open('data.txt','r') as d:
    content = d.readline()
    print(content)
    a=1
    for line in d:
        print(a,") ",end="")

        print(line)
        a+=1

