import numpy as np

# a = [ 2, 4, 8 ]
# print(a)
# print(a*2)
b = np.array([
    [
        [3, 5, 11],
        [99, 2, 3],
        [6, 2, 1]
    ],
    [
        [3, 5, 11],
        [1, 2, 3],
        [6, 2, 1]
    ],
])
#print(np.shape(b))
#                                     2   1
#             0   1   2   3   4   5   6   7
#b = np.array([ 10, 20, 30, 40, 50, 60, 70, 80])
#print(b[0, 1, 0])

# a = np.array([230, 10, 284, 39, 76])
# cutoff = 200
# print(a)
# a[a > cutoff] = 0
# print(a)
#np.array([True, False, True, False, False])

a = np.array([
    [1, 2],
    [2, 4],
    [3, 8]
    ]
    )
b = np.array([10, 0.5])

print(a*b)

