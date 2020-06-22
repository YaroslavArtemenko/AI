import math
import random
import math

def print_res(i, y_model, delt_i, vec_w):
    if i<10:
        print('i = ', i, '  ==== y_model = ', y_model, ' ==== delth = ', round(delt_i,5), 'vec_w = ', vec_w)
    else:
        print('i = ', i, ' ==== y_model = ', round(y_model,8), ' ==== delth = ', round(delt_i,5), 'vec_w = ', vec_w)
# def print_res(i, y_model, delt_i)
#     print('i = ', i, ' ==== y_model = ', round(y_model,5), ' ==== delth = ', round(delt_i,5))
def y_model_sigmoidal(x_sum):
    y_model = 1 / (1 + math.exp(- x_sum))
    return y_model

x_inp =         8.
y_expect =      0.5
vec_w =         [0.398, 0.401]
vec_delt_w =    [0., 0.]

x_test =        2.
y_test =        []
delt_possible = 0.1
delt_i =        1.
i =             1
x_sum =         [0., 0., 0.,]
y_model =       [y_expect, 0., 0.]


while delt_i > delt_possible:
    x_sum[1] = y_model[0] * vec_w[0]
    y_model[1] = y_model_sigmoidal(x_sum[1])

    x_sum[2] = y_model[1] * vec_w[1]
    y_model[2] = y_model_sigmoidal(x_sum[2])

    delt_i =  math.fabs((y_model[2] - y_expect) / y_expect)

    if delt_i <= delt_possible:
        print_res(i, y_model, delt_i, vec_w)
        break
    else:
        ##third neurone correction
        b_3 = y_model[2] * (1 - y_model[2]) * (y_expect - y_model[2])
        vec_delt_w[1] = y_model[1] * b_3

        ##second neurone correction
        b_2 = y_model[1] * (1 - y_model[1]) * (b_3* vec_w[1])
        vec_w[1] += vec_delt_w[1]
        vec_delt_w[0] = x_inp * b_2
        vec_w[0] += vec_delt_w[0]
    print_res(i, y_model, delt_i, vec_w)
    i+=1


############################################################################################################
x_summar_test=[0., 0., 0.]
x_summar_test[1] = x_test * vec_w[0]
y_test.append(y_model_sigmoidal(x_summar_test[1]))
x_summar_test[2] = y_test[0] * vec_w[1]
y_test.append(y_model_sigmoidal(x_summar_test[2]))
print("x_test = ", x_test)
print("y_output = ",y_test[len(y_test)-1])
