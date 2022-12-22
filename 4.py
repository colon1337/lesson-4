inv = {'нож':3, 'ключ':1, 'майка':2}
print(f'Инвентарь: {inv.items()}')
while True:
    a = input('Добавить или удалить предмет? (Стоп-слово: Стоп или стоп)')
    if a == 'добавить' or a == 'Добавить':
        item = dict()
        b = input('Какой предмет?')
        c = int(input('Какой вес?'))
        inv[b] = c
        print(f'Инвентарь: {inv.items()}')
    elif a == 'удалить' or a == 'Удалить':
        b = input('Какой предмет?')
        inv.pop(b)
        print(f'Инвентарь: {inv.items()}')
    elif a == 'стоп' or a == 'Стоп':
        break
    else:
        print('Введите действие')
    limit = sum(inv.values())
    if limit > 40:
        print('Вы перегружены! Освободите инвентарь!')
        print(f'Вес инвентаря: {limit}')
    else:
        print(f'Вес инвентаря: {limit}')

