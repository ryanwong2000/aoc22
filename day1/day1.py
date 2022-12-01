
with open('day1\calories.txt', 'r', encoding="utf-8") as f:
  lines = f.readlines()
  sum = 0
  highest = -1
  elf = 1
  fattestElf = 1
  for line in lines:
    if line.strip():
      sum += int(line.strip())
    else:
      print(f'elf {elf}; sum: {sum}')
      if sum > highest:
        highest = sum
        fattestElf = elf
        print(f'elf {elf}; highest: {highest}')
      sum = 0
      elf += 1
  
  print(f'HIGHEST: {fattestElf}; CALORIES: {highest}')
      

print('------------------------------------------')
