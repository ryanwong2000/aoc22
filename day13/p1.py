import ast
def compareInts(a, b):
  if a < b:
    return 'yes'
  elif a > b:
    return 'no'
  else:
    return 'cont'
def compareValues(a, b):
  # both values are integers
  if isinstance(a, int) and isinstance(b, int):
    return compareInts(a, b)
  # both values are lists
  if isinstance(a, list) and isinstance(b, list):
    for i in range(min(len(a), len(b))):
      checkRes = compareValues(a[i], b[i])
      if checkRes == 'cont':
        continue
      return checkRes # either 'yes' or 'no'
    
    if len(a) == len(b):
      return 'cont'
    return 'yes' if len(a) < len(b) else 'no'
  # left value is int and right value is list
  if isinstance(a, int) and isinstance(b, list):
    return compareValues([a], b)
  # left value is list and right value is int
  if isinstance(a, list) and isinstance(b, int):
    return compareValues(a, [b])
  

data = open('day13/input.in', 'r', encoding="utf-8").read().split('\n\n')

indices = 0
for i, pair in enumerate(data):
  left, right = pair.split('\n')
  left = ast.literal_eval(left)
  right = ast.literal_eval(right)

  # print(left)
  # print(right)
  # print('res',i+1, compareValues(left, right))
  # print()

  if compareValues(left, right) == 'yes':
    # print(i+1)
    indices += i + 1

print(f'[PART 1] Sum of valid indices is {indices}')