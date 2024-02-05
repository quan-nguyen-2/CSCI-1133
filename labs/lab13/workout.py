import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rotation_mt(theta):
    return np.array([math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)])
square_rotate = np.loadtxt('square.txt')
plt.scatter(square_rotate[0], square_rotate[1])
plt.show()

rot = rotation_mtx(math.pi / 4)
sq_rot = rot @ square_rotate
plt.scatter(sq_rot[0], sq_rot[1])
plt.show()
