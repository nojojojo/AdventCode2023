import re

input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

def split(s):
    return s.split('\n') 

ex_list = split(input)
print(ex_list)
sol = []
n = 0


while n < len(ex_list):
    item = re.sub(r'\D', '', ex_list[n])
    if int(item) > 2:
        item = item[0] + item[-1]
    sol.append(int(item))
    n = n+1


total = sum(sol)
print(sol)
print(total)