data = open('day15/test.in', 'r', encoding="utf-8").read().split('\n')
lines = [line.split(': ') for line in data]

# gets the coordinates from a string containing the coordinates
def parseCoords(words):
  for word in words:
    word = word.strip(',').strip(':')
    if word.startswith('x'):
      x = int(word[2:])
    elif word.startswith('y'):
      y = int(word[2:])
  return (x, y)

sensorCoords = []
beaconCoords = []
# parse input to get beacon and sensor coords
for line in lines:
  for half in line:
    words = half.split()
    if words[0].startswith('Sensor'):
      sensorCoords.append((parseCoords(words)))
    if words[0].startswith('closest'):
      beaconCoords.append((parseCoords(words)))

def expand(x, y):
  

# define direction vectors
#      N  E  W  S
dr = [-1, 0, 0, 1]
dc = [0, 1, -1, 0]

