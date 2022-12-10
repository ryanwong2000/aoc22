pos = []
for ii in range(10):
  pos.append((0,0))
tailSet = {(0,0)}

ROPE_LENGTH = 10

def moveHead(dir, dist):
  for i in range(dist):
    if(dir == 'R'):
      # move the x coord in the positive direction
      pos[0] = (pos[0][0] + 1, pos[0][1])
    elif(dir == 'L'):
      # move the x coord in the negative direction
      pos[0] = (pos[0][0] - 1, pos[0][1])
    elif(dir == 'U'):
      # move the y coord in the positive direction
      pos[0] = (pos[0][0], pos[0][1] + 1)
    elif(dir == 'D'):
      # move the y coord in the negative direction
      pos[0] = (pos[0][0], pos[0][1] - 1)
    for x in range(ROPE_LENGTH - 1):
      checkTail(x)
      
def checkTail(a):
  leadX, leadY = pos[a][0], pos[a][1]
  followX, followY = pos[a+1][0], pos[a+1][1]
  if abs(leadX - followX) <= 1 and abs(leadY - followY) <= 1:
    return
  
  # move Y axis
  if leadX == followX:
    # tail under head
    if leadY - followY > 0:
      pos[a+1] = (followX, followY + 1)
    # tail over head
    if leadY - followY < 0:
      pos[a+1] = (followX, followY - 1)
  
  # move X axis
  elif leadY == followY:
    # tail left of head
    if leadX - followX > 0:
      pos[a+1] = (followX + 1, followY)
    # tail right of head
    if leadY == followY and leadX - followX < 0:
      pos[a+1] = (followX - 1, followY)

  else:
    # X is too far
    if leadX - followX >= 2 and leadY - followY > 0:
      pos[a+1] = (followX + 1, followY + 1)
    elif leadX - followX >= 2 and leadY - followY < 0:
      pos[a+1] = (followX + 1, followY - 1)
    elif leadX - followX <= -2 and leadY - followY > 0:
      pos[a+1] = (followX - 1, followY + 1)
    elif leadX - followX <= -2 and leadY - followY < 0:
      pos[a+1] = (followX - 1, followY - 1)

    # Y is too far
    elif leadY - followY >= 2 and leadX - followX > 0:
      pos[a+1] = (followX + 1, followY + 1)
    elif leadY - followY >= 2 and leadX - followX < 0:
      pos[a+1] = (followX - 1, followY + 1)
    elif leadY - followY <= -2 and leadX - followX > 0:
      pos[a+1] = (followX + 1, followY - 1)
    elif leadY - followY <= -2 and leadX - followX < 0:
      pos[a+1] = (followX - 1, followY - 1)
  
  if a+1 == ROPE_LENGTH - 1:
    tailSet.add(pos[a+1]) 

with open('day9/input.in', 'r', encoding="utf-8") as f:
  # read data
  lines = f.read().split('\n')

  for line in lines:
    direction, distance = line.split(' ')
    moveHead(direction, int(distance))
  print(f'[PART 2] Number of spaces visited: {len(tailSet)}')
    