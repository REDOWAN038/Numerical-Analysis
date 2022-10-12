from prettytable import PrettyTable
import random

myTable = PrettyTable(['Iteration','x','m','ea'])

function = input('enter your function : ')
devFunction = input('enter first derivative of your function : ')
u = float(input('enter starting value : '))
v = float(input('enter ending value : '))
tol = float(input('enter tolerence value : '))
totalIteration = int(input('enter total iteration : '))
print()

def getFunctionValue(x):
    val = eval(function)
    return val

def getDerivativeFunctionValue(x):
    val = eval(devFunction)
    return val

def getRoot(x):

    cnt = 1

    while(True):
        l = getFunctionValue(x)
        r = getDerivativeFunctionValue(x)
        m = x-(l/r)
        ea = abs(m-x)
        ea = (ea/m)*100
        myTable.add_row([cnt, x, m, ea])
        x = m

        if(ea<=tol):
            break
        if (cnt == totalIteration):
            break

        cnt+=1

x = random.uniform(u,v)
getRoot(x)
print(myTable)