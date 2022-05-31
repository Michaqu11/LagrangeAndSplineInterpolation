from scipy.linalg import lu

def printMAtrx(M):
    n = len(M)
    for i in range(n):
        print(M[i])


def multiply(M, V):
    nV = [0 for x in range(len(M))]
    for i in range(len(nV)):
        for j in range(len(nV)):
            nV[i] += M[i][j] * V[j]
    return nV


def forward_sub(L, b):
    N = len(L)
    y = [0.0 for y in range(len(L))]
    for i in range(N):
        temp = b[i]
        for j in range(i):
            temp -= L[i][j] * y[j]
        y[i] = temp / L[i][i]

    return y

def back_sub(U, y):
    N = len(U)
    x = [0.0 for y in range(len(U))]
    for i in reversed(range(N)):
        temp = y[i]
        for j in range(i+1, N):
            temp -= U[i][j] * x[j]
        x[i] = temp / U[i][i]
    return x


def LU_solve(matrix, b):
    P, L, U = lu(matrix)
    b = multiply(P, b)
    y = forward_sub(L, b)
    x = back_sub(U, y)

    return x
