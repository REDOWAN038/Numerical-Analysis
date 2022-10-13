from prettytable import PrettyTable
import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def getFunctionValue(x):
    val = eval(function)
    return val

def findRoot(l, r):
    prev = -1.0
    cnt = 1
    found = False
    root = -1
    error = 0
    lll =l
    rrr = r

    while l<r:
        ll = l
        rr = r
        m = (l + r) / 2.0
        xm = getFunctionValue(m)
        xl = getFunctionValue(l)


        if (xl * xm > 0.0):
            l = m
        elif (xl * xm < 0.0):
            r = m
        else:
            found = True
            root = m
            if (cnt > 1):
                ea = abs(m - prev)
                ea = ea / m
                ea = ea * 100
                error = ea
                myTable.add_row([cnt, ll, rr, m, ea, xm])
            else:
                myTable.add_row([cnt, ll, rr, m, '-', xm])
            break

        if (cnt > 1):
            ea = abs(m - prev)
            ea = ea / m
            ea = ea * 100
            error = ea
        if(cnt>1):
            myTable.add_row([cnt, ll, rr, m, ea, xm])
            if (ea <= tol):
                found = True
                root = m
                break
        else:
            myTable.add_row([cnt, ll, rr, m, '-', xm])

        cnt += 1
        prev = m

        if (cnt == (totalIteration + 1)):
            root = m
            break

    if (found):
        print("The Root is " + str(root) + " with error " + str(error))
        print('We found the root at iteration : ', cnt)
    else:
        print("Can't get accurate result for given tolerance you wanted due for iteration limitations")
        txt = 'Root after iteration {} is {} with error {}'
        print(txt.format(totalIteration, root, error))

    while lll <= rrr:
        x.append(lll)
        y.append(getFunctionValue(lll))
        lll = lll + 0.01

myTable = PrettyTable(['Iteration','l','r','m','ea','F(m)'])

function = input('enter your function : ')
u = float(input('enter lower limit : '))
v = float(input('enter upper limit : '))
tol = float(input('enter tolerance value : '))
totalIteration = int(input('enter total iteration : '))
print()

x, y = symbols('x y')
firstSign = getFunctionValue(u)
secondSign = getFunctionValue(v)
x = []
y = []
iter = []
err = []


if((firstSign*secondSign) < 0):
    findRoot(u,v)
    print()
    print(myTable)

    x = np.array(x)
    y = np.array(y)
    plt.axhline(y=0.0, color='r', linestyle='-')
    plt.axvline(x=0.0, color='r')
    plt.xlabel("m")
    plt.ylabel("f(m)")
    plt.plot(x, y)
    plt.show()

else:
    print("Not a valid range")