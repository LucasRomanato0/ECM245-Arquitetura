# Lucas Romanato de Oliveira
# RA: 20.00313-7

fileName = input('Nome do arquivo de leitura: ')
file1 = open(fileName,'r')
Lines = file1.readlines()

fileNameResult = input('Nome do arquivo para armezenar os resultados: ')
result = open(fileNameResult, 'w')

conversion = {"HLT":" : 00",
              "STO":" : 1",
              "LD":" : 2",
              "LDI":" : 3",
              "ADD":" : 4",
              "ADDI":" : 5",
              "SUB":" : 6",
              "SUBI":" : 7",
              "JUMP":" : 8",
              "NOP":" : 9"}

count = 0
n = 0
# Strips the newline character
for line in Lines:
    try:
        split = line.strip().split(" ")
        result.write(str(hex(n)).upper()[2:] + conversion[split[0]] + split[1] + "\n")
        print(line.strip())
        n = n+1
    except:
        pass
result.close()
