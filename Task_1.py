'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''


def check_day(number):
    if 6 <= number <=7:
        return('Выходной день')
    elif 1 <= number <= 5:
        return('Рабочий день')
    else:
        return('Некорректынй ввод')


n = int(input('Введите день недели (число от 1 до 7): '))
print(check_day(n))