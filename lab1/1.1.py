import math


x = [1.,7.,4.,5.]
y = 0.3
w = [0.02, -0.1, 0.5, 0.035]

delt_w = [0., 0., 0., 0.]

delta_dop = 0.1
delt_i = 1.
b_i = 0
count = 1

while delt_i > delta_dop:
    x_sum = 0
    for i in range(0, len(x)):
        x_sum += x[i] * w[i]

    y_model = 1 / (1 + math.exp(- x_sum))

    delt_i = math.fabs((y_model - y) / y)

    if delt_i < delta_dop:
        print("i = ", count, "|  y_model = ", round(y_model, 5), "|  DELTA = ", round(delt_i, 3))
        break
    else:
        b_i = y_model * (1 - y_model) * (y - y_model)
        for j in range(0, len(delt_w)):
            delt_w[j] = x[j] * b_i
        for k in range(0, len(w)):
            w[k] = w[k] + delt_w[k]
    print("i = ", count, "|  y_model = ", round(y_model, 5), "|  DELTA = ", round(delt_i, 3))
    count += 1




# x_test = [1., 4., 3., 8.]
# y_test = []
# x_sum = 0
#
# for i in range(0, len(w)):
#     x_sum += x[i] * w[i]
# y_model = 1 / (1 + math.exp(- x_sum))
# y_test.append(w[i] * x_test[i])
#
# print("\n\nx_test = ", x_test)
# print("y_test = ", y_test)