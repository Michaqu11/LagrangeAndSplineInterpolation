from matplotlib import pyplot, pyplot as plt

def draw(dis, h, interpolatedx, interpolatedh, td, th, n, metod):
    plt.plot(dis, h, 'o', color='red', markersize=3, label='dane wejściowe')
    plt.plot(interpolatedx, interpolatedh, color='green', label='funkcja interpolująca')
    plt.plot(td, th, 'o', markersize=3, color='blue', label='dane interpolowane')
    title = metod + ' dla ' + str(n) + ' węzłów'
    pyplot.title(title)
    plt.xlabel('Odległość')
    plt.ylabel('Wysokość [m]')
    plt.legend()
    plt.show()