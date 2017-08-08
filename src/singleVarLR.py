# #Implementation of Batch Gradient Descent on a single variable linear hypothesis

import xlrd
import numpy
import matplotlib.pyplot as plt


def load_data():
    data_file = xlrd.open_workbook("slr02.xls")
    data_file = data_file.sheet_by_index(0)
    data = {}
    for row in range(data_file.nrows):
        if row > 0:
            data[data_file.cell_value(row, 0)] = data_file.cell_value(row, 1)
    return data


def lin_hypothesis(x, theta0, theta1):
    return theta0 + theta1 * x


def gradient_descent(data, alpha):
    theta0 = 0.0
    theta1 = 0.0
    iterations = 0
    converged = False

    prev_sum = sum([(lin_hypothesis(x, theta0, theta1) - data[x]) ** 2 for x in data.keys()])

    while not converged:
        iterations += 1
        temp0 = 0.0
        temp1 = 0.0
        for x in data.keys():
            temp0 += (lin_hypothesis(x, theta0, theta1) - data[x])
            temp1 += (lin_hypothesis(x, theta0, theta1) - data[x]) * x

        theta0 -= (alpha / (len(data))) * temp0
        theta1 -= (alpha / (len(data))) * temp1

        curr_sum = sum([(theta0 + theta1 * x - data[x]) ** 2 for x in data.keys()])

        if abs(prev_sum - curr_sum) <= .01:
            converged = True
            print "Iterations: ", iterations

        prev_sum = curr_sum

    return theta0, theta1


def main():
    alpha = 0.001
    data = load_data()
    theta0, theta1 = gradient_descent(data, alpha)

    print "theta0", theta0
    print "theta1", theta1

    x = numpy.linspace(10, 25, 100)
    plt.plot(data.keys(), data.values(), 'o', x, theta0 + theta1*x)
    plt.xlabel("Cricket Chirps")
    plt.ylabel("Temperature")
    plt.show()

if __name__ == '__main__':
    main()
