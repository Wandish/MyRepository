# Task 2

# Создайте список, содержащий элементы целочисленного типа, затем
# используйте цикл, чтобы изменить тип этих элементов на плавающий тип.
# (Подсказка: используйте встроенную функцию float()).

int_list = [1,2,3,4,5,6,7,8,9,10]
float_list = []
for i in int_list:
    float_list.append(float(i))
print(float_list)


array = [1,2,3,4,5,6,7,8,9,10]
print(id(array))
array = list(map(float, array))
print(id(array))

# Task 3

# Вывести числа Фибоначчи до введенного числа n, с помощью циклов.
# (Последовательность чисел Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13 и т. д.)

fib1 = fib2 = 1
 
n = int(input("Введите число: "))
fib1 = fib2 = 1
print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')