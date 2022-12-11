# inventories = [
#   [79, 98],
#   [54,65,75,74],
#   [79,60,97],
#   [74]
# ]
# inspect = [0,0,0,0]
# def HandleMoonkey0(item):
#   item *= 19
#   item //= 3
#   if item % 23 == 0:
#     #throw to monkey 3
#     inventories[2].append(item)
#   else:
#     # throw to monkey 2
#     inventories[3].append(item)
# def HandleMoonkey1(item):
#   item += 6
#   item //= 3
#   if item % 19 == 0:
#     #throw to monkey 6
#     inventories[2].append(item)
#   else:
#     # throw to monkey 7
#     inventories[0].append(item)
# def HandleMoonkey2(item):
#   item *= item
#   item //= 3
#   if item % 13 == 0:
#     #throw to monkey 3
#     inventories[1].append(item)
#   else:
#     # throw to monkey 5
#     inventories[3].append(item)
# def HandleMoonkey3(item):
#   item += 3
#   item //= 3
#   if item % 17 == 0:
#     #throw to monkey 4
#     inventories[0].append(item)
#   else:
#     # throw to monkey 5
#     inventories[1].append(item)

# for round in range(20):
#   while(inventories[0]):
#     HandleMoonkey0(inventories[0].pop(0))
#     inspect[0] += 1
#   while(inventories[1]):
#     HandleMoonkey1(inventories[1].pop(0))
#     inspect[1] += 1
#   while(inventories[2]):
#     HandleMoonkey2(inventories[2].pop(0))
#     inspect[2] += 1
#   while(inventories[3]):
#     HandleMoonkey3(inventories[3].pop(0))
#     inspect[3] += 1

#   print('ROUND ' + str(round + 1))
#   for i, inv in enumerate(inventories):
#     print(f'Monkey {i}: {inv}')
# print(inspect)


with open('day11/input.in', "r") as f:
    content = f.read().splitlines()

monkeyOperations = [(content[x][23:]) for x in range(2, len(content), 7)]
monkeyTest = [int(content[x][21:]) for x in range(3, len(content), 7)]
monkeyConditions = [[int(content[x][29:]), int(content[x+1][30:])] for x in range(4, len(content), 7)]

modulo = 1
for i in monkeyTest:
    modulo *= i

def main(part):
    monkeyInspections = [0 for _ in range(len(monkeyTest))]
    monkeyItems = [[[int(x) for x in (content[y][18:]).split(", ")] for y in range(1, len(content), 7)]][0]
    for _ in range(0, (20 if part == 1 else 10000 if part == 2 else 0)):
        for i in range(0, len(monkeyInspections)):
            for j in range(0, len(monkeyItems[i])):
                current = monkeyItems[i][j]
                if monkeyOperations[i] == "* old":
                    current *= current
                elif monkeyOperations[i][:2] == "* ":
                    current *= int(monkeyOperations[i][2:])
                elif monkeyOperations[i][:2] == "+ ":
                    current += int(monkeyOperations[i][2:])
                current = current // 3 if part == 1 else current % modulo
                if current % monkeyTest[i] == 0:
                    monkeyItems[monkeyConditions[i][0]].append(current)
                else:
                    monkeyItems[monkeyConditions[i][1]].append(current)
                monkeyInspections[i] += 1
            monkeyItems[i] = []
    print(monkeyInspections)
    
    return sorted(monkeyInspections)[-1]*sorted(monkeyInspections)[-2]

print("Part 1:", main(1))
print("Part 2:", main(2))
