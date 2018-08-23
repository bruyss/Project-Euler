#! python3
# What is the total of all name scores in the file?


def alph_value(s):
    a_value = 0
    for c in s:
      a_value += ord(c) - ord('A') + 1
    return a_value


assert alph_value('COLIN') == 53


file = open('22_names.txt')
names = file.read().split(',')

sorted_names = []
for name in names:
    i = 0
    name = name[1:-1]
    while i < len(sorted_names) and name > sorted_names[i]:
        i += 1
    sorted_names.insert(i, name)

answer = 0

for name in sorted_names:
    answer += alph_value(name)*(sorted_names.index(name) + 1)

print(answer)