d = dict()
d2 = dict()

d2['n'] = 1
d2['s'] = '?'

d[0] = d2


mark = False

for dir in d[0]:
    if d2[dir] == '?':
        print(dir)
        mark = True

print(mark)