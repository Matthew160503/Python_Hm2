import math
import fractions

a = input("Введите дробь через /: ")
b = input("Введите вторую дробь через /: ")


def lcm(x, y):
    return (x * y) // math.gcd(x, y)


def fractions_summ(x, y):
    list_a = x.split('/')
    list_b = y.split('/')

    lcm_nums = lcm(int(list_a[1]), int(list_b[1]))

    summ = str(int(lcm_nums / int(list_a[1])) * int(list_a[0]) + int(lcm_nums /
               int(list_b[1])) * int(list_b[0])) + '/' + str(lcm_nums)

    list_summ = summ.split('/')

    temp = math.gcd(int(list_summ[0]), int(list_summ[1]))

    if temp != 1:
        list_summ[0] = str(int(int(list_summ[0]) / temp))
        list_summ[1] = str(int(int(list_summ[1]) / temp))
        summ = list_summ[0] + '/' + list_summ[1]

    return summ


def fraction_multiply(x, y):
    list_a = x.split('/')
    list_b = y.split('/')

    multiply = str(int(list_a[0]) * int(list_b[0])) + '/' + str(int(list_a[1]) * int(list_b[1]))

    list_multiply = multiply.split('/')
    temp = math.gcd(int(list_multiply[0]), int(list_multiply[1]))

    if temp != 1:
        list_multiply[0] = str(int(int(list_multiply[0]) / temp))
        list_multiply[1] = str(int(int(list_multiply[1]) / temp))
        multiply = list_multiply[0] + '/' + list_multiply[1]

    return multiply


check_a = fractions.Fraction(a)
check_b = fractions.Fraction(b)

print('Cумма = ' + fractions_summ(a, b) + '. Произведение = ' + fraction_multiply(a, b))
print('Проверка сумммы = ' + str(check_a + check_b) + '. Проверка произведения = ' + str(check_a * check_b))