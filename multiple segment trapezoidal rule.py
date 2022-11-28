from sympy import *
from prettytable import PrettyTable

def getFunctionValue(func,x):
    val = eval(func)
    return val

def getTotalArea(func, a, b, n):
    fa = getFunctionValue(func,a)
    fb = getFunctionValue(func,b)
    tot = 0
    h = (b-a)/n

    for i in range(1, n):
        tot = tot + getFunctionValue(func, a+i*h)

    tot = 2*tot
    result = (h/2)*(fa+tot+fb)
    return result

func = input('enter your function : ')
a = float(input('enter lower limit : '))
b = float(input('enter upper limit : '))
cnt = int(input('enter number of times you will give segments : '))
myTable = PrettyTable(['number of segments', 'Area', 'ea(%)'])
prev = 0

for i in range(0, cnt):
    n = int(input('enter number of segments : '))
    area = getTotalArea(func, a, b, n)

    if(i==0):
        myTable.add_row([n, area, '----'])
    else:
        ea = (abs(area-prev) / area) * 100
        myTable.add_row([n, area, ea])

    prev = area

print(myTable)

'''
2000*ln(140000/(140000-2100*x))-9.8*x
8
30
enter number of times you will give segments : 8
enter number of segments : 1
enter number of segments : 2
enter number of segments : 3
enter number of segments : 4
enter number of segments : 5
enter number of segments : 6
enter number of segments : 7
enter number of segments : 8
'''