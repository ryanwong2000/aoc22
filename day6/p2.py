with open('day6/test.in', 'r', encoding="utf-8") as f:
  buffer = f.read()
  window = buffer[:14]
  marker = -1
  for x in range(14, len(buffer)):
    print(f'window: {window}')
    #check dupes
    if len(window) == len(set(window)):
       marker = x
       break
    # move to the right
    window = window[1:] + buffer[x]
  print(f'[PART 1] The first marker after character: {marker}')