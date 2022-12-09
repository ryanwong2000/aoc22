with open('day8/input.in', 'r', encoding="utf-8") as f:
  lines = f.read().split('\n')
  numCols = len(lines[0])
  numRows = len(lines)
  visible = [] # set of coords for trees that are visible in the form (row, col)

  # make a 2d array with the data
  # forest[row][col]
  forest = [list(row) for row in lines]

  # all trees on the edges are visible
  # horizontal edges
  for col in range(numCols):
    visible.append((0, col))
    visible.append((numRows - 1, col))
  # vertical edges (skip the first and last)
  for row in range(1, numRows - 1):
    visible.append((row, 0))
    visible.append((row, numCols - 1))

  # print(f'2*{numRows} x 2*{numCols} - 4 = {len(visible)}')
  # print((0, 0) in visible)
  
  
  # check the north visibility
  for ic in range(1, numCols - 1):
    tallestN = forest[0][ic]
    tallestS = forest[numRows - 1][ic]
    for ir in range(1, numRows - 1):
      irr = numRows - 1 - ir
      if (forest[ir][ic] > tallestN):
        if (ir, ic) not in visible:
          visible.append((ir,ic))
        tallestN = forest[ir][ic]
      if (forest[irr][ic] > tallestS):
        if (irr, ic) not in visible:
          visible.append((irr,ic))
        tallestS = forest[irr][ic]
  # print(len(visible))

  # check east west visibility  
  for ir in range(1, numRows - 1):
    tallestW = forest[ir][0]
    tallestE = forest[ir][numCols - 1]
    for ic in range(1, numCols - 1):
      icc = numCols - 1 - ic
      if (forest[ir][ic] > tallestW):
        if (ir, ic) not in visible:
          visible.append((ir,ic))
        tallestW = forest[ir][ic]
      if (forest[ir][icc] > tallestE):
        if (ir, icc) not in visible:
          visible.append((ir,icc))
        tallestE = forest[ir][icc]


  # for coord in visible:
    # print(coord)
  print(f'[PART 1]: number of visible trees: {len(visible)}')
