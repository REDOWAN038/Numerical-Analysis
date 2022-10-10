from prettytable import PrettyTable

myTable = PrettyTable(['Iteration','l','r','m','ea'])

u = float(input('enter starting value : '))
v = float(input('enter ending value : '))
tol = float(input('enter tolerence value : '))
maxPower = int(input('enter maximum power of x : '))

factors = []

cnt = maxPower

def cheackSign(a):
    cnt = maxPower
    v1 = 0.00

    for val in factors:
        v1 = v1 + (val * (a**cnt))
        cnt-=1

    return v1

def findRoot(l,r,tol):
    prev = -1.0
    cnt = 1
    res = -1.0
    ea = -1.0
    found = False

    ll = l
    rr = r

    while l<r:
        ll = l
        rr = r
        m = (l + r) / 2.0
        xm = cheackSign(m)
        xl = cheackSign(l)

        if (xl * xm > 0.0):
            l = m
        elif (xl * xm < 0.0):
            r = m
        else:
            res = m
            break

        if(cnt>1):
            ea = abs(m-prev)
            ea = ea/m
            ea = ea*100
            '''
            if(ea<=tol):
                found = True
                res = m
                break
            '''
        myTable.add_row([cnt,ll,rr,m,ea])

        cnt+=1
        prev = m

        if(cnt==11):
            break

    if(found):
        print('root is : ', res)
    else:
        print('no root found')

while(cnt>=0):
    txt = 'enter factor of x^{} : '
    val = float(input(txt.format(cnt)))
    factors.append(val)
    cnt-=1

firstSign = cheackSign(u)
secondSign = cheackSign(v)

if((firstSign*secondSign) < 0):
    findRoot(u,v,tol)
    print()
    print(myTable)

