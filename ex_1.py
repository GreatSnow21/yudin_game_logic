# def isEven(value):
#     return value % 2 == 0

"""

В предложенном алгоритме используется оператор вычисления остатка.

Плюсы: важное преимущество - простота в понимании. Также оператор
удобен в использовании, так как непосредственно работает с числом.
Код читабелен и не вызывает дополнительных воросов.

Минусы: более медленный, чем представленная альтернатива. Причиной
является операция деления, которая используется оператором
для вычисления остатка.


"""

def isEven(value):
    return value & 1 == 0

'''

В качестве аналогичного алгоритма я использовал функцию с побитовым И (&).

Плюсы: более быстрая работа с большими числами по причине того,
что операции с битами затрачивают меньше времени, в отличие от вычисления
остатка.

Минусы: более сложный с точки зрения понимания принципов работы с побитовыми
операторами в Python. Необходимо обладать базовыми знаниями работы с
двоичными разрядами.

'''
num = int(input())
num_res = isEven(num)

print(num_res)
