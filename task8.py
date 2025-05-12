# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор

s = {'А': '@', 'Б':'~', 'В': '&', 'Г': '^', 'Д':'*', 'Е':''}
ds = {value:key for key,value in s.items()}
def shifr(q):
    if q == 1:
        o = ''
        a = input('ВВЕДИТЕ СЛОВО ДЛЯ ШИФРОВАНИЯ: ')
        for i in range(len(a)):
            if a[i] in s:
                d = a[i]
                o += str(s[d])
        return o
    if q == 2:
        o = ''
        a = input('ВВЕДИТЕ СЛОВО ДЛЯ ДЕШИФРОВАНИЯ: ')
        for i in range(len(a)):
            if a[i] in ds:
                d = a[i]
                o += str(ds[d])
        return o

print(shifr(int(input('ВВЕДИТЕ: 1 (ДЛЯ ШИФРОВАНИЯ) ИЛИ 2 (ДЛЯ ДЕШИФРАЦИИ): '))))
