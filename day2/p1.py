with open('day2/input.txt', 'r', encoding="utf-8") as f:
  lines = f.readlines()

  beats = dict([('X','C'), ('Y','A'), ('Z', 'B')])
  draws = dict([('X','A'), ('Y','B'),('Z','C')])
  points = dict([('X',1), ('Y',2), ('Z',3)])
  
  score = 0
  for line in lines:
    #char
    opp = line[0]
    you = line[2]
    #draw
    if opp == draws[you]:
      score += 3 + points[you]
    #you win
    elif opp == beats[you]:
      score += 6 + points[you]
    #you lose
    else:
      score += points[you]
  print(f'score: {score}')