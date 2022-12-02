with open('day2/input.txt', 'r', encoding="utf-8") as f:
  lines = f.readlines()
  # beats = [('X','C'), ('Y','A'), ('Z', 'B')]
  opp = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
  }
  mine = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
  }
  points = [('X',1), ('Y',2), ('Z',3)]
  print(lines)