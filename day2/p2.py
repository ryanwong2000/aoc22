with open('day2/input.txt', 'r', encoding="utf-8") as f:
  lines = f.readlines()

  #if we want to beat A (rock) we play paper (2 points)
  shapePointsForWin = dict([('A',2),('B',3),('C',1)])
  shapePointsForLose = dict([('A',3),('B',1),('C',2)])
  shapePointsForDraw = dict([('A',1),('B',2),('C',3)])

  score = 0
  for line in lines:
    #char
    opp = line[0]
    outcome = line[2]
    #lose
    if outcome == 'X':
      score += shapePointsForLose[opp]
    #draw
    elif outcome == 'Y':
      score += shapePointsForDraw[opp] + 3
    #win
    elif outcome == 'Z':
      score += shapePointsForWin[opp] + 6
  print(f'score: {score}')
