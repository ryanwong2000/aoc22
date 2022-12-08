from anytree import Node, RenderTree, search, Walker

def getPath(cdStack):
  return '/'.join(cdStack)


with open('day7/input.in', 'r', encoding="utf-8") as f:
  commands = f.read().split('\n')
  cdStack = [] # tracks the current cd and its path
  root = Node('~', None, type='dir', size=0)

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
      # add a node to the dictionary with the dir path as the key and the Node
      # object as the value, and the top of the cdStack as the parent
      parentPath = getPath(cdStack)
      dpath = parentPath + '/' + dirName
      nodes[dpath] = Node(dirName, nodes[parentPath], type='dir', size=0)
      # print(f'new dir: {nodes[dpath]}')

    # ignore
    elif line.startswith('$ ls'):
      continue

    # add new file to directory
    else:
      fsize, fname = line.split(' ')
      parentPath = getPath(cdStack)
      fpath = parentPath + '/' + fname
      nodes[fpath] = Node(fname, nodes[parentPath], type='file', size=int(fsize))


  
  sumToDelete2 = float('inf')
  
  # calculate the size of each dir
  for dir in search.findall(root, filter_=lambda node: node.type == 'dir'):
    files = search.findall(dir, filter_=lambda node: node.type == 'file')
    # print(f'chilren of {dir.name}: {files}')
    dir.size = sum(int(f.size) for f in files)
    if(dir.size <= 100000):
      sumToDelete += dir.size
      
    TOTAL_DISK_SPACE = 70000000
    SPACE_NEEDED = 30000000
    SPACE_USED = nodes['/'].size
    SPACE_AVAILABLE = TOTAL_DISK_SPACE - SPACE_USED
    SPACE_TO_FREE = SPACE_NEEDED - SPACE_AVAILABLE
    print (SPACE_NEEDED, SPACE_AVAILABLE, SPACE_TO_FREE)
    if(dir.size < sumToDelete2 and dir.size > SPACE_TO_FREE):
      sumToDelete2 = dir.size
    
    

  # print(RenderTree(root))

  print(f'[PART 1]: sumToDelete: {sumToDelete}')
  print(f'[PART 2]: sumToDelete: {sumToDelete2}')
