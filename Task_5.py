"""
Используя цикл while, выведите на экран для числа 2 его
степени от 0 до 20. Возведение в степень в Python обозначается как
**(2**2 = 4).
"""

num = 2
step = 0

while step <= 20:
    print(num ** step)
    step += 1