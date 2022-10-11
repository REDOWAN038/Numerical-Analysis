from prettytable import PrettyTable

myTable = PrettyTable(['Iteration','l','r','m','ea'])

u = float(input('enter starting value : '))
v = float(input('enter ending value : '))
tol = float(input('enter tolerence value : '))
totalIteration = int(input('enter total iteration : '))
maxPower = int(input('enter maximum power of x : '))

factors = []

cnt = maxPower

def getValue(a):
    cnt = maxPower
    v1 = 0.00

    for val in factors:
        v1 = v1 + (val * (a**cnt))
        cnt-=1

    return v1

def findRoot(l,r):
    prev = -1.0
    cnt = 1
    ea = -1.0

    while l<r:
        ll = l
        rr = r
        m = (l + r) / 2.0
        xm = getValue(m)
        xl = getValue(l)

        if (xl * xm > 0.0):
            l = m
        elif (xl * xm < 0.0):
            r = m
        else:
            break

        if(cnt>1):
            ea = abs(m-prev)
            ea = ea/m
            ea = ea*100

        myTable.add_row([cnt,ll,rr,m,ea])

        cnt+=1
        prev = m

        if(ea<=tol):
            break

        if(cnt==(totalIteration+1)):
            break

while(cnt>=0):
    txt = 'enter factor of x^{} : '
    val = float(input(txt.format(cnt)))
    factors.append(val)
    cnt-=1

firstSign = getValue(u)
secondSign = getValue(v)

if((firstSign*secondSign) < 0):
    findRoot(u,v)
    print()
    print(myTable)

