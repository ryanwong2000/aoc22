with open('day10/input.in', 'r', encoding="utf-8") as f:
  lines = f.read().split('\n')

  Xregister = 1
  count = 0
  Vqueue = [0 * 3]
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
    # print(cycles[x], score)

  print(f'[PART 1] Total score: {totalscore}')
  
  WIDTH = 40
  HEIGHT = 6
  # for ii in range(1,HEIGHT + 1):
  #   for jj in range(1,WIDTH + 1):
  #     print(ii, (ii-1)* WIDTH + jj)

  # test first row
  # for jj in range(22):
  #   print(f'cycle {jj}, pos {jj-1}: {cycles[jj]}, {cycles[jj][1] - 1 <= jj <= cycles[jj][1] + 1}')

  # index = 0
  # for ii in range(1,HEIGHT + 1):
  #   print(ii, end='')
  #   for jj in range(1,WIDTH + 1):
  #     cycle = cycles[index][0]
  #     _X = cycles[index][1]
  #     if _X - 1 <= cycle <= _X + 1:
  #       print('#', end='')
  #     else:
  #       print('.', end='')
  #     index += 1
  #   print()

  print(spritePos[219], spritePos[220])
  for ii, pos in enumerate(spritePos):
    if ii == 0:
      continue
    if pos in range(ii%40-1, ii%40+2):
      print('#', end='')
    else:
      print('.', end='')

    if ii % 40 == 0:
      print()
    # print(cycle)
