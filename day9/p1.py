posTail, posHead = (0, 0), (0, 0)
headQueue = [(0,0)]
tailSet = {(0,0)}

def move(dir, dist):
  global posHead
  # p = list(posHead)
  for i in range(dist):
    if(dir == 'R'):
      # move the x coord in the positive direction
      posHead = (posHead[0] + 1, posHead[1])
    elif(dir == 'L'):
      # move the x coord in the negative direction
      posHead = (posHead[0] - 1, posHead[1])
    elif(dir == 'U'):
      # move the y coord in the positive direction
      posHead = (posHead[0], posHead[1] + 1)
    elif(dir == 'D'):
      # move the y coord in the negative direction
      posHead = (posHead[0], posHead[1] - 1)
    checkTail()
    headQueue.append(posHead)
      
def checkTail():
  global posTail
  headX, headY = posHead[0], posHead[1]
  tailX, tailY = posTail[0], posTail[1]
  if abs(headX - tailX) <= 1 and abs(headY - tailY) <= 1:
    return
  
  # move Y axis
  if headX == tailX:
    # tail under head
    if headY - tailY > 0:
      posTail = (tailX, tailY + 1)
    # tail over head
    if headY - tailY < 0:
      posTail = (tailX, tailY - 1)
  
  # move X axis
  elif headY == tailY:
    # tail left of head
    if headX - tailX > 0:
      posTail = (tailX + 1, tailY)
    # tail right of head
    if headY == tailY and headX - tailX < 0:
      posTail = (tailX - 1, tailY)

  else:
    # X is too far
    if headX - tailX >= 2 and headY - tailY > 0:
      posTail = (tailX + 1, tailY + 1)
    elif headX - tailX >= 2 and headY - tailY < 0:
      posTail = (tailX + 1, tailY - 1)
    elif headX - tailX <= -2 and headY - tailY > 0:
      posTail = (tailX - 1, tailY + 1)
    elif headX - tailX <= -2 and headY - tailY < 0:
      posTail = (tailX - 1, tailY - 1)

    # Y is too far
    elif headY - tailY >= 2 and headX - tailX > 0:
      posTail = (tailX + 1, tailY + 1)
    elif headY - tailY >= 2 and headX - tailX < 0:
      posTail = (tailX - 1, tailY + 1)
    elif headY - tailY <= -2 and headX - tailX > 0:
      posTail = (tailX + 1, tailY - 1)
    elif headY - tailY <= -2 and headX - tailX < 0:
      posTail = (tailX - 1, tailY - 1)
  # print(f'tail move to {posTail}')
  tailSet.add(posTail)


def tooFar():
  headX, headY = posHead[0], posHead[1]
  tailX, tailY = posTail[0], posTail[1]
  # if on the same axis, check for only linear distance
  if headX == tailX or headY == tailY:
    return abs(headX - tailX) + abs(headY - tailY) > 1

  return abs(headX - tailX) + abs(headY - tailY) > 2 


with open('day9/input.in', 'r', encoding="utf-8") as f:
  # read data
  lines = f.read().split('\n')

  for line in lines:
    direction, distance = line.split(' ')
    move(direction, int(distance))
  # print(headQueue)
  # print(tailSet)
  print(f'[PART 1] Number of spaces visited: {len(tailSet)}')
    