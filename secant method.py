from prettytable import PrettyTable

myTable = PrettyTable(['Iteration','x','y','z','ea'])

x = float(input('enter first guess : '))
y = float(input('enter second guess : '))
tol = float(input('enter tolerence value : '))
totalIteration = int(input('enter total iteration : '))
maxPower = int(input('enter maximum power of x : '))

factors = []

cnt = maxPower

def getFunctionValue(x):
    cnt = maxPower
    v1 = 0.00

    for val in factors:
        v1 = v1 + (val * (x ** cnt))
        cnt -= 1

    return v1

def getRoot(x,y):
    cnt = 1

    while(1):
        fx = getFunctionValue(x)
        fy = getFunctionValue(y)

        z = y - ((fy*(y-x))/(fy-fx))

        ea = (abs(z-y)/z) * 100

        myTable.add_row([cnt, x, y, z, ea])

        x = y
        y = z

        if(ea<=tol):
            break

        if(cnt==totalIteration):
            break

        cnt+=1


while(cnt>=0):
    txt = 'enter factor of x^{} : '
    val = float(input(txt.format(cnt)))
    factors.append(val)
    cnt-=1

getRoot(x,y)
print()
print(myTable)