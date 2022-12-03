with open('day3/input.txt', 'r', encoding="utf-8") as f:
  lines = f.readlines()

  letters = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y','z',
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
  priorities = list(range(1,53))

  #dictionary comprehension
  #create a dictionary of 'letter': 'priority' pairs
  res = {letters[i]: priorities[i] for i in range(52)}

  sum1 = 0
  for line in lines:
    first = line[0:(len(line)-1)//2]
    last = line[(len(line)-1)//2:]

    #find the dupe
    for letter in last:
      if(first.find(letter) > -1):
        # print(f'{letter}: {res[letter]}')
        sum1 += res[letter]
        break
  print(f'[PART 1] sum: {sum1}')

