from math import exp
from random import uniform

delte = 0.001

count_of_neurons = [2, 3, 1]

ww = []

class Neuron_I:   #vhodnoj nejron
    def __init__(self, number):
        self.n = number

    def activation(self):
        self.y = self.y * 1

    def training(self, x):
        self.y = x[self.n]
        self.activation()
        return self.y


class Neuron_M:  #spryatannie nejrony
    def __init__(self, counr, i):
        self.i = i
        # w = [[-0.1, 0.1, 0.2], [-0.2, 0.5, 0.3], [-0.1, 0.1, 0.2]]
        w = []
        for i in range(counr + 1):
            w.append(uniform(-1, 1))
        self.w = w


    def sumo(self):
        sums = 0
        for i in range(len(self.x)):
            sums += float(self.x[i]) * self.w[i]
        self.y = sums
        ww.append(self.w)

    def activation(self):
        self.y = 1 / (1 + exp(-1 * self.y))

    def correction(self): #schitaem deltu(obratnij prohod)
        dop = neuron_3_1.beck()
        sigma = self.y * (1 - self.y) * dop[self.i]
        # sigma = sig
        delta_w = []
        for i in range(len(self.x)):
            delta_w.append(self.x[i] * sigma * 0.01)
            self.w[i] = self.w[i] + delta_w[i]

    def training(self, x):
        self.x = x
        self.sumo()
        self.activation()
        return self.y


class Neuron_U: #vihodnoj nejron
    def __init__(self, counr):
        # w = [0.5, 0.1, -0.1, 0.2]
        w = []
        for i in range(counr + 1):
            w.append(uniform(-1, 1))
        self.w = w

    def sumo(self):
        sums = 0
        for i in range(len(self.x)):
            sums += float(self.x[i]) * self.w[i]
        self.y = sums
        ww.append(self.w)

    def activation(self):
        self.y = 1 / (1 + exp(-1 * self.y))

    def mistake(self): #pogreshnost
        self.delta = abs((self.y - y) / y)
        return self.delta

    def correction(self): #schitam sigmu
        sigma = self.y * (1 - self.y) * (y - self.y)
        delta_w = []
        for i in range(len(self.x)):
            delta_w.append(self.x[i] * sigma * 0.01)
            self.w[i] = self.w[i] + delta_w[i]

    def training(self, x):
        self.x = x
        self.sumo()
        self.activation()
        # self.mistake()
        print("Y - " + str(self.y))
        return self.y

    def beck(self): #ispolzuetsa v spryatannom nejrone, schitaem tut,potomu schto zavisit ot vihodnogo nejrona
        res = []
        sigma = self.y * (1 - self.y) * (y - self.y)
        for i in range(3):
            res.append(sigma * self.w[i])
        return res


neuron_1_1 = Neuron_I(0) #vhodnie 2
neuron_1_2 = Neuron_I(1)
neuron_2_1 = Neuron_M(2, 0) #3 spryatannih
neuron_2_2 = Neuron_M(2, 1)
neuron_2_3 = Neuron_M(2, 2)
neuron_3_1 = Neuron_U(3) #vihodnoj

x = [[3, 4], [9, 11], [21, 29], [25, 35]]  #nashi uchebnie primeri


for i in range(500000):  #uchim nejronku
    ww = []
    print("Епоха " + str(i + 1))
    for j in range(4):
        y1 = [1]
        y2 = [1]
        y3 = []
        y = (x[j][0] + x[j][1]) / 100   #obchisluvane
        print("Итерация " + str(j + 1))
        y1.append(neuron_1_1.training(x[j]))  #vkluchaem training
        y1.append(neuron_1_2.training(x[j]))
        y2.append(neuron_2_1.training(y1))
        y2.append(neuron_2_2.training(y1))
        y2.append(neuron_2_3.training(y1))
        y3.append(neuron_3_1.training(y2))
        neuron_3_1.correction()  #correction
        neuron_2_1.correction()
        neuron_2_2.correction()
        neuron_2_3.correction()



print("\n\nТестування")
x = [[23, 29]]
y = (x[0][0] + x[0][1]) / 100
y1 = [1]
y2 = [1]
y3 = []
ww = []
y1.append(neuron_1_1.training(x[0]))    #correction ne nuzhna, potomu chto uzhe nejronka nauchennaya
y1.append(neuron_1_2.training(x[0]))
y2.append(neuron_2_1.training(y1))
y2.append(neuron_2_2.training(y1))
y2.append(neuron_2_3.training(y1))
y3.append(neuron_3_1.training(y2))

print(ww)

