from random import randint
a = []
b = []
for i in range(10):
    a.append(randint(1, 20))
for i in range(10):
    b.append(randint(1, 15))
print(a)
print(b)
c = [i for i in a if i in b]
d = [i for i in a if i not in b]
e = [i for i in b if i not in a]
f = [i for i in a + b if i not in a or i not in b]
print(f'входят в оба {c}')
print(f'входят только в первый {d}')
print(f'входят только во второй {e}')
print(f'входят в один из них {f}')