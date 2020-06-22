import math

def y_model_sigmoidal(x_sum):
    y_model = 1 / (1 + math.exp(- x_sum))
    return y_model
##2-3-1
#        12 to 123 [w01,w02,w03]    [w11, w12, w13]    [w21, w22, w23]
w1x =           [[0.53, 0.1, 0.66],[0.3, 0.32, 0.305],[0.25, 0.26, 0.28]]
#       123 to 1 [w01]  [w11] [w21] [w31]
w2x =           [[0.77],[0.7],[0.4],[0.57]]

x =             [7, 4]
x_sum =         0.
N_neurons_1 =   2
N_neurons_2 =   3
N_neurons_3 =   1
layer1_out =    [0., 0.]
layer2_out =    [0., 0., 0.]
layer3_out =    [0.]
y_output =      [layer1_out,layer2_out,layer3_out]
# принимает сигнал через линейную функцию
for i in range(0, N_neurons_1):
    layer1_out[i] = x[i]
#передает с нейронов 1,2 первого шара на нейроны 1,2,3 второго шара
for i in range (0, N_neurons_2):
    for j in range (0,len(w1x)):
        if j == 0:
            x_sum += 1 * w1x[j][i]
        else:
            x_sum += y_output[0][j-1] * w1x[j][i]
    layer2_out[i] = y_model_sigmoidal(x_sum)
    x_sum = 0
#передает с нейронов второго шара на последний нейрон, 3-го шара, откуда получаем y_model
for i in range (0, N_neurons_3):
    for j in range (0,len(w2x)):
        if j == 0:
            x_sum += 1 * w2x[j][i]
        else:
            x_sum += y_output[1][j-1] * w2x[j][i]
    layer3_out[i] = y_model_sigmoidal(x_sum)
    x_sum = 0

print(y_output)
