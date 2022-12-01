
with open('day1\calories.txt', 'r', encoding="utf-8") as f:
  lines = f.readlines()
  calories = 0
  highest = -1
  chonks = []
  elf = 1
  fattestElf = 1
  for line in lines:
    if line.strip():
      calories += int(line.strip())
    else:
      # print(f'elf {elf}; sum: {sum}')
      if calories > highest:
        highest = calories
        fattestElf = elf
        print(f'elf {elf}; highest: {highest}')
        if len(chonks) == 3:
          chonks.pop(0)
        chonks.append((elf, highest))
      calories = 0
      elf += 1

  print(chonks)
  
  print(f'[PART 1] HIGHEST: {fattestElf}; CALORIES: {highest}')
  print(f'[PART 2] {sum(j for i, j in chonks)}')
      

print('------------------------------------------')
