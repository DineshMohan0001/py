import re
# TESTER = re.compile(
#     r"^"
#     r"(?!.*(\d)(-?\1){3})"
#     r"[456]\d{3}"
#     r"(\d{12}|(-\d{4}){3})"
#     r"$")
# for _ in range(int(input().strip())):
#     print("Valid" if TESTER.search(input().strip()) else "Invalid")




data = re.compile(r"(?!.*(\d)(-?\1){3})")
matche = data.finditer(input())
for m in matche:
    print(m)




pattern = re.compile(r"^t" r"\.com" )
match = pattern.finditer(string="ti 33.33 .com")
for x in match:
    print(x)




p = re.compile(r'\d')
mat = p.finditer(string="1234hi45")
for x in mat:
    print(x)




