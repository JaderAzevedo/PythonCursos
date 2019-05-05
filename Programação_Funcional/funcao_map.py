a = [1, 2, 3]


# ________________________________________________________________
# Programação procedural
# a2 = []
# for i in a:
#     a2.append(i*2)
# print(a2)
print(
    '-----------------------------------------------------------')

# ________________________________________________________________
# Programação funcional utilizando map

m = list(map(lambda i: i*2, a))
print(m)

t = tuple(map(lambda i: i**3, a))
print(t)

print(a)
