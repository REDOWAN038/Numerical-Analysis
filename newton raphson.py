from prettytable import PrettyTable
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import math

def getFunctionValue(x):
    val = eval(function)
    return val

def getDerivativeFunctionValue(x):
    val = eval(devFunction)
    return val

def countSignificantDigits(x):
    return int(2-math.log10(x*2))

def getRoot(x):

    cnt = 1
    found = False
    root = -1
    error = -1

    while(True):
        l = getFunctionValue(x)
        r = getDerivativeFunctionValue(x)
        m = x-(l/r)
        ea = abs(m-x)
        ea = (ea/m)*100
        xm = getFunctionValue(m)
        myTable.add_row([cnt, x, m, ea, xm, countSignificantDigits(ea)])
        x = m
        root = m
        error = ea

        if(ea<=tol):
            found = True
            break
        if (cnt == totalIteration):
            break

        cnt+=1

    if (found):
        print("The Root is " + str(root) + " with error " + str(error))
        print('We found the root at iteration : ', cnt)

    else:
        print("Can't get accurate result for given tolerance you wanted due for iteration limitations")
        txt = 'Root after iteration {} is {} with error {}'
        print(txt.format(totalIteration, root, error))


myTable = PrettyTable(['Iteration','x(i-1)','x(i)','ea', 'f(x(i))', 'Significant Digits'])

function = input('enter your function : ')
xx = float(input('enter your initial guess : '))
tol = float(input('enter tolerance value : '))
totalIteration = int(input('enter total iteration : '))
print()

x, y = symbols('x y')
devFunction = Derivative(function, x)
devFunction =  str(devFunction.doit())

xaxis = []
yaxis = []
u = xx-xx
v = xx+xx

while u<=v:
    xaxis.append(u)
    yaxis.append(getFunctionValue(u))
    u+=0.01

getRoot(xx)
print()
print(myTable)

xaxis = np.array(xaxis)
yaxis = np.array(yaxis)
plt.axhline(y=0.0, color='r', linestyle='-')
plt.axvline(x=0.0, color='r')
plt.xlabel("m")
plt.ylabel("f(m)")
plt.plot(xaxis, yaxis)
plt.show()
