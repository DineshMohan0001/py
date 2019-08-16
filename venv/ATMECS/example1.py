import re
# import data
# with open ('data.txt','r') as f:
#     c=f.read()
#     print(c)


f=open('data.txt')
g=f.read()
# pattern = re.compile(r'[a-zA-Z0-9]')
# match = pattern.finditer(c)
# for x in match:
#     print (x)


#
# pattern = re.compile(r'\D')
# match = pattern.finditer(str(input()))
# for x in match:
#     print(x)
#
#
#
# c=re.compile(r'[^cb]at')
# ma = c.finditer(g)
# for x in ma:
#     print(x)
#
#
#
#
s= re.compile(r'[a-zA-Z0-9.]+@(gmail|yahoo)\.(com|edu)')
r = s.finditer(g)
for x in r:
     print(x)

#
# s = re.compile(r'[a-zA-Z0-9.]+@(gmail|yahoo)\.(com|edu)')
# r = s.finditer(g)
# for x in r:
#     print(x.group(0))


pattern = re.compile(r'\d\d\d(\*|-)+\d\d\d(\ *|-)+\d\d\d')
match = pattern.finditer(g)
for x in match:
    print(x)