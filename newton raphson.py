from prettytable import PrettyTable
import random

myTable = PrettyTable(['Iteration','x','m','ea'])

u = float(input('enter starting value : '))
v = float(input('enter ending value : '))
tol = float(input('enter tolerence value : '))
totalIteration = int(input('enter total iteration : '))
print()

maxPower = int(input('enter maximum power of x : '))
factors = []
cnt = maxPower

while(cnt>=0):
    txt = 'enter factor of x^{} : '
    val = float(input(txt.format(cnt)))
    factors.append(val)
    cnt-=1

print()

maxPowerDev = int(input('enter maximum power of x (first Derivative) : '))
factorsDev = []
cntDev = maxPowerDev

while(cntDev>=0):
    txt = 'enter factor of x^{} : '
    val = float(input(txt.format(cntDev)))
    factorsDev.append(val)
    cntDev-=1
print()

def getFunctionValue(x):
    cnt = maxPower
    v1 = 0.00

    for val in factors:
        v1 = v1 + (val * (x ** cnt))
        cnt -= 1

    return v1

def getDerivativeFunctionValue(x):
    cnt = maxPowerDev
    v1 = 0.00

    for val in factorsDev:
        v1 = v1 + (val * (x ** cnt))
        cnt -= 1

    return v1

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