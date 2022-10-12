from prettytable import PrettyTable
import math

def getFunctionValue(x):
    val = eval(function)
    return val

def findRoot(l,r):
    prev = -1.0
    cnt = 1

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
            if (cnt > 1):
                ea = abs(m - prev)
                ea = ea / m
                ea = ea * 100
                myTable.add_row([cnt, ll, rr, m, ea])
            else:
                myTable.add_row([cnt, ll, rr, m, '-'])
            break

        if (cnt > 1):
            ea = abs(m - prev)
            ea = ea / m
            ea = ea * 100
        if(cnt>1):
            myTable.add_row([cnt, ll, rr, m, ea])
            if (ea <= tol):
                break
        else:
            myTable.add_row([cnt, ll, rr, m, '-'])

        cnt += 1
        prev = m

        if (cnt == (totalIteration + 1)):
            break

myTable = PrettyTable(['Iteration','l','r','m','ea'])

function = input('enter your function : ')
u = float(input('enter starting value : '))
v = float(input('enter ending value : '))
tol = float(input('enter tolerence value : '))
totalIteration = int(input('enter total iteration : '))


firstSign = getFunctionValue(u)
secondSign = getFunctionValue(v)


if((firstSign*secondSign) < 0):
    findRoot(u,v)
    print()
    print(myTable)