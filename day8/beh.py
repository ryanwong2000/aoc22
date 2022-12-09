def findViewLength(tree, forestLine):
  viewLength = 0
  for t in forestLine:
    viewLength += 1
    if int(t) >= tree:
      print(t)
      return viewLength
  return viewLength

with open('day8/test.in', 'r', encoding="utf-8") as f:
  lines = f.read().split('\n')
  numCols = len(lines[0])
  numRows = len(lines)

  highestScore = 0
  # make a 2d array with the data
  # forest[row][col]
  forest = [list(row) for row in lines]

  currentTree = 9
  ir, ic = 5, 9
  north = findViewLength(currentTree, [row[ic] for row in forest][:ir][::-1])
  south = findViewLength(currentTree, [row[ic] for row in forest][ir+1:])
  west = findViewLength(currentTree, forest[ir][:ic][::-1])
  east = findViewLength(currentTree, forest[ir][ic+1:])
  score = north * south * east * west
  print(north, south, east, west)
  print(score)
  print(forest[5][9])
  print([row[ic] for row in forest][:ir][::-1])
  print([row[ic] for row in forest][ir+1:])
  print(forest[ir][:ic][::-1])
  print(forest[ir][ic+1:])