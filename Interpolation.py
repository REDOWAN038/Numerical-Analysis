from prettytable import PrettyTable

def getResult(mat, n):
    for steps in range(0, n-1):
        max_row = steps
        max_val = 0

        for i in range(steps, n):
            if (abs(mat[i][steps]) > max_val):
                max_val = abs(mat[i][steps])
                max_row = i

        for i in range(0, n+1):
            mat[steps][i], mat[max_row][i] = mat[max_row][i], mat[steps][i]

        for i in range(steps+1, n):
            c = mat[i][steps] / mat[steps][steps]
            for j in range(steps, n+1):
                v = c*mat[steps][j]
                mat[i][j]-=v

    ans = [0.0 for j in range(n)]

    for i in range(n - 1, -1, -1):
        if(mat[i][i]==0):
            raise Exception('division by zero occur')
        ans[i] = mat[i][n] / mat[i][i]
        for k in range(i - 1, -1, -1):
            mat[k][n] -= mat[k][i] * ans[i]

    return ans

def directInterpolation(data, val):
    # linear direct interpolation
    mat = [[0.0 for j in range(3)] for i in range(2)]
    mat[0][0] = 1
    mat[0][1] = data[0][1]
    mat[0][2] = data[0][2]

    mat[1][0] = 1
    mat[1][1] = data[1][1]
    mat[1][2] = data[1][2]

    coeffs = getResult(mat, 2)
    resultLinear = coeffs[0] + (val*coeffs[1])

    # quadratic direct interpolation
    mat = [[0.0 for j in range(4)] for i in range(3)]
    mat[0][0] = 1
    mat[0][1] = data[0][1]
    mat[0][2] = data[0][1] * data[0][1]
    mat[0][3] = data[0][2]

    mat[1][0] = 1
    mat[1][1] = data[1][1]
    mat[1][2] = data[1][1] * data[1][1]
    mat[1][3] = data[1][2]

    mat[2][0] = 1
    mat[2][1] = data[2][1]
    mat[2][2] = data[2][1] * data[2][1]
    mat[2][3] = data[2][2]

    coeffs = getResult(mat, 3)
    resultQuadratic = coeffs[0] + (val*coeffs[1]) + ((val*val)*coeffs[2])
    error1 = abs(resultQuadratic - resultLinear) / resultQuadratic
    error1 = error1 * 100

    #cubic direct interpolation

    mat = [[0.0 for j in range(5)] for i in range(4)]
    mat[0][0] = 1
    mat[0][1] = data[0][1]
    mat[0][2] = data[0][1] * data[0][1]
    mat[0][3] = data[0][1] * data[0][1] * data[0][1]
    mat[0][4] = data[0][2]

    mat[1][0] = 1
    mat[1][1] = data[1][1]
    mat[1][2] = data[1][1] * data[1][1]
    mat[1][3] = data[1][1] * data[1][1] * data[1][1]
    mat[1][4] = data[1][2]

    mat[2][0] = 1
    mat[2][1] = data[2][1]
    mat[2][2] = data[2][1] * data[2][1]
    mat[2][3] = data[2][1] * data[2][1] * data[2][1]
    mat[2][4] = data[2][2]

    mat[3][0] = 1
    mat[3][1] = data[3][1]
    mat[3][2] = data[3][1] * data[3][1]
    mat[3][3] = data[3][1] * data[3][1] * data[3][1]
    mat[3][4] = data[3][2]

    coeffs = getResult(mat, 4)
    resultCubic = coeffs[0] + (val * coeffs[1]) + ((val * val) * coeffs[2]) + ((val * val * val) * coeffs[3])
    error2 = abs(resultCubic - resultQuadratic) / resultCubic
    error2 = error2 * 100

    myTable.add_row(['Direct Interpolation', resultLinear, '----', resultQuadratic, error1, resultCubic, error2])

def doLagrange(x, y, val):
    ans = 0
    n = len(x)

    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (val - x[j]) / (x[i] - x[j])

        ans += y[i] * L

    return ans

def lagrangeInterpolation(data, val):
    # linear
    x = [data[0][1], data[1][1]]
    y = [data[0][2], data[1][2]]
    resultLinear = doLagrange(x, y, val)

    # quadratic

    x.append(data[2][1])
    y.append(data[2][2])
    resultQuadratic = doLagrange(x, y, val)
    error1 = abs(resultQuadratic - resultLinear) / resultQuadratic
    error1 = error1 * 100

    # cubic

    x.append(data[3][1])
    y.append(data[3][2])
    resultCubic = doLagrange(x, y, val)
    error2 = abs(resultCubic - resultQuadratic) / resultCubic
    error2 = error2 * 100

    myTable.add_row(['Lagrange Interpolation', resultLinear, '----', resultQuadratic, error1, resultCubic, error2])

def doNewtonsDivided(x, y, val):
    n = len(x) - 1

    dataTable = [[0.0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        dataTable[i][0] = y[i]

    for j in range(n):
        for i in range(j + 1, n + 1):
            dataTable[i][j + 1] = (dataTable[i][j] - dataTable[j][j]) / (x[i] - x[j])

    ans = dataTable[0][0]

    for i in range(n):

        tmp = 1

        for j in range(i + 1):
            tmp *= (val - x[j])

        ans += tmp * dataTable[i + 1][i + 1]

    return ans

def newtonsDividedInterpolation(data, val):
    # linear
    x = [data[0][1], data[1][1]]
    y = [data[0][2], data[1][2]]
    resultLinear = doNewtonsDivided(x, y, val)

    # quadratic

    x.append(data[2][1])
    y.append(data[2][2])
    resultQuadratic = doNewtonsDivided(x, y, val)
    error1 = abs(resultQuadratic - resultLinear) / resultQuadratic
    error1 = error1 * 100

    # cubic

    x.append(data[3][1])
    y.append(data[3][2])
    resultCubic = doNewtonsDivided(x, y, val)
    error2 = abs(resultCubic - resultQuadratic) / resultCubic
    error2 = error2 * 100

    myTable.add_row(['Newtons Divided Interpolation', resultLinear, '----', resultQuadratic, error1, resultCubic, error2])

numberOfPoints = int(input('Enter number of data points : '))
x = []
y = []
print("Enter the data points x f(x) format separated by space")

for i in range(0, numberOfPoints):
    inp = input(" x f(x) {} : ".format(i+1)).split()
    x.append(float(inp[0]))
    y.append(float(inp[1]))

val = float(input('Enter the point at which you want your result : '))

myTable = PrettyTable(['Method Name', "Linear Result", 'ea(Linear)%', 'Quadratic Result', 'ea(Quadratic)%', 'Cubic Result', 'ea(Cubic)%'])

data = []

for i in range(numberOfPoints):
    data.append([abs(val - x[i]), x[i], y[i]])

data.sort()

directInterpolation(data, val)
lagrangeInterpolation(data, val)
newtonsDividedInterpolation(data, val)


print(myTable)