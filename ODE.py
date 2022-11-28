from sympy import *
from prettytable import PrettyTable

def getFunctionValue(eqn,x,y):
    val = eval(eqn)
    return val

def euler(eqn,x,y,xn,step):
    val = getFunctionValue(eqn, x, y)
    val = val*step
    curr = y+val


    if(xn==(x+step)):
        result =  curr
    else:
        result = euler(eqn,x+step,curr,xn,step)

    return result

def heun(eqn,x,y,xn,step):
    a2 = 1/2
    a1 = 1-a2
    p = (1/2)/a2
    q = (1/2)/a2

    k1 = getFunctionValue(eqn,x,y)
    k2 = getFunctionValue(eqn,x+(p*step),y+(q*k1*step))

    val = a1*k1 + a2*k2
    val = val*step
    curr = y+val

    if (xn == (x + step)):
        result = curr
    else:
        result = heun(eqn, x + step, curr, xn, step)

    return result

def midpoint(eqn,x,y,xn,step):
    a2 = 1
    a1 = 1-a2
    p = (1/2)/a2
    q = (1/2)/a2

    k1 = getFunctionValue(eqn,x,y)
    k2 = getFunctionValue(eqn,x+(p*step),y+(q*k1*step))

    val = a1*k1 + a2*k2
    val = val*step
    curr = y+val

    if (xn == (x + step)):
        result = curr
    else:
        result = midpoint(eqn, x + step, curr, xn, step)

    return result

def ralston(eqn,x,y,xn,step):
    a2 = 2/3
    a1 = 1-a2
    p = (1/2)/a2
    q = (1/2)/a2

    k1 = getFunctionValue(eqn,x,y)
    k2 = getFunctionValue(eqn,x+(p*step),y+(q*k1*step))

    val = a1*k1 + a2*k2
    val = val*step
    curr = y+val

    if (xn == (x + step)):
        result = curr
    else:
        result = ralston(eqn, x + step, curr, xn, step)

    return result


eqn = input('Enter Your Equation : ')
x0 = float(input('x0 : '))
y0 = float(input('y0 : '))
xn = float(input('xn : '))
cnt = int(input('How many times you will give step size : '))

myTable = PrettyTable(['Step Size','Euler','ea(Euler)%','Heun','ea(Heun)%','Midpoint','ea(Midpoint)%', 'Ralston', 'ea(Ralston)%',])
prevEular, prevHeun, prevMidpoint, prevRalston = 0, 0, 0, 0

for i in range(0, cnt):
    step = float(input('Step Size : '))
    ansEuler = euler(eqn, x0, y0, xn, step)
    ansHeun = heun(eqn, x0, y0, xn, step)
    ansMidpoint = midpoint(eqn, x0, y0, xn, step)
    ansRalston = ralston(eqn, x0, y0, xn, step)

    if(i==0):
        myTable.add_row([step, ansEuler, '----', ansHeun,  '----', ansMidpoint,  '----', ansRalston, '----'])
        prevEular = ansEuler
        prevHeun = ansHeun
        prevMidpoint = ansMidpoint
        prevRalston = ansRalston

    else:
        eaEular = (abs(ansEuler - prevEular) / ansEuler ) * 100
        eaHeun = (abs(ansHeun - prevHeun) / ansHeun) * 100
        eaMidpoint = (abs(ansMidpoint - prevMidpoint) / ansMidpoint) * 100
        eaRalston = (abs(ansRalston - prevRalston) / ansRalston) * 100
        myTable.add_row([step, ansEuler, eaEular, ansHeun, eaHeun, ansMidpoint, eaMidpoint, ansRalston, eaRalston])
        prevEular = ansEuler
        prevHeun = ansHeun
        prevMidpoint = ansMidpoint
        prevRalston = ansRalston

print(myTable)

'''
eqn : -2.2067*10**(-12)*(y**4-81*10**8)
x0 : 0
y0 : 1200
xn : 480
How many times you will give step size : 5
Step Size : 480
Step Size : 240
Step Size : 120
Step Size : 60
Step Size : 30
'''