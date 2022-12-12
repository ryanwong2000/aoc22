import numpy as np
with open('day12/test.in', 'r', encoding="utf-8") as f:
  data = f.read().split('\n')
  print(data)
  matrix = [list(line) for line in data]
  # matrix = np.asmatrix(matrix)
  x = np.where(matrix == 'S')
  print(x)
