import math
import numpy
def pent(k):
    return int(k*(3*k-1) / 2)


def compute_partitions(n):
    partitions = [1]
    for i in range(1, n+1):
        partitions.append(0)
        for k in range(1, i+1):
            for t in [pent(k), pent(-k)]:
                partitions[i] = partitions[i] + math.floor(((numpy.sign(i-t))+1)/2)*((-1)**(k))*partitions[i-t]
    return partitions

print(compute_partitions(5))