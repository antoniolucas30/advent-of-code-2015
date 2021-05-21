numAtual = 0

while True:

  try:

    p = 0
    letter = 0
    l = 1

    s = input()

    for i in range(1, len(s)):

      duplaAtual = s[i - 1] + s[i]

      if(duplaAtual[0] == duplaAtual[1]):
        letter = 1

      if(duplaAtual == "ab" or duplaAtual == "cd" or duplaAtual == "pq" or duplaAtual == "xy"):
        l = 0


    p = (l) and (letter) and (((s.count('a')) + (s.count('e')) + (s.count('i')) + (s.count('o')) + (s.count('u'))) >= 3)

    numAtual += p


  except EOFError:
    print(numAtual)
    break
