data = open('day14/input.in', 'r', encoding="utf-8").read().split('\n')
# each line is a path
paths = [path for path in data]

# make map of
# assign "collisions"
filled = set() # set of coords (x, y) where there can be a collision
# iterate and make the line each path describes by filling from point to point
for path in paths:
  points = []
  # find the points in a line
  for strPoint in path.split(' -> '):
    x, y = map(int, strPoint.split(','))
    points.append((x, y))

  # track which points have been filled
  for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    
    # horizontal line
    if y1 == y2:
      for x in range(min(x1, x2), max(x1, x2) + 1):
        filled.add((x, y1))
    # vertical line
    elif x1 == x2:
      for y in range(min(y1, y2), max(y1, y2) + 1):
        filled.add((x1, y))

deepestY = max([point[1] for point in filled])
floorY = deepestY + 2
print(f'deepest y: {deepestY} and floor: {floorY}')

def sandFalling(x, y):
  if (x, y) in filled:
    return False
  # not in the void
  while y < floorY:
    # check down
    if (x, y+1) not in filled:
      y += 1
    # check down left
    elif (x-1, y+1) not in filled:
      x -= 1
      y += 1
    # check down right
    elif (x+1, y+1) not in filled:
      x += 1
      y += 1
    # stay and fill
    else:
      filled.add((x, y))
      return True
  # place sand on floor
  filled.add((x, floorY-1))
  return True

# simulate
source = (500, 0)
sandCount = 0
while sandFalling(source[0], source[1]):
  sandCount += 1
print(f'[PART 2] There are {sandCount} units of sand that fall before filling up')
