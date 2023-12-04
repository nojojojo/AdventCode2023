import re

with open('input.txt') as f:
    input = list(f)

ex_list = input
print(ex_list)
sol = []
n = 0

while n < len(ex_list):
    item = re.sub(r'\D', '', ex_list[n])
    item = item[0] + item[-1]
    sol.append(int(item))
    n = n+1

total = sum(sol)
print(total)
print(sol)
print(len(ex_list))