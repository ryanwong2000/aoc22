n lines:
    if line.startswith('noop'):
      cycles += 1
      cycleCount.append((cycles, Xregister))
    else:
      addx, V = line.split()
      count = int(V)
      cycles += 1
      cycleCount.append((cycles, Xregister))
      cycles += 1
      Xregister += 1
      cycleCount.append((cycles, Xregister))
      
  print(cycleCount)