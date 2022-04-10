import numpy as np

ex = np.array([1,2,3,4,5,6,7,8,9,10,11])
print(ex.shape)

ex2=ex[np.newaxis]
print(ex2.shape)
print(ex2)

ex3=ex[:,np.newaxis]
print(ex3.shape)
print(ex3)

ex4 = np.expand_dims(ex, axis=2)
print(ex4.shape)
print(ex4)