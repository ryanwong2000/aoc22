with open('day10/input.in', 'r', encoding="utf-8") as f:
  lines = f.readlines()
  
  cycle_values = [1]

  for command in lines:
    if command.startswith("a"):
      for i in range(2):
        if i == 0:
          cycle_values.append(cycle_values[-1])
        if i == 1:
          cycle_values.append(cycle_values[-1] + int(command.split()[1]))
    elif command.startswith("n"):
      cycle_values.append(cycle_values[-1])
  
  output = ""
  for i, value in enumerate(cycle_values):
    if cycle_values[i] in range((i % 40) - 1, (i % 40) + 2):
      output += "#"
    else:
      output += " "
    if (i + 1) % 40 == 0:
      output += "\n"
    
  print(output)
  ##################################################################################################
  Xregister = 1
  count = 1
  Vqueue = [0 * 3]
  # cycles = [(count, Xregister)]
  spritePos = []
  totalscore = 0

  for line in lines:
    # print(line)
    if line.startswith('noop'):
      spritePos.append(Xregister)
      count += 1
      # cycles.append((count, Xregister))
    else:
      addx, V = line.split()
      spritePos.append(Xregister)
      count += 1
      # cycles.append((count, Xregister))
      spritePos.append(Xregister)
      count += 1
      # cycles.append((count, Xregister))
      Xregister += int(V)
  

  ###################################################
  print(len(spritePos),len(cycle_values))

  # for i in range(len(spritePos)):
  #   print(spritePos[i], cycle_values[i])
  # print(spritePos[0], cycle_values[0])
  # print(spritePos[-1], cycle_values[-1])
  for ii, pos in enumerate(spritePos):
    # if ii == 0:
    #   continue
    if pos in range(ii%40-1, ii%40+2):
      print('#', end='')
    else:
      print(' ', end='')

    if ii % 40 == 0:
      print()
  