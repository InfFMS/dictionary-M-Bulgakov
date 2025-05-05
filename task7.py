# Даны два словаря. Напишите программу, которая объединит эти словари. 
# Если ключи встречаются в обоих исходных словарях, значения, 
# которые хранятся по этим ключам складываются.
# Пример:

# Первый словарь: {'a': 100, 'b': 200, 'c':300}
# Второй словарь: {'a': 300, 'b': 200, 'd':400}
# Результат: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

s1 = {input(f'key {i + 1} '):int(input(f'value {i + 1} ')) for i in range(int(input('length 1 ')))}
s2 = {input(f'key {j + 1} '):int(input(f'value {j + 1} ')) for j in range(int(input('length 2 ')))}

key1 = list(s1.keys())
key2 = list(s2.keys())
k = key1
for i in range(len(key2)):
    k.append(key2[i])
key3 = sorted(k)
s3 = {}
for i in key3:
    s3[i] = s1.get(i,0) + s2.get(i,0)
print(s3)