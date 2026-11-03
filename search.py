import random
collection = [] #создаём уникальный список
while len(collection) < 100:
    a = random.randint(0, 1000000)
    if a not in collection:
        collection.append(a)
collection.sort()
print("сгенерированный список:", collection)
print("Введите значение:")
element = int(input())
#линейный поиск
a = 0  #переменная для проверки отсутствия значений
b = 0  #счетчик сравнений
for i in range(len(collection)):
    b += 1
    if collection[i] == element:
        a += 1
        print("Индекс элемента =", i)
        break
if a == 0:
    print("Элемент не находится в списке ")
print("Кол-во сравнений линейным методом =", b)
#бинарный поиск
lys = collection  #используем тот же список
val = element  #ищем то же самое значение
first = 0
last = len(lys) - 1
index = -1
cn = 0  #счетчик сравнений
d = 0  #неизменяемая переменная если эл. не найден
while (first <= last) and (index == -1):
    mid = (first + last) // 2
    cn += 1  #считаем каждую проверку в цикле
    if lys[mid] == val:
        index = mid
        d += 1
        print("Индекс элемента =", index)
    else:
        if val < lys[mid]:
            last = mid - 1
        else:
            first = mid + 1
if d == 0:
    print("Элемент не находится в списке ")
print("Кол-во сравнений бинарным методом =", cn)
