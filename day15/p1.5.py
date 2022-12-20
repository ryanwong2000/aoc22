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

YY = 10

intervals = []

# find the intervals over which the sensor overlaps the target YY
for i, sensor in enumerate(sensorCoords):
  beacon = beaconCoords[i]
  bx = beacon[0]
  by = beacon[1]
  sx = sensor[0]
  sy = sensor[1]
  distance = manhattanDistance(sx, sy, bx, by)
  distanceToYY = abs(YY - sy)
  if distanceToYY > distance:
    continue
  dx = abs(distance - distanceToYY)
  intervals.append((sx - dx, sx + dx))

# find beacons on the target YY to exclude them
beaconsOnYY = set([beacon[0] for beacon in beaconCoords if beacon[1] == YY])

# iterate through the possible x values on YY and check if it is covered by an interval
minX = min(interval[0] for interval in intervals)
maxX = max(interval[1] for interval in intervals)

covered = 0
for x in range(minX, maxX+1):
  if x in beaconsOnYY:
    continue
  for left, right in intervals:
    if left <= x <= right:
      covered += 1
      break
# print(intervals)
print(f'[PART 1] The number of positions covered at Y={YY} is {covered}')

