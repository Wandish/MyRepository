# Вводит кол-во раз, после чего ввод цыфер и вывод макс и мин число

# koli4estvo = int(input("Ввеедите кол-во: "))

# lis_t = []

# for x in range(koli4estvo):
#     lis_t.append(int(input("Ввеедите число: ")))

# Попробовать завернуть в list Comprehension
# list_Comprehension = [lis_t.append(int(input("Ввеедите число: "))) for x in range(koli4estvo)]

# print(f'Максимальное число: {max(lis_t)}')
# print(f'Минимальное число: {min(lis_t)}')

# a = "d"
# print(hash(a))

# # Task 1
# В диапазоне от 1 до 10 определите
# • четные числа, которые делятся на 2,
# • нечетные числа, которые делятся на 3,
# • числа, которые не делятся на 2 и 3.

for x in range(1,11):
    if x % 2 ==0:
        print(f'Четные числа, которые делятся на 2: {x}')
    elif x % 3 ==0:
        print(f'Нечетные числа, которые делятся на 3: {x}')
    else: 
        print(f'Числа, которые не делятся на 2 и 3: {x}')
    