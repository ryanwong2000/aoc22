def findViewLength(tree, forestLine):
  viewLength = 0
  for t in forestLine:
    viewLength += 1
    if int(t) >= tree:
      return viewLength
  return viewLength

with open('day8/input.in', 'r', encoding="utf-8") as f:
  lines = f.read().split('\n')
  numCols = len(lines[0])
  numRows = len(lines)

  highestScore = 0
  # make a 2d array with the data
  # forest[row][col]
  forest = [list(row) for row in lines]
  for ic in range(numCols):
    for ir in range(numRows):
      currentTree = int(forest[ir][ic])
      north = findViewLength(currentTree, [row[ic] for row in forest][:ir][::-1])
      south = findViewLength(currentTree, [row[ic] for row in forest][ir+1:])
      west = findViewLength(currentTree, forest[ir][:ic][::-1])
      east = findViewLength(currentTree, forest[ir][ic+1:])
      score = north * south * west * east
      if score > highestScore:
        highestScore = score

  print(f'[PART 2] highest view score: {highestScore}')