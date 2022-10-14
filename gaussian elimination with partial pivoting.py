
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


n = int(input("Number of Equations: "))
print("Enter coefficients of the equations in format ax^n+bx^(n-1)+...+c = d")
mat = [[0.0 for j in range(n + 1)] for i in range(n)]

for i in range(0, n):
    txt = 'Equation {} : '
    v = input(txt.format(i + 1)).split()
    for j in range(0, n+1):
        mat[i][j] = (float)(v[j])

result = getResult(mat, n)
print()
print("Solution of Given Equations : ", end=' ')
print(result)

'''
25 5 1 106.8
64 8 1 177.2
144 12 1 279.2

10 -7 0 7
-3 2.099 6 3.901
5 -1 5 6
'''
