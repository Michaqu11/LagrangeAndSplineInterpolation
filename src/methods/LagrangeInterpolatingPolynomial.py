import random

from src.draw import draw


def count_interpolation_function(x, probePoints):
    Fx = 0
    N = len(probePoints)
    for i in range(N):
        x_i, y_i = probePoints[i]
        o = 1
        for j in range(N):
            if i != j:
                x_j, y_j = probePoints[j]
                o *= (float(x) - float(x_j)) / (float(x_i) - float(x_j))

        Fx += float(y_i) * o

    return Fx

def find_probe_points(points, count):
    n = len(points) / (count - 1)
    probe_points = []
    for i in range(count):
        index = int(i*n) - 1
        if not i:
            index = 0
        probe_points.append((points[index][0], points[index][1]))
    return probe_points

def lagrangeInterpolatingPolynomial(points, nodesNumer):
    disData = []
    hData = []
    interpolated = []

    disProbe = []
    hProbe = []
    probePoints = find_probe_points(points, nodesNumer)
    probePoints2 = [probePoints[0], probePoints[-1]]
    for i in range(len(probePoints) - 2):
        r = random.randint(0, len(points) - 1)
        probePoints2.append((points[r][0], points[r][1]))
    #probePoints = probePoints2

    for point in points:
        x, y = point
        disData.append(float(x))
        hData.append(float(y))
        interpolated.append(float(count_interpolation_function(x, probePoints)))


    for point in probePoints:
        x, y = point
        disProbe.append(float(x))
        hProbe.append(float(count_interpolation_function(x, probePoints)))

    #print("Liczba wezłów: " + str(len(probePoints)))
    draw(disData, hData, disData, interpolated, disProbe, hProbe, len(probePoints), ' Lagrange\'a')
