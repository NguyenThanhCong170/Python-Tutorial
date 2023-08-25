number = [1,23,23,232,32,32,32,32,32,32,32,32,32,32]
abc = []
for x in number:
    if x not in abc:
        abc.append(x)
print(abc)
