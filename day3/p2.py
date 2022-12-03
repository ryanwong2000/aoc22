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
    # we remove the \n at the end of each line cause they would be common
    elf1 = lines[i].strip('\n')
    elf2 = lines[i+1].strip('\n')
    elf3 = lines[i+2].strip('\n')
    # converts the strings (as lists) to sets to do the intersection
    # and then goes back to a list where we take the first (only) element
    group = list(set(elf1) & set(elf2) & set(elf3))[0]
    
    sum2 += res[group]
  print(f'[PART 2] sum: {sum2}')