
START = 'AA'

# parse input and put it in a dictionary with the valve name as the key
data = open('day16/input.in', 'r', encoding="utf-8").read().split('\n')
valves = dict()
for line in data:
  words = line.split()
  valves[words[1]] = {
    'rate': int(words[4][5:len(words[4])-1]),
    'leadsTo': [word.strip(',') for word in words[9:]]
  }
# print(valves)
# get the valves that actually have a flow rate
toOpen = [v for v in valves if valves[v]['rate'] > 0]
print(len(toOpen))

# track the shortest distance from each valves
distances = dict()

for valve in valves: #valve is the key for valves
  if valve != START and not valves[valve]['rate']:
    continue # ignore "empty" nodes

  distances[valve] = {valve: 0, START: 0} # we add the current valve and the START temporarily so we dont search them

  visited = {valve}

  visitQ = [(0, valve)] # (distance, name of visited valve)
  

  # breadth first search for shortest path
  while visitQ:
    distance, position = visitQ.pop(0)
    for neighbor in valves[position]['leadsTo']:
      if neighbor in visited:
        continue
      visited.add(neighbor)
      if neighbor in toOpen:
        distances[valve][neighbor] = distance + 1
      visitQ.append((distance + 1, neighbor))

  del distances[valve][valve] # remove them after searching
  if valve != START:
    del distances[valve][START]

# print(distances)

indices = dict()

for ii, el in enumerate(toOpen):
  indices[el] = ii

cache = {}
# HOW I UNDERSTAND THE BITMASK TO WORK
# 000100101 reads right to left <----------------
# 1st is open, 2nd is closed, 3rd is open, 4th is closed, etc
def dfs(time, valve, bitmask): # a bitmask track the binary state of every valve that we need to turn on
  # check cache if we have already calculated for this subtree
  if (time, valve, bitmask) in cache:
    return cache[(time, valve, bitmask)]

  maxFlow = 0
  for neighbor in distances[valve]:
    bit = 1 << indices[neighbor] # *********bit shifting, I HAVE NO CLUE WHAT THIS DOES
    if bitmask & bit:
      continue
    timeRemaining = time - (distances[valve][neighbor] + 1)
    if time <= 0:
      continue
    maxFlow = max(maxFlow, dfs(timeRemaining, neighbor, bitmask | bit) + valves[neighbor]['rate'] * timeRemaining)

  cache[(time, valve, bitmask)] = maxFlow
  return maxFlow

TIME_LEFT = 30

res1 = dfs(TIME_LEFT, START, 0)
print(f'[PART 1] The best path to take will release {res1} pressure')


# OKOK HOW BIG BRAIN IS THIS???
# -> we search partition the valves toOpen between us and the elephant
# we try every combination of partition until we find the best one
# -> we can force the partition by manually giving a bitmask where the valves belonging to the other partition are set to "open"

TIME_LEFT_ELEPHANT = 26
bAllOpen = (1 << len(toOpen)) - 1 # 1 << 6 looks like this: 1000000
bestFlow = 0
for i in range((bAllOpen + 1 // 2)):
  me = dfs(TIME_LEFT_ELEPHANT, START, i)
  ellie = dfs(TIME_LEFT_ELEPHANT, START, bAllOpen ^ i)
  bestFlow = max(bestFlow, me + ellie)

print(f'[PART 2] The best path with Yung Ellie will release {bestFlow} pressure')
# shout out the boy https://www.youtube.com/watch?v=bLMj50cpOug