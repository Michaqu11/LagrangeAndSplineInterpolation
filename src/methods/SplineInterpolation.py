import random

from src.draw import draw
from src.operations.LU import LU_solve
from src.operations.matrixAndVectorOperation import create_zero_vector, create_zero_square_matrix


def count_interpolation_function(points):
    # data = [(1, 6), (3, -2), (5, 4)]
    size = (len(points) - 1)
    matrixSize = 4 * size
    M = create_zero_square_matrix(matrixSize)
    V = create_zero_vector(matrixSize)
    size = (len(points) - 1)

    for i, point in enumerate(points[:size]):
        x, y = point
        pos = 4 * i
        M[pos][pos] = 1.0
        V[pos] = float(y)

    for i, point in enumerate(points[:size]):
        x, y = point
        next_x, next_y = points[i + 1]
        h = float(next_x) - float(x)
        pos = 4 * i
        for j in range(4):
            M[pos + 1][pos + j] = h ** j
        V[pos + 1] = float(next_y)

    for i, point in enumerate(points[1:size]):
        i = i + 1
        x, y = point
        prev_x, prev_y = points[i - 1]
        h = float(x) - float(prev_x)
        pos = 4 * (i - 1)
        curr_pos = 4 * i
        for j in range(1, 4):
                M[pos + 2][pos + j] = j * h**(j-1)
        M[pos + 2][curr_pos + 1] = -1
        V[pos + 2] = 0

    for i, point in enumerate(points[1:size]):
        i = i + 1
        x, y = point
        prev_x, prev_y = points[i - 1]
        h = float(x) - float(prev_x)
        pos = 4 * (i - 1)
        curr_pos = 4*i
        for j in range(1, 4):
            M[pos + 3][pos + 2] = 2
            M[pos + 3][pos + 3] = 6*h
            M[pos + 3][curr_pos + 2] = -2
        V[pos + 3] = 0

    x1, y1 = points[-1]
    x0, y0 = points[-2]
    h = float(x1) - float(x0)
    M[-2][2] = 2
    M[-1][-1] = 6 * h
    M[-1][-2] = 2
    V[-1] = 0
    V[-2] = 0

    return LU_solve(M, V)

def spline_calc(x, interpolation, points):
    for i in range(len(points)-1):
        result = 0
        if points[i][0] <= x <= points[i+1][0]:
            for j in range(4):
                h = x - points[i][0]
                result += interpolation[4 * i + j] * h**j
            break
    return result

def find_probe_points(points, count):
    n = len(points) / (count - 1)
    probe_points = []
    for i in range(count):
        index = int(i*n) - 1
        if not i:
            index = 0
        probe_points.append((points[index][0], points[index][1]))
    return probe_points

def spline_interpolateon(points, n):

    probePoints = find_probe_points(points, n)
    probePoints2 = [probePoints[0]]
    index = []
    for i in range(len(probePoints) - 2):
        r = random.randint(0, len(points) - 1)
        index.append(r)

    index.sort()
    for i in range(len(probePoints) - 2):
        probePoints2.append((points[index[i]][0], points[index[i]][1]))
    probePoints2.append(probePoints[-1])
    #probePoints = probePoints2
    dis = []
    h = []
    interpolated = []
    probeX = []
    probeH = []

    interpolation = count_interpolation_function(probePoints)

    for point in points:
        dis.append(point[0])
        h.append(point[1])
        height = spline_calc(point[0], interpolation, probePoints)
        interpolated.append(height)

    for point in probePoints:
        probeX.append(point[0])
        probeH.append(point[1])


    draw(dis, h, dis[:-1], interpolated[:-1], probeX, probeH,len(probePoints), 'Spline' )

