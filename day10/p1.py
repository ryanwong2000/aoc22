with open('day10/input.in', 'r', encoding="utf-8") as f:
  lines = f.read().split('\n')

  Xregister = 1
  count = 0
  Vqueue = [0 * 3]
  cycles = [(count, Xregister)]
  totalscore = 0

  for line in lines:
    # print(line)
    if line.startswith('noop'):
      count += 1
      cycles.append((count, Xregister))
    else:
      addx, V = line.split()
      count += 1
      cycles.append((count, Xregister))
      count += 1
      cycles.append((count, Xregister))
      Xregister += int(V)

  for x in range(20, count, 40):
    score = cycles[x][0] * cycles[x][1]
    totalscore += score
    print(cycles[x], score)
  
  

  print(f'[PART 1] Total score: {totalscore}')
  
