with open('day5/input.in', 'r', encoding="utf-8") as f:
  # separate data into two sections
  [crates, instructions] = f.read().split('\n\n')
  
  crates = crates.split('\n')
  instructions = instructions.split('\n')
  
  labels = crates.pop().strip()
  numberOfStacks = int(labels[len(labels)-1])
  print(f'numberOfStacks: {numberOfStacks}')
  print(f'crates: {crates}')
  stacks = []
  for i in range(numberOfStacks):
    stacks.append([])
  # 1 = 1, 2 = 5, 3 = 9 => 4i + 1
  for level in reversed(crates):
    for i in range(numberOfStacks):
      letter = level[4*i + 1]
      if not letter.isspace():
        stacks[i].append(letter)

  # append to the toStack, the top crate from the fromStack
  for order in instructions:
    [move, fromStack, toStack] = order.replace('move', '').replace('from', '').replace('to','').split()
    move = int(move)
    fromStack = int(fromStack) - 1
    toStack = int(toStack) - 1
    for i in range(move):
      stacks[toStack].append(stacks[fromStack].pop())

  
  output = ''
  for stack in stacks:
    output += stack.pop()
  print(f'[PART 1] Top of stacks: {output}')