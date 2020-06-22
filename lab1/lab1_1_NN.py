import math
import random


#def print_res(i, y_model, delt_i, vec_w):
    #if i<10:
        #print('i = ', i, '  ==== y_model = ', round(y_model,8), ' ==== delth = ', round(delt_i,5), 'vec_w = ', vec_w)
    # else:
    #     print('i = ', i, ' ==== y_model = ', round(y_model,8), ' ==== delth = ', round(delt_i,5), 'vec_w = ', vec_w)
# def print_res(i, y_model, delt_i)
#     print('i = ', i, ' ==== y_model = ', round(y_model,5), ' ==== delth = ', round(delt_i,5))

# def y_model_sigmoidal(x_sum):
#     y_model = 1 / (1 + math.exp(- x_sum))
#     return y_model

x = [1.,7.,4.,5.]
y_expect = 0.3
w = [1, 0.4, 0.7, 0.3]

vec_delt_w = [0., 0., 0., 0.]

x_test = [2., 4., 1., 7.]
y_test = []
delt_possible = 0.1
delt_i = 1.
b_i = 0
i = 1


while delt_i > delt_possible:
    x_sum = 0.
    for p in range(0, len(x)):
        x_sum += x[p] * w[p]

    y_model = 1 / (1 + math.exp(- x_sum))

    delt_i =  math.fabs((y_model - y_expect) / y_expect)

    if delt_i <= delt_possible:
        print('i = ', i, '  ==== y_model = ', round(y_model,8), ' ==== delth = ', round(delt_i,5), 'vec_w = ', w)
        break
    else:
        b_i = y_model * (1 - y_model) * (y_expect - y_model)
        for j in range(0, len(vec_delt_w)):
            vec_delt_w[j] = x[j] * b_i
        for k in range(0, len(w)):
            w[k] = w[k] + vec_delt_w[k]
    print('i = ', i, '  ==== y_model = ', round(y_model,8), ' ==== delth = ', round(delt_i,5), 'vec_w = ', w)
    i+=1


x_sum = 0
for i in range(0, len(w)):
    x_sum += x[i] * w[i]

y_model = 1 / (1 + math.exp(- x_sum))
y_test.append(w[i] * x_test[i])


print("x_test = ", x_test)
print("y_test = ", y_test)
