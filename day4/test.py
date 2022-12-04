def fully_intersect(a, b, c, d):
  if a <= c <= d <= b or c <= a <= b <= d:
    print(f'{a}-{b}, {c}-{d}')
    return True
  return False
  # return a <= c <= d <= b or c <= a <= b <= d
with open('day4/input.in') as f:
  arr = []
  for line in f.readlines():
    group = []
    for interval in line.strip().split(','):
      group.append(list(map(int, interval.split('-'))))
    arr.append(group)
  # print(f'arr {arr}')
  res = 0
  for group in arr:
    a, b = group[0]
    c, d = group[1]
    if fully_intersect(a, b, c, d):
      res += 1
      # print(f'{res}: {a}-{b}, {c}-{d}')
  print('Part 1:', res)