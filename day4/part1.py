import hashlib

strAtual = input()
numAtual = 0

while True:
  
  strWhile = strAtual + str(numAtual)

  h = hashlib.md5(strWhile.encode())

  hashAtual = h.hexdigest()

  if(hashAtual[0:5] == "00000"):
    print(strWhile)
    break

  numAtual += 1
