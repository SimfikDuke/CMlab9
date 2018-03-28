from numpy import linalg as la
import numpy as np

class det(object):
    def __init__(self, array, smesh=False):
        self.a = np.array(array, dtype=float)
        self.n = len(array)
        self.c = la.norm(self.a)
        if smesh: self.a = self.a - np.dot(self.c, np.eye(self.n))
        self.xk = [i/(self.n-1) for i in range(self.n)]
        self.xk1 = self.xk
        self.normxk = la.norm(self.xk)
        self.lk = 0.0
        self.lk1 = 0.0
        self.yk = self.xk
        self.eps = 1e10
        self.smesh = smesh

    def calc(self):
        self.lk = self.lk1
        self.xk = self.xk1
        self.xk1 = np.dot(self.a, self.yk)
        self.lk1 = np.dot(self.xk1, self.yk) / np.dot(self.yk, self.yk)
        self.normxk = la.norm(self.xk1)
        self.yk = self.xk1/self.normxk
        self.eps = abs(self.lk1 - self.lk)
    def epscals(self, eps):
        print("(0)\n" + str(self))
        i = 1
        while self.eps > eps:
            self.calc()
            print("("+str(i)+")\n" + str(self))
            i+=1
        if self.smesh:
            print("Minimalnoe sobstvennoe znachenie =")
            print(self.c + self.lk1)
        else:
            print("Maximalnoe sobstvennoe znachenie =")
            print(self.lk1)


    def __str__(self):
        return "xk = " + str(self.xk1) +\
        "\nlk = " + str(self.lk1) +\
        "\nyk = " + str(self.yk) + \
        "\neps = " + str(self.eps) + "\n"