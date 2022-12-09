posTail, posHead = (0, 0), (0, 0)
headQueue = [(0,0)]
tailSet = {(0,0)}

def move(dir, dist):
  global posHead
  p = list(posHead)
  for i in range(dist):
    if(dir == 'R'):
      # move the x coord in the positive direction
      p[0] += 1
    elif(dir == 'L'):
      # move the x coord in the negative direction
      p[0] -= 1
    elif(dir == 'U'):
      # move the y coord in the positive direction
      p[1] += 1
    elif(dir == 'D'):
      # move the y coord in the negative direction
      p[1] -= 1
    posHead = tuple(p)  
    headQueue.append(posHead)
      
    

def tooFar():
  headX, headY = posHead[0], posHead[1]
  tailX, tailY = posTail[0], posTail[1]
  # if on the same axis, check for only linear distance
  if headX == tailX or headY == tailY:
    return abs(headX - tailX) + abs(headY - tailY) > 1

  return abs(headX - tailX) + abs(headY - tailY) > 2 


with open('day9/test.in', 'r', encoding="utf-8") as f:
  # read data
  lines = f.read().split('\n')

  for line in lines:
    direction, distance = line.split(' ')
    move(direction, int(distance))
  print(headQueue)
    