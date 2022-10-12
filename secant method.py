from prettytable import PrettyTable

myTable = PrettyTable(['Iteration','x','y','z','ea'])

function = input('enter your function : ')
x = float(input('enter first guess : '))
y = float(input('enter second guess : '))
tol = float(input('enter tolerence value : '))
totalIteration = int(input('enter total iteration : '))

def getFunctionValue(x):
    val = eval(function)
    return val

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


getRoot(x,y)
print()
print(myTable)