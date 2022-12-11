inventories = [
  [79, 98],
  [54,65,75,74],
  [79,60,97],
  [74]
]
inspect = [0,0,0,0]
def HandleMoonkey0(item):
  item *= 19
  item //= 3
  if item % 23 == 0:
    #throw to monkey 3
    inventories[2].append(item)
  else:
    # throw to monkey 2
    inventories[3].append(item)
def HandleMoonkey1(item):
  item += 6
  item //= 3
  if item % 19 == 0:
    #throw to monkey 6
    inventories[2].append(item)
  else:
    # throw to monkey 7
    inventories[0].append(item)
def HandleMoonkey2(item):
  item *= item
  item //= 3
  if item % 13 == 0:
    #throw to monkey 3
    inventories[1].append(item)
  else:
    # throw to monkey 5
    inventories[3].append(item)
def HandleMoonkey3(item):
  item += 3
  item //= 3
  if item % 17 == 0:
    #throw to monkey 4
    inventories[0].append(item)
  else:
    # throw to monkey 5
    inventories[1].append(item)

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

  print('ROUND ' + str(round + 1))
  for i, inv in enumerate(inventories):
    print(f'Monkey {i}: {inv}')
print(inspect)