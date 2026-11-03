from random import randint as ri
start_list = [ri(0, 100_000) for _ in range(100)] #создаем список
print("Исходный список:", start_list)
sorted_bubble = start_list.copy() #сортировка пузырьком
b = 0  #счетчик сравнений для пузырька
stop_flag = True
while stop_flag:
    stop_flag = False
    for i in range(len(sorted_bubble) - 1):
        b += 1  # считаем сравнение
        if sorted_bubble[i] < sorted_bubble[i + 1]:
            sorted_bubble[i], sorted_bubble[i + 1] = sorted_bubble[i + 1], sorted_bubble[i]
            stop_flag = True
print("список при пузырьке:", sorted_bubble)
print("Кол-во сравнений пузырька:", b)
selection_list = start_list.copy() #сортировка выбором
c = 0  #счетчик сравнений
for i in range(len(selection_list)):
    max_idx = i
    for j in range(i + 1, len(selection_list)):
        c += 1  #Считаем сравнение
        if selection_list[j] > selection_list[max_idx]:
            max_idx = j
    selection_list[i], selection_list[max_idx] = selection_list[max_idx], selection_list[i] #меняем местами элемент и максимум
print("список при выборке:", selection_list)
print("Кол-во сравнений выборки:", c)
