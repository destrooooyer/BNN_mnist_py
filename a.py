import numpy as np

arr = np.array([784,10])
file = open("weights_loc.txt", 'r')
arr=file.read()
print arr[0]