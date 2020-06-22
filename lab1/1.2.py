import math

x = 0.5
y = 0.5
w = [0.4, 0.7]

delt_w = [0., 0.]

delta_dop = 0.1
delt_i = 1.

count = 1

x_sum = [0., 0., 0.,]
y_model = [x, 0., 0.]

while delt_i > delta_dop:
    x_sum[1] = y_model[0] * w[0]

    y_model[1] = 1 / (1 + math.exp(- x_sum[1]))
    x_sum[2] = y_model[1] * w[1]

    y_model[2] = 1 / (1 + math.exp(- x_sum[2]))

    delt_i = math.fabs((y_model[2] - y) / y)

    if delt_i < delta_dop:
        print("i = ", count, "|  y_model = ", y_model, "|  DELTA = ", round(delt_i, 3))
        break
    else:
        b_3 = y_model[2] * (1 - y_model[2]) * (y - y_model[2])
        delt_w[1] = y_model[1] * b_3
        w[1] = w[1] + delt_w[1]

        b_2 = y_model[1] * (1 - y_model[1]) * b_3 * w[1]
        delt_w[0] = x * b_2
        w[0] = w[1] + delt_w[0]
    print("i = ", count, "|  y_model = ", y_model, "|  DELTA = ", round(delt_i, 3))

    count += 1




# x_test = 5.
# y_test = []
# x_summa = [0., 0., 0.,]
# x_summa[1] = x_test * w[0]
# y_test.append(1 / (1 + math.exp(- x_summa[1])))
# x_summa[2] = y_test[0] * w[1]
# y_test.append((1 / (1 + math.exp(- x_summa[2]))))
#
# print('\n\nx_test = ', x_test)
# print("y_test = ",y_test[len(y_test)-1])
