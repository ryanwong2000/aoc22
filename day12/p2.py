# import numpy as np

def canDescend(current, dest):
  if current == 'S':
    current = 'a' # S shares the lowest elevation as a
  if dest == 'E':
    dest = 'z' # E shares the highest elevation as z
  # print(ord(current), current, dest)
  return ord(current) >= ord(dest)-1

with open('day12/input.in', 'r', encoding="utf-8") as f:
  data = f.read().split('\n')
  # print(data)
  matrix = [list(line) for line in data]
  # print(matrix)

  numRows = len(matrix)
  numCols = len(matrix[0])
  # print(numRows, numCols)

  starts = []
  # find the Start and End coords as (row, col)
  for iLine, line in enumerate(matrix):
    for iEl, el in enumerate(line):
      if el == 'S' or el == 'a':
        starts.append((iLine, iEl))
      if el == 'E':
        endCoords = (iLine, iEl)
  print(endCoords)
  print(len(starts))

  bestSpot = starts[0]
  shortestPath = float('inf')
  for startCoords in starts:
    # matrix to track coords we visit
    visited = [[ False for _ in range(numCols) ] for _ in range(numRows)]
    visited[startCoords[0]][startCoords[1]] = True # set starting coordinates to True
    # queue to track the cells that need to be explored
    toExplore = [startCoords] # start with starting coords

    nextLayerCount = 0 # (havent found the next layer yet)
    leftInLayer = 1 # (the starting cell)
    moveCount = 0

    # define direction vectors
    #      N  E  W  S
    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]

    reachedEnd = False

    # keep finding the adjacents until we run out of cells to visit
    while toExplore:
      currentCoords = toExplore.pop(0)
      # print(currentCoords)
      # check if we reached the end
      if currentCoords == endCoords:
        reachedEnd = True
        break
      currentR, currentC = currentCoords
      # -- GET ADJACENT CELLS --
      # go through each dir vector
      for i in range(4):
        rr = currentR + dr[i]
        cc = currentC + dc[i]

        # check out of bounds
        if rr < 0 or cc < 0 or rr > numRows-1 or cc > numCols-1:
          continue
        # check if already visited
        if visited[rr][cc]:
          continue
        # check if the next one is higher
        # print('current', currentR, currentC)
        if not canDescend(matrix[currentR][currentC], matrix[rr][cc]):
          continue
        # add to queue
        toExplore.append((rr, cc))
        visited[rr][cc] = True
        nextLayerCount += 1
      # -- GET ADJACENT CELLS --
      
      leftInLayer -= 1
      if leftInLayer == 0:
        leftInLayer = nextLayerCount
        nextLayerCount = 0
        moveCount += 1
        # print(moveCount, matrix[currentR][currentC])
    
    if reachedEnd and moveCount < shortestPath:
      shortestPath = moveCount
      bestSpot = startCoords
      print(f'[PART 2] Least number of moves to reach E from {bestSpot}: {shortestPath}')

  
  # print(f'[PART 2] Least number of moves to reach E from {bestSpot}: {shortestPath}')