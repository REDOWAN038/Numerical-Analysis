
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

def getResult(lower, upper, mat, n):
    result = []

    for k in range(n):
        temp = [[0.0 for j in range(n + 1)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                temp[i][j] = lower[i][j]

        for i in range(n):
            if(i==k):
                temp[i][n] = 1.0
            else:
                temp[i][n] = 0.0

        for i in range(n//2):
            temp[i], temp[n-i-1] = temp[n-i-1], temp[i]

        z = [0.0 for i in range(0, n)]

        for i in range(n - 1, -1, -1):
            z[i] = temp[i][n] / temp[i][i]
            for kk in range(i - 1, -1, -1):
                temp[kk][n] -= temp[kk][i] * z[i]

        for i in range(n//2):
            z[i], z[n-i-1] = z[n-i-1], z[i]

        print(z)

        for i in range(n):
            for j in range(n):
                temp[i][j] = upper[i][j]

        for i in range(n):
            temp[i][n] = z[i]

        ans = [0 for k in range(n)]
        for i in range(n - 1, -1, -1):
            ans[i] = temp[i][n] / temp[i][i]
            for kk in range(i - 1, -1, -1):
                temp[kk][n] -= temp[kk][i] * ans[i]

        result.append(ans)

    return result

'''
def getResult(lower,upper,mat,n):
    temp = [[0.0 for j in range(n + 1)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            temp[i][j] = lower[i][j]

    for i in range(n):
        temp[i][n] = mat[i][n]

    z = [0.0 for i in range(0, n)]
    for i in range(0, n):
        z[i] = temp[i][n] / temp[i][i]
        for k in range(i + 1, n):
            temp[k][n] -= temp[k][i] * z[i]

    for i in range(n):
        for j in range(n):
            temp[i][j] = upper[i][j]

    for i in range(n):
        temp[i][n] = z[i]

    ans = [0 for k in range(n)]
    for i in range(n - 1, -1, -1):
        ans[i] = temp[i][n] / temp[i][i]
        for k in range(i - 1, -1, -1):
            temp[k][n] -= temp[k][i] * ans[i]

    return ans
'''



n = int(input("Enter Number of Dimension: "))
print("Enter Your Matrix : ")
mat = [[0.0 for j in range(n)] for i in range(n)]

for i in range(0, n):
    v = input().split()
    for j in range(0, n):
        mat[i][j] = (float)(v[j])

upper, lower = getUpperAndLower(mat, n)
result = getResult(lower, upper, mat, n)
print()

if(upper==False and lower==False):
    print('no solution exists')
    exit(0)

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

print('Result : ', result)

'''
25 5 1 106.8
64 8 1 177.2
144 12 1 279.2

10 -7 0 7
-3 2.099 6 3.901
5 -1 5 6
'''
