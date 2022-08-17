#Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3
a = []
print('Ведите длину массива')
n = int(input())
print("Введите элементы массива")
for i in range(n):
    a.append(int(input()))
b = []
for i in a:
    if i % 3 == 0:
        b.append(i)
print(b)
