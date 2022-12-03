with open('day3/input.txt', 'r', encoding="utf-8") as f:
  lines = f.readlines()

  letters = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y','z',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
  priorities = list(range(1,53))

  #dictionary comprehension
  #create a dictionary of 'letter': 'priority' pairs
  res = {letters[i]: priorities[i] for i in range(52)}

  sum2 = 0
  for i in range(0, len(lines), 3):
    elf1 = lines[i]
    elf2 = lines[i+1]
    elf3 = lines[i+2]
    group = list(set(elf1).intersection(elf2).intersection(elf3))[0]
    sum2 += res[group]
  print(f'[PART 2] sum: {sum2}')