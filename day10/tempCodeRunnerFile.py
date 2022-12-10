tput = ""
  for i, value in enumerate(cycle_values):
    if cycle_values[i] in range((i % 40) - 1, (i % 40) + 2):
      output += "#"
    else:
      output += "."
    if (i + 1) % 40 == 0:
      output += "\n"