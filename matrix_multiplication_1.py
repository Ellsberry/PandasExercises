
import numpy as np
from pprint import pprint


print(print.__dir__())
pprint(np.array.__dir__())

robot_price = np.array([70, 80, 140])
# robots_sold_by_month = np.array([[30, 20, 10], [40, 25, 30], [10, 30,20]])
robots_sold_by_month = np.array([[30, 40, 20], [20, 25, 20], [10, 30, 20]])
print(f"{robots_sold_by_month.dot(robot_price)}", "\n")
"""

ai = np.array([[1, 2, 3, 4, 5, 6],
               [7, 8, 9, 10, 11, 12],
               [13, 14, 15, 16, 17, 18],
               [19, 20, 21, 22, 23, 24],
               [25, 26, 27, 28, 29, 30],
               [31, 32, 33, 34, 35, 36]])
print(ai, "\n", "\n")

i1 = np.array([[1, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 1]])

print(f"Line 38 i1 {i1}", "\n", "\n")
print(i1.dot(ai), "\n", "\n")

i2 = np.array([[0, 0, 0, 0, 0, 1],
               [0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 0, 0],
               [0, 1, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0]])



print(i2.dot(ai), "\n", "\n")
print(ai.dot(i2), "\n", "\n")

"""