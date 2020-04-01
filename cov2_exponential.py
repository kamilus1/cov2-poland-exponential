import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



class COV2:
    def __init__(self, intervals=2, choose = 1):
        f = open("cov2.csv", "r")
        file_lines = f.readlines()[1:]
        self.x = np.array([int(line.split(";")[1]) for line in file_lines])
        self.y = np.array([int(line.split(";")[2]) for line in file_lines])
        self.intervals = intervals
        self.choose = choose
    def create_fit_line(self):
        group_size = int(len(self.x)/self.intervals)
        plt.figure()
        plt.plot(self.x, self.y, 'ko', label="COV2 cases in Poland")
        color_step = 0.5/self.intervals
        for i in range(0, (self.intervals-1)):
            x = self.x[i*group_size:(i+1)*group_size+1]
            y = self.y[i*group_size:(i+1)*group_size+1]
            popt, pcov = curve_fit(self.func, x, y)
            plt.plot(x, self.func(x, *popt), color=[0.5+i*color_step, 0.2, 0.5+i*color_step],
                     label="a:{}, b:{}, c:{}".format(popt[0], popt[1], popt[2]))
        x = self.x[(self.intervals-1) * group_size:len(self.x)]
        y = self.y[(self.intervals-1) * group_size:len(self.x)]
        popt, pcov = curve_fit(self.func, x, y)
        print(popt)
        plt.plot(x, self.func(x, *popt), color=[1, 0.2, 1],
                 label="a:{}, b:{}, c:{}".format(popt[0], popt[1], popt[2]))
        plt.legend()
        plt.show()
    def func(self, x, a, b, c):
        if self.choose == 1:
            return self.exponential_func(x, a, b, c)
        elif self.choose  == 2:
            return self.quadratic_func(x, a, b, c)
        elif self.choose  == 3:
            return self.poly_func(x, a, b, c)
        elif self.choose  == 4:
            return self.linear_func(x, a, b, c)

    @classmethod
    def exponential_func(cls, x, a, b, c):
        return a*pow(b, x)+c
    @classmethod
    def quadratic_func(cls, x, a, b, c):
        return a*pow(x, 2) + b*x + c
    @classmethod
    def poly_func(cls, x, a, b, c):
        return a*pow(x, b) + c
    @classmethod
    def linear_func(cls, x, a, b, c):
        return a*x + b + c
if __name__ == '__main__':
    #change intervals setting to get more or less accurate values
    C = COV2(intervals=2, choose=2)
    C.create_fit_line()
