import settings
import os

parkingLot = [[".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
             ]

# C = carro
# P = pessoa
# V = Vanessa
# A = Carro autonomo da vanessa

def readPseudoFen():
  global parkingLot
  fenDefalt = "1CCC1C2C1/1P5P1P/1CC1CC3C/6CC1C/CPPC1P4/3C2CCC1/1CCCP1CCP1/3PC1P3/CP7C/PC1CC2C1P"
  fenline = fenDefalt.split("/")

  spacesCounter = 0
  lineCounter = -1

  for line in fenline:
    lineCounter += 1
    spacesCounter = 0
    for char in line:
      if char == "C" or char == "P" or char == "V" or char == "A":
        parkingLot[lineCounter][spacesCounter] = char
        spacesCounter += 1
      else:
        blanks = int(char)
        spacesCounter += blanks

readPseudoFen()

oldTrain = [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]

Train = [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]


alpha = 0.4
gama = 0.8

def bigger(*oldT):
  bigger = oldT[0][0]
  for i in range(1,4):
    if(oldT[0][i] > bigger):
      bigger = oldT[0][i]
  return bigger

def going(j,k,i):
  if(i==0): # going -> up
    if(j-1 < 0): return j,k 
    else: return j-1,k
  if(i==1): # going -> left
    if(k-1 < 0): return j,k
    else: return j,k-1
  if(i==2): # going -> down
    if(j+1 > 9): return j,k
    else: return j+1,k
  if(i==3): #going -> right
    if(k+1 > 9): return j,k
    else: return j,k+1


def checkNextPosition(j,k,*park):
  x = park[0][j][k]
  if x == ".":
    return 1
  elif x == "C":
    return 2
  elif x == "P":
    return 3
  elif x == "V":
    return 4

os.system('cls' if os.name == 'nt' else 'clear')

print(". = Posições acessiveis do estacionamento\nC = Carro\nP = Pessoa")

# mostra o estacionamento
for line in parkingLot:
  for spot in line:
    if spot == "A" or spot == "V":
      print(f'{settings.bcolors.WARNING}{spot}{settings.bcolors.ENDC}', end="     ")
    else:
      print(spot, end="     ")
  print("\n")

# instruções
print("Digite as posições de Vanessa e do seu Carro:\n(no formato [x][y])\n(x,y -> 1 até 10)\n(x -> da esquerda para direita)\n(y -> de cima para baixo)\n(não faz sentido posicionar Vanessa e seu carro no mesmo local)")

# pede input pro user
while True:
  print("\nVanessa:")
  vx = int(input("[x]:"))-1
  vy = int(input("[y]:"))-1
  print("Carro:")
  cx = int(input("[x]:"))-1
  cy = int(input("[y]:"))-1

  if((vx == 9 and vy == 0) or (cx == 9 and cy == 0)):
    print("Vanessa ou carro autônomo bloqueado, impossivel se encontrarem")
  elif(vx in range(0,10) and vy in range(0,10) and cy in range(0,10) and cx in range(0,10) and (cx != vx or cy != vy) and parkingLot[cy][cx] == "." and parkingLot[vy][vx] == "."):
      break

  print("POSIÇÃO(ÕES) INVALIDAS, digite novamente")

os.system('cls' if os.name == 'nt' else 'clear')

parkingLot[vy][vx] = "V"

# Treinamento
for _ in range(0,55): # n -> de treinamentos
  for j in range(0,10): # -> coluna
    for k in range(0,10): # -> linha
      if(parkingLot[j][k] == "."):
        for i in range(0,4):
          x, y = going(j,k,i)
          #print(x,y)            
          z = checkNextPosition(x,y,parkingLot)

          if(z == 1):
            maxQ = bigger(oldTrain[x][y])
          elif(z == 2):
            maxQ = settings.reward.CrashInCar
          elif(z == 3):
            maxQ = settings.reward.RunOverPerson
          elif(z == 4):
            maxQ = settings.reward.GetToVanessa
            
          Train[j][k][i] = oldTrain[j][k][i] + alpha * (settings.reward.GoToBlank + gama * maxQ - oldTrain[j][k][i])
    oldTrain = Train 

parkingLot[cy][cx] = "A"

# inicia variavel para dizer o caminho
track = parkingLot

# monta o caminho em "track"
while True:
  bestOption = Train[cy][cx][0]
  x=0
  for i in range(1,4):
    if(Train[cy][cx][i] > bestOption):
      x = i
      bestOption = Train[cy][cx][i]

  if(x == 0): cy-= 1 #0 -> UP
  if(x == 1): cx-= 1 #1 -> LEFT
  if(x == 2): cy+= 1 #2 -> DOWN
  if(x == 3): cx+= 1 #3 -> RIGHT

  
  if(cy == vy and cx == vx): break

  track[cy][cx] = "☆"

print("Caminho do carro autônomo até Vanessa no estacionamento. \n(A = Carro autônomo, V = Vanessa, ☆ = Caminho do carro até Vanessa)\n")
for line in track:
  for spot in line:
    if spot == "A" or spot == "V":
      print(f'{settings.bcolors.WARNING}{spot}{settings.bcolors.ENDC}', end="     ")
    elif spot == "☆":
      print(f'{settings.bcolors.OKGREEN}{spot}{settings.bcolors.ENDC}', end="     ")
    else:
      print(spot, end="     ")
  print("\n")

print("Deseja ver o treinamento de cada estado('.')? ('Y' para sim) (qualquer tecla para não)")
c = input()

if(c == "Y" or c == "y"):
  print("\nformato: [linha][coluna] -> [cima, esquerda, baixo, direita]\n")
  for b in range(0,10):  
    for a in range(0,10):
      print("[", b,"][", a, "] ->", Train[b][a])
    print('\n')
else:
  print("allright, bye :)")
