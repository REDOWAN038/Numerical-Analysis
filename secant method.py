from prettytable import PrettyTable
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def getFunctionValue(x):
    val = eval(function)
    return val

def getRoot(x,y):
    cnt = 1
    found = False
    root = -1
    error = -1

    while(1):
        fx = getFunctionValue(x)
        fy = getFunctionValue(y)

        z = y - ((fy*(y-x))/(fy-fx))
        fz = getFunctionValue(z)
        p = abs(z-y)
        print(p)
        p/=z
        print(p)
        ea = p * 100
        print(ea)

        root = z
        error = ea

        myTable.add_row([cnt, x, y, z, ea, fz])

        x = y
        y = z

        if(ea<=tol):
            found = True
            break

        if(cnt==totalIteration):
            break

        cnt+=1

    if (found):
        print("The Root is " + str(root) + " with error " + str(error))
        print('We found the root at iteration : ', cnt)

    else:
        print("Can't get accurate result for given tolerance you wanted due for iteration limitations")
        txt = 'Root after iteration {} is {} with error {}'
        print(txt.format(totalIteration, root, error))


myTable = PrettyTable(['Iteration','x(i-2)','x(i-1)','x(i)','ea','f(x(i))'])

function = input('enter your function : ')
xx = float(input('enter first guess : '))
xy = float(input('enter second guess : '))
tol = float(input('enter tolerance value : '))
totalIteration = int(input('enter total iteration : '))
print()

x = []
y = []
u = xx-xx
v = xy+xy

while u<=v:
    x.append(u)
    y.append(getFunctionValue(u))
    u+=0.01


getRoot(xx, xy)
print()
print(myTable)

xaxis = np.array(x)
yaxis = np.array(y)
plt.axhline(y=0.0, color='r', linestyle='-')
plt.axvline(x=0.0, color='r')
plt.xlabel("m")
plt.ylabel("f(m)")
plt.plot(xaxis, yaxis)
plt.show()