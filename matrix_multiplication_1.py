
import numpy as np
from pprint import pprint


# print(np.array.__dir__())
# pprint(np.array.__dir__())

# robot_cost = np.array([70, 80, 140])
# robots_sold_by_month = np.array([[30, 40, 20], [20, 25, 20], [10, 30, 20]])
# print(f"Cost of all robots for months 1, 2, and 3:   {robots_sold_by_month.dot(robot_cost)}", "\n")
#
"""
a_matrix = np.array([[1, 2, 3, 4, 5, 6],
                    [7, 8, 9, 10, 11, 12],
                    [13, 14, 15, 16, 17, 18],
                    [19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30],
                    [31, 32, 33, 34, 35, 36]])
print("Line 20 a_matrix \n", a_matrix, "\n", "\n")

identity = np.array([[1, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1]])

print("Line 29 identity \n", f"{identity}", "\n", "\n")
print(f"Line 30 identity dot a_matrix \n", identity.dot(a_matrix), "\n", "\n")
print(f"Line 31 a_matrix dot identity \n", a_matrix.dot(identity), "\n", "\n")

rc_matrix = np.array([[0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0]])

print(f"Line 40 rc_matrix dot a_matrix \n", rc_matrix.dot(a_matrix), "\n", "\n")
print(f"Line  41 a_matrix dot rc_matrix \n", a_matrix.dot(rc_matrix), "\n", "\n")

#
# b1 = np.array([[1, 2, 3], [2, 1, 4], [3, 2, 1]])
# b2 = np.array([[3, 4, 5], [4, 1, 2], [1, 1, 1]])
# print(f"Line 44 b1 \n", f"{b1}", "\n", "\n")
# print(f"Line 44 b2 \n", f"{b2}", "\n", "\n")
# print(b1.dot(b2))

# g1 = np.array([1, 2, 3])
# g2 = np.array([[3], [4], [5]])
# print(f"Line 53 g1 \n", f"{g1}", "\n", "\n")
# print(f"Line 54 g2 \n", f"{g2}", "\n", "\n")
# print(f"Line 55 b2 \n", g1.dot(g2))
"""

b1 = np.array([[1, 2, 3], [2, 1, 4], [3, 2, 1]])
b2 = np.array([[3, 4, 5], [4, 1, 2], [1, 1, 1]])
b3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Line 60 matrix b3 \n", f"{b3}", "\n")


first = 3
last = 3
mistery = np.zeros((first, last))
mistery[0][last - 1] = 1

for i in range(last):
    mistery[i][i-1] = 1

print(mistery, "\n")
# print(mistery.dot(b3), "\n")
# print(b3.dot(mistery), "\n")
# print(b3.dot(mistery).dot(mistery), "\n")


