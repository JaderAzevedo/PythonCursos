# Versão Normal

dobros = []
for i in range(10):
    dobros.append(i*2)
print(dobros)


# Versão com listcomprehension

# [expressão  for item in list]

dobros = [i*2 for i in range(10)]
print(dobros)
