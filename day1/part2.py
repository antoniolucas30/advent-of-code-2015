s = input()

currentLevel = 0
total = 1

for i in s:

  if(i == '('):
    currentLevel += 1

  else:
    currentLevel -= 1
  
  if(currentLevel == -1):
    break

  total += 1

print(total)
