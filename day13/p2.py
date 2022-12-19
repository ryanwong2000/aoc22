import ast

def intCompare(a, b):
  if a < b:
    return 'yes'
  elif a > b:
    return 'no'
  else:
    return 'cont'
def listCompare(a, b):
  for i in range(min(len(a), len(b))):
    checkRes = isOrdered(a[i], b[i])
    if checkRes == 'cont':
      continue
    return checkRes # either 'yes' or 'no'

  # made it through one of the lists, check which
  if len(a) == len(b):
    return 'cont'
  return 'yes' if len(a) < len(b) else 'no'

def isOrdered(a, b):
  # both values are integers
  if isinstance(a, int) and isinstance(b, int):
    return intCompare(a, b)
  # both values are lists
  if isinstance(a, list) and isinstance(b, list):
    return listCompare(a, b)
  # left value is int and right value is list
  if isinstance(a, int) and isinstance(b, list):
    return isOrdered([a], b)
  # left value is list and right value is int
  if isinstance(a, list) and isinstance(b, int):
    return isOrdered(a, [b])

def heapifyPackets(packets, nn, iRoot):
  largest = iRoot # init  largest as the root
  left = 2 * iRoot + 1
  right = 2 * iRoot + 2

  # check if left child is larger than root
  if left < nn and isOrdered(packets[left], packets[largest]) == 'no':
    largest = left
  
  # check if right child is larger than root
  if right < nn and isOrdered(packets[right], packets[largest]) == 'no':
    largest  = right

  # if the  largest is not the root, swap
  if largest != iRoot:
    packets[iRoot], packets[largest] = packets[largest], packets[iRoot]
    # heapify the new root
    heapifyPackets(packets, nn, largest)
  
def heapSortPackets(packets):
  n = len(packets)

  # Build min heap
  for i in range(n//2 - 1, -1 , -1):
    heapifyPackets(packets, n, i)

  # extract the element one by one
  for i in range(n-1, 0, -1):
    packets[i], packets[0] = packets[0], packets[i]
    heapifyPackets(packets, i, 0)
  
data = open('day13/input.in', 'r', encoding="utf-8").read().split('\n')
lines = list(filter(lambda x: x != '', data))
packets = list(map(ast.literal_eval, lines))

# add the divider packets
packets.append([[2]])
packets.append([[6]])

heapSortPackets(packets)

i2, i6 = 0, 0
for i, packet in enumerate(packets):
  if packet == [[2]]:
    i2 = i+1
  elif packet == [[6]]: 
    i6 = i+1
    break

print(f'[PART 2] the decoder key is {i2} * {i6} = {i2 * i6}')