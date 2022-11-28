from sympy import *

def getFunctionValue(func,x):
    val = eval(func)
    return val

def getTotalArea(func, a, b):
    fa = getFunctionValue(func, a)
    fb = getFunctionValue(func, b)
    m = (a+b)/2
    fm = getFunctionValue(func, m)
    fm = 4*fm
    h = (b-a)/2
    result = (h/3) * (fa+fm+fb)
    return result

func = input('enter your function : ')
a = float(input('enter lower limit : '))
b = float(input('enter upper limit : '))

area = getTotalArea(func, a, b)
print('Total Area : ', area)

'''
2000*ln(140000/(140000-2100*x))-9.8*x
8
30
11065.7163277322
'''