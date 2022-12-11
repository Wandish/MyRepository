# Task 1

# Напишите скрипт, который будет вычислять
# факториал введенного числа
# без использования рекурсии.

vvod = int(input("Введите число: "))
 
factorial = 1
 
for i in range(2, vvod+1):
    factorial *= i
 
print(factorial)