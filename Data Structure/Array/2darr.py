import numpy as np


ab = np.arange(start=1, stop=51).reshape(2, 25)

# print(ab)
# print(ab.shape)
# print(ab[1])
print(ab[1][1])


for pntr in range(10, 25):
    print(ab[0][pntr])
for pntr in range(1, 25):
    print(ab[1][pntr])
