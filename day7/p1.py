from anytree import Node, RenderTree, search, Walker

with open('day7/test.in', 'r', encoding="utf-8") as f:
  commands = f.read().split('\n')
  cdStack = [] # tracks the current cd and its path
  root = Node('', None, type='dir', size=0)
  nodes = {'/': root}
  sumToDelete = 0
  w = Walker()
  # print(commands)
  for line in commands:
    # move up a level by popping the dir off the stack
    if line == '$ cd ..':
      cdStack.pop()

    # move into the dir by pushing to the stack
    elif line.startswith('$ cd'):
      cdStack.append(line[5:])
      # print(cdStack)

    # make new directory
    elif line.startswith('dir'):
      dirName = line[4:]
      # add a node to the dictionary with the dir name as the key and the Node
      # object as the value, and the top of the cdStack as the parent
      nodes[dirName] = Node(dirName, nodes[cdStack[-1]], type='dir', size=0)
      # print(f'new dir: {nodes[dirName]}')

    # ignore
    elif line.startswith('$ ls'):
      continue

    # add new file to directory
    else:
      fsize, fname = line.split(' ')
      nodes[fname] = Node(fname, nodes[cdStack[-1]], type='file', size=int(fsize))

  
  # calculate the size of each dir
  for dir in search.findall(root, filter_=lambda node: node.type == 'dir'):
    files = search.findall(dir, filter_=lambda node: node.type == 'file')
    print(f'chilren of {dir.name}: {files}')
    dir.size = sum(int(f.size) for f in files)
    if(dir.size <= 100000):
      sumToDelete += dir.size
    
  print(RenderTree(root))

  print(f'sumToDelete: {sumToDelete}')
