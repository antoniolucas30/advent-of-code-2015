numAtual = 0

while True:

  try:

    s = input()

    p = 0
    l = 0

    for i in range(1, len(s)):

      primeira = s[i - 1] + s[i]

      if(primeira in s[i+1:len(s)+1]):
        p = 1
        break

    for i in range(2, len(s)):

      atual = s[i - 2] + s[i - 1] + s[i]

      if(atual[0] == atual[2]):
        l = 1
        break

    

    numAtual += (p and l)


  except EOFError:
    print(numAtual)
    break
