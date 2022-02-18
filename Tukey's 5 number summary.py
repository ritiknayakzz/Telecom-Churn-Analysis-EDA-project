## This notebook has functions written by the author for 
## Tukey's 5 number summary along with functions for 
## mean, range, standard deviation, variance, 
## mode, and inter quartile range also.

from collections import Counter
import math
import numpy as np

moto = np.random.randn(40)
x = [1,2,5,3,6]
y = [1,2,1,1,3,2,4]
z = [0,100]

def minimum(x):
  mini = x[0]
  for i in x[0:]:
    if i < mini:
      mini = i
  return mini

def maximum(x):
  maxim = x[0]
  for i in x[0:]:
    if i > maxim:
      maxim = i
  return maxim

def mean(x):
    #v = 0
    #for i in x:
     #   v = v + i
    #return v / len(x)

     return sum(x) / len(x)

def median(x):
    sorted_x = sorted(x)
    n = len(x)
    midpoint = n // 2 

    # Modulo operator
    if n % 2 == 1:
        return sorted_x[midpoint]

    else:
        hi = midpoint
        lo = midpoint - 1
        return (sorted_x[hi] + sorted_x[lo]) / 2

# QuickSelect

def quantile(x, p):
    p_index = int(len(x) * p)

    return sorted(x)[p_index]

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]

# Dispersion

def rng(x):
     return max(x) - min(x)

def de_mean(x):
     x_bar = mean(x)
     return [(x_i - x_bar) ** 2 for x_i in x]

def variance(x):
     n = len(x)
     deviations = de_mean(x)
     return sum(deviations) / (n-1)

def standard_dev(x):
     return math.sqrt(variance(x))

def interquartile_range(x):
     return quantile(x, 0.75) - quantile(x, 0.25)
