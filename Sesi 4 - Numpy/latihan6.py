import numpy as np

a1=np.array([[1,1],[2,2]])
a2=np.array([[3,3],[4,4]])

print(np.vstack((a1,a2)))
print(np.hstack((a1,a2)))

x1=np.array(range(1, 24+1))
x2=np.hsplit(x1,4)
x3=x1.view()

print(x1)
print(x2)
print(x3)
