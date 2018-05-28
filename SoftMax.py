x = [1, 2, 3]
y = [2, 5, 10]
theta = 5
step_size = 0.01
for i in range(3):
    pred_y = theta * x[i] ** 2 + 1
    theta = theta - step_size * 2 * (pred_y - y[i]) * x[i] ** 2
    print("theta=", theta)

import numpy as np

pred_y = []
for i in range(3):
    pred_y.append(theta * x[i] ** 2 + 1)

pred_y = np.array(pred_y)
y = np.array(y)

theta = theta - step_size * 2 / 3 * np.dot((pred_y - y), np.square(x))
print("theta=", theta)

import numpy as np
import random

x = [1, 2, 3]
y = [2, 5, 10]
theta = 5
step_size = 0.01
max_iters = 20
iter_count = 0

while iter_count < max_iters:
    i = random.randint(0, 2)
    pred_y = theta * x[i] ** 2 + 1
    theta = theta - step_size * 2 * (pred_y - y[i]) * x[i] ** 2
    iter_count += 1
    print("iter_count=%d,theta=%f" % (iter_count, theta))

while iter_count < max_iters:
    pred_y = []
    for i in range(3):
        pred_y.append(theta * x[i] ** 2 + 1)

    pred_y = np.array(pred_y)
    y = np.array(y)

    theta = theta - step_size * 2 / 3 * np.dot((pred_y - y), np.square(x))
    iter_count += 1
    print("iter_count=%d,theta=%f" % (iter_count, theta))