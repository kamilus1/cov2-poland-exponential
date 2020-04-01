import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



class COV2:
    def __init__(self, intervals=2):
        f = open("cov2.csv", "r")
        file_lines = f.readlines()[1:]
        self.x = np.array([int(line.split(";")[1]) for line in file_lines])
        self.y = np.array([int(line.split(";")[2]) for line in file_lines])
        self.intervals = intervals
    def create_fit_line(self):
        group_size = int(len(self.x)/self.intervals)
        plt.figure()
        plt.plot(self.x, self.y, 'ko', label="COV2 cases in Poland")
        color_step = 0.5/self.intervals
        for i in range(0, (self.intervals-1)):
            x = self.x[i*group_size:(i+1)*group_size+1]
            y = self.y[i*group_size:(i+1)*group_size+1]
            popt, pcov = curve_fit(self.exponential_func, x, y)
            plt.plot(x, self.exponential_func(x, *popt), color=[0.5+i*color_step, 0.2, 0.5+i*color_step],
                     label="fitted curve[exponent base={}]".format(popt[1]))
        x = self.x[(self.intervals-1) * group_size:len(self.x)]
        y = self.y[(self.intervals-1) * group_size:len(self.x)]
        popt, pcov = curve_fit(self.exponential_func, x, y)
        plt.plot(x, self.exponential_func(x, *popt), color=[1, 0.2, 1],
                 label="fitted curve[exponent base={}]".format(popt[1]))
        plt.legend()
        plt.show()
    @classmethod
    def exponential_func(cls, x, a, b, c):
        return a*pow(b, x)+c

if __name__ == '__main__':
    #change intervals setting to get more or less accurate values
    C = COV2(intervals=4)
    C.create_fit_line()
