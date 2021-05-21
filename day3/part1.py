class Numeros:

  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2


s = input()
test = 1

ultimaPos = Numeros(0, 0)

vec = [[0, 0]]


for i in s:

  presence = False

  if(i == '^'):
    ultimaPos.num1 -= 1

  elif(i == 'v'):
    ultimaPos.num1 += 1

  elif(i == '<'):
    ultimaPos.num2 -= 1

  else:
    ultimaPos.num2 += 1

  for j in vec:

    if(ultimaPos.num1 == j[0] and ultimaPos.num2 == j[1]):
      presence = True
      break

  if(not presence):
    vec.append([ultimaPos.num1, ultimaPos.num2])
    test += 1


print(test)
