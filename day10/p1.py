with open('day10/input.in', 'r', encoding="utf-8") as f:
  lines = f.read().split('\n')

  Xregister = 1
  count = 0
  cycles = [(count, Xregister)]
  spritePos = []
  totalscore = 0

  for line in lines:
    # print(line)
    if line.startswith('noop'):
      count += 1
      cycles.append((count, Xregister))
      spritePos.append(Xregister)
    else:
      addx, V = line.split()
      count += 1
      cycles.append((count, Xregister))
      spritePos.append(Xregister)
      count += 1
      cycles.append((count, Xregister))
      spritePos.append(Xregister)
      Xregister += int(V)

  for x in range(20, count, 40):
    score = cycles[x][0] * cycles[x][1]
    totalscore += score

  print(f'[PART 1] Total score: {totalscore}')
  
  WIDTH = 40
  HEIGHT = 6

  print(spritePos[219], spritePos[220])

  print('[PART 2] ')
  for ii, pos in enumerate(spritePos):
    if pos in range(ii%40-1, ii%40+2):
      print('#', end='')
    else:
      print(' ', end='')

    if (ii + 1) % 40 == 0:
      print()
    # print(cycle)
