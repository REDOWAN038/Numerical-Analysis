from sympy import *
from prettytable import PrettyTable

def getFunctionValue(func,x):
    val = eval(func)
    return val

def getTotalArea(func, a, b, n):
    h = (b-a)/n
    fval = []

    curr = a

    for i in range(0, n+1) :
        val = getFunctionValue(func, curr)
        fval.append(val)
        curr+=h

    odd = 0
    for i in range(1, n, 2):
        odd+=fval[i]
    odd = 4*odd

    even = 0

    for i in range(2, n-1, 2):
        even+=fval[i]
    even = 2*even

    result = (h/3) * (fval[0]+odd+even+fval[n])
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
enter your function : 2000*ln(140000/(140000-2100*x))-9.8*x
enter lower limit : 8
enter upper limit : 30
enter number of times you will give segments : 5
enter number of segments : 2
enter number of segments : 4
enter number of segments : 6
enter number of segments : 8
enter number of segments : 10
'''
