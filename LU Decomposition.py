
def getUpperAndLower(mat, n):
    upper = [[0.0 for j in range(n)] for i in range(n)]
    lower = [[0.0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            upper[i][j] = mat[i][j]

    for i in range(n):
        for j in range(n):
            if(i==j):
                lower[i][j] = 1


    for j in range(0, n-1):
        for i in range(j+1, n):
            if (upper[j][j] == 0):
                return False, False
            c = upper[i][j] / upper[j][j]
            lower[i][j] = c

            for k in range(j, n):
                v = c*upper[j][k]
                upper[i][k]-=v

    return upper, lower

def preProcess(matrix, val, n):
    new_matrix = [[0.0 for j in range(n + 1)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            new_matrix[i][j] = matrix[i][j]

    for i in range(0, n):
        new_matrix[i][n] = val[i]

    return new_matrix

def solveX(temp, n):
    x = [0 for k in range(n)]

    for i in range(n - 1, -1, -1):
        try:
            x[i] = temp[i][n] / temp[i][i]
        except:

            print("Division By Zerro Error. Couldn't find solution")
            return False

        for j in range(i - 1, -1, -1):
            temp[j][n] -= (temp[j][i] * x[i])

    return x

def solveZ(temp, n):
    z = [0 for k in range(n)]
    for i in range(0, n):
        z[i] = temp[i][n]
        for j in range(i + 1, n):
            temp[j][n] -= (z[i] * temp[j][i])

    return z

def solveEquation(eqn,lower,upper,n):
    temp = preProcess(lower, eqn, n)
    z = solveZ(temp, n)
    x = preProcess(upper, z, n)
    result = solveX(x, n)
    return result


def findInverse(lower,upper,n):
    inverse = [[0.0 for j in range(n)] for i in range(n)]
    for i in range(0, n):
        inverse[i][i] = 1

    for j in range(0, n):
        eqn = [0.0 for k in range(n)]
        for i in range(0, n):
            eqn[i] = inverse[i][j]
        val = solveEquation(eqn, lower, upper, n)

        for i in range(0, n):
            inverse[i][j] = val[i]

    return inverse

n = int(input("Enter Number of Dimension: "))
print("Enter Your Matrix : ")
mat = [[0.0 for j in range(n)] for i in range(n)]

for i in range(0, n):
    v = input().split()
    for j in range(0, n):
        mat[i][j] = (float)(v[j])

upper, lower = getUpperAndLower(mat, n)
print()

if(upper==False and lower==False):
    print('no solution exists')
    exit(0)

result = findInverse(lower, upper, n)
invMatrix = [[0.0 for j in range(n)] for i in range(n)]

for j in range(n):
    for i in range(n):
        invMatrix[i][j] = result[i][j]



print("Upper Triangular Matrix : ")

for i in upper:
    for j in i:
        print('%.2f' % j, end=' ')
    print()

print()

print("Lower Triangular Matrix : ")
for i in lower:
    for j in i:
        print('%.2f' % j, end=' ')
    print()
print()

print("Inverse Matrix : ")
for i in invMatrix:
    for j in i:
        print('%.4f' % j, end=' ')
    print()
print()

'''
25 5 1 
64 8 1 
144 12 1 

10 -7 0 
-3 2.099 6
5 -1 5
'''
