#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

with open('file.txt', 'r') as f:
    positions = f.read().split('\n')
positions = list(map(int, positions))
n = int(input())
list_gen = [i for i in range(-n, n+1)]
multi = 1
for pos in positions:
    multi *=list_gen[pos]
print(positions)
print(list_gen)
print(multi)