vec = []
answer = 0

for i in range(1000):

  vecReserva = []

  for j in range(1000):
    vecReserva.append(0)

  vec.append(vecReserva)

while True:

  try:
    
    s = list(input().split())

    if(s[0] == "turn"):

      num1Linha = int(s[2][0:s[2].find(',')])
      num1Coluna = int(s[2][s[2].find(',')+1:len(s[2])])
      num2Linha = int(s[4][0:s[4].find(',')])
      num2Coluna = int(s[4][s[4].find(',')+1:len(s[4])])


      if(s[1] == "on"):
        
        for i in range(num1Linha, num2Linha + 1):

          for j in range(num1Coluna, num2Coluna + 1):

            if(vec[i][j] == 0):
              vec[i][j] = 1
              answer += 1
      
      elif(s[1] == "off"):
        
        for i in range(num1Linha, num2Linha + 1):

          for j in range(num1Coluna, num2Coluna + 1):

            if(vec[i][j] == 1):
              vec[i][j] = 0
              answer -= 1
    else:
      
      num1Linha = int(s[1][0:s[1].find(',')])
      num1Coluna = int(s[1][s[1].find(',')+1:len(s[1])])
      num2Linha = int(s[3][0:s[3].find(',')])
      num2Coluna = int(s[3][s[3].find(',')+1:len(s[3])])

      for i in range(num1Linha, num2Linha + 1):

        for j in range(num1Coluna, num2Coluna + 1):

          if(vec[i][j] == 0):
            vec[i][j] = 1
            answer += 1

          else:
            vec[i][j] = 0
            answer -= 1
      


  except EOFError:
    print(answer)
    break
