first = input("Введите  первое число:")
second =input("Введите второе число:")
third =input("Введите третье число:")
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')

