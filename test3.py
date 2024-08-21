from scipy.optimize import linear_sum_assignment
import numpy as np

costM = [[2,5],[2,2],[3,2]]

costM = np.array(costM)
c = np.copy(costM)
print(c)

x,y = linear_sum_assignment(costM)

print(x,y)