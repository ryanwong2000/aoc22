with open('day5/test.in', 'r', encoding="utf-8") as f:
  # separate data into two sections
  [stacks, instructions] = f.read().strip().split('\n\n')
  stacks = stacks.split('\n')
  instructions = instructions.split('\n')
  labels = stacks.pop().strip()
  numberOfStacks = labels[len(labels)-1]
  print(f'numberOfStacks: {numberOfStacks}')
  rows = []
  for i, level in enumerate(stacks):
    rows.append(''.join(level.split()).replace('[','').replace(']',''))
    print(i, level)
  print(rows)
  print(instructions)