with open('day4/input.in', 'r', encoding="utf-8") as f:
  data = f.read().strip()
  pairs = data.split('\n')
  subsets = 0
  intersects = 0
  for pair in pairs:
    sections = pair.split(',')
    ran1 = sections[0]
    ran2 = sections[1]
    [start1, end1] = ran1.split('-')
    [start2, end2] = ran2.split('-')
    set1 = set(range(int(start1),int(end1)+1))
    set2 = set(range(int(start2),int(end2)+1))
    if set1.issubset(set2) or set2.issubset(set1):
      # print(set1, set2)
      subsets += 1
      # print(f'{count}: {start1}-{end1}, {start2}-{end2}')
    if set.intersection(set1, set2):
      intersects += 1
      print(f'{intersects}: {start1}-{end1}, {start2}-{end2}')


  print(f'[PART 1] count: {subsets}')
  print(f'[PART 2] count: {intersects}')