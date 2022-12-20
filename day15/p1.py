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

covered = set()
# calculate the manhattan distance to the beacon coordinates
for iSensor, sensor in enumerate(sensorCoords):
  sensorX, sensorY = sensor
  beaconX, beaconY = beaconCoords[iSensor]
  distance = abs(sensorX - beaconX) + abs(sensorY - beaconY)
  # mark all the coordinates within that distance as marked
  
  # define direction vectors
  dr = [1, 1, -1, -1]
  dc = [1, -1, 1, -1]
  for d in range(4):
    for ii in range(distance+1):
      for jj in range(ii+1):
        covered.add((sensorX + jj * dr[d], sensorY + (ii - jj) * dc[d]))

yLevel = 2000000
covered = covered.difference(set(beaconCoords))
print(len(covered))
res = [x for x in covered if x[1] == yLevel]
print(len(res))


