import re


# with open('day11/test.in', 'r', encoding="utf-8") as f:
#   inventories = []
#   monkeys = dict() # {0: { op: new = old * 19, test: 23, true: 2, false: 3 }}

#   data = f.read().split('\n\n')

#   for block in data:
#     lines = block.split('\n')
#     for line in lines:
#       line = line.strip()
#       # print(line)
#       if 'Monkey' in line:
#         iMonkey = line[7]
#       elif 'Starting items:' in line:
#         inventories.append(re.findall(r'\d+', line))
#       elif 'Operation:' in line:
           
inventories = [
  [57],
  [58,93,88,81,72,73,65],
  [65,95],
  [58,80,81,83],
  [58,89,90,96,55],
  [66,73, 87, 58, 62, 67],
  [85, 55, 89],
  [73, 80, 54, 94, 90, 52, 69, 58]
]
inspect = [0,0,0,0,0,0,0,0]
def HandleMoonkey0(item):
  item *= 13
  item //= 3
  if item % 11 == 0:
    #throw to monkey 3
    inventories[3].append(item)
  else:
    # throw to monkey 2
    inventories[2].append(item)
def HandleMoonkey1(item):
  item += 2
  item //= 3
  if item % 7 == 0:
    #throw to monkey 6
    inventories[6].append(item)
  else:
    # throw to monkey 7
    inventories[7].append(item)
def HandleMoonkey2(item):
  item += 6
  item //= 3
  if item % 13 == 0:
    #throw to monkey 3
    inventories[3].append(item)
  else:
    # throw to monkey 5
    inventories[5].append(item)
def HandleMoonkey3(item):
  item *= item
  item //= 3
  if item % 5 == 0:
    #throw to monkey 4
    inventories[4].append(item)
  else:
    # throw to monkey 5
    inventories[5].append(item)
def HandleMoonkey4(item):
  item += 3
  item //= 3
  if item % 3 == 0:
    #throw to monkey 1
    inventories[1].append(item)
  else:
    # throw to monkey 7
    inventories[7].append(item)
def HandleMoonkey5(item):
  item *= 7
  item //= 3
  if item % 17 == 0:
    #throw to monkey 4
    inventories[4].append(item)
  else:
    # throw to monkey 1
    inventories[1].append(item)
def HandleMoonkey6(item):
  item += 4
  item //= 3
  if item % 2 == 0:
    #throw to monkey 2
    inventories[2].append(item)
  else:
    # throw to monkey 0
    inventories[0].append(item)
def HandleMoonkey7(item):
  item += 7
  item //= 3
  if item % 19 == 0:
    #throw to monkey 6
    inventories[6].append(item)
  else:
    # throw to monkey 0
    inventories[0].append(item)

for round in range(20):
  while(inventories[0]):
    HandleMoonkey0(inventories[0].pop(0))
    inspect[0] += 1
  while(inventories[1]):
    HandleMoonkey1(inventories[1].pop(0))
    inspect[1] += 1
  while(inventories[2]):
    HandleMoonkey2(inventories[2].pop(0))
    inspect[2] += 1
  while(inventories[3]):
    HandleMoonkey3(inventories[3].pop(0))
    inspect[3] += 1
  while(inventories[4]):
    HandleMoonkey4(inventories[4].pop(0))
    inspect[4] += 1
  while(inventories[5]):
    HandleMoonkey5(inventories[5].pop(0))
    inspect[5] += 1
  while(inventories[6]):
    HandleMoonkey6(inventories[6].pop(0))
    inspect[6] += 1
  while(inventories[7]):
    HandleMoonkey7(inventories[7].pop(0))
    inspect[7] += 1

  print('ROUND ' + str(round + 1))
  for i, inv in enumerate(inventories):
    print(f'Monkey {i}: {inv}')
print(inspect)