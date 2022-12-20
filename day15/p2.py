data = open('day15/input.in', 'r', encoding="utf-8").read().split('\n')
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

def manhattanDistance(x1, y1, x2, y2):
  return abs(x1 - x2) + abs(y1 - y2)

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

positiveLines = []
negativeLines = []

# find the boundary lines made by each sensor
for i, sensor in enumerate(sensorCoords):
  beacon = beaconCoords[i]
  bx = beacon[0]
  by = beacon[1]
  sx = sensor[0]
  sy = sensor[1]
  distance = manhattanDistance(sx, sy, bx, by)
  # negative slope: y = -ax + b -> 0 = x + y + b
  # positive slope: y = ax + b -> 0 = x - y + b
  negativeLines.extend([sx + sy - distance, sx + sy + distance])
  positiveLines.extend([sx - sy - distance, sx - sy + distance])

POSITIVE_LINE = None
NEGATIVE_LINE = None

for ii in range(len(positiveLines)):
  for jj in range(ii + 1, len(positiveLines)):
    l1, l2 = positiveLines[ii], positiveLines[jj]
    if abs(l1 - l2) == 2:
      POSITIVE_LINE = min(l1, l2) + 1

    l1, l2 = negativeLines[ii], negativeLines[jj]
    if abs(l1 - l2) == 2:
      NEGATIVE_LINE = min(l1, l2) + 1

XX = 0
YY = 20

xx = (POSITIVE_LINE + NEGATIVE_LINE) // 2
yy = (NEGATIVE_LINE - POSITIVE_LINE) // 2

print(f'[PART 2] The number only possible location for the beacon between X={XX} and Y={YY} is at x={xx} and y={yy}')
print(f'         The tuning frequency is {xx * 4000000 + yy}')

