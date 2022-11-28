import numpy as np
import matplotlib.pyplot as plt

def estimateCoefs(x, y, n):
    meanX = np.mean(x)
    meanY = np.mean(y)

    sum1 = np.sum(y * x) - n * meanY * meanX
    sum2 = np.sum(x * x) - n * meanX * meanX

    b1 = sum1 / sum2
    b0 = meanY - b1 * meanX

    return (b0, b1)

def plotRegressionLine(x, y, b):
    plt.scatter(x, y, color="m", marker="o", s=30)
    yPred = b[0] + b[1] * x
    plt.plot(x, yPred, color="g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

n = int(input('enter number of points : '))
x = []
y = []

for i in range(n):
    inp = input("Point No. {} : ".format(i + 1)).split()
    x.append(int(inp[0]))
    y.append(int(inp[1]))

x = np.array(x)
y = np.array(y)

coefs = estimateCoefs(x, y, n)
print("\nEstimated coefficients:\nb0 = {}  \nb1 = {}".format(coefs[0], coefs[1]))
plotRegressionLine(x, y, coefs)

'''
enter number of points : 10
Point No. 1 : 0 1
Point No. 2 : 1 3
Point No. 3 : 2 2
Point No. 4 : 3 5
Point No. 5 : 4 7
Point No. 6 : 5 8
Point No. 7 : 6 8
Point No. 8 : 7 9
Point No. 9 : 8 10
Point No. 10 : 9 12
'''