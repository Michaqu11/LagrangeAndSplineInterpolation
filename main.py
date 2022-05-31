from src.methods.LagrangeInterpolatingPolynomial import lagrangeInterpolatingPolynomial
from src.methods.SplineInterpolation import spline_interpolateon
from src.readData import read_data



if __name__ == '__main__':
    files, filesName = read_data()
    n = 10
    for i, file in enumerate(files):
        lagrangeInterpolatingPolynomial(file, n)
        pass

    n = 100
    for i, file in enumerate(files):
        spline_interpolateon(file, n)
        pass