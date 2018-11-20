import turing

arquivo = open("maquina.txt", "r")

inicial = int(arquivo.readline().split()[0])

linha = arquivo.readline()
valores = linha.split()

finais = [int(x) for x in valores]

transicoes = {}

D = 0
E = 1
I = 2

for linha in arquivo:
    #eSaida -> eDestino com s1 n1 dir e s2 n2 dir e s2 n3 dir 
    valores = linha.split()
    estadoSaida = int(valores[0])
    estadoDestino = int(valores[2])
    
    simboloSaida1 = ' ' if valores[4] == "$" else valores[4]
    simboloDestino1 = ' ' if valores[5] == "$" else valores[5]
    direcao1 = D if valores[6] == "D" else (E if valores[6] == "E" else I)
    
    simboloSaida2 = ' ' if valores[8] == "$" else valores[8]
    simboloDestino2 = ' ' if valores[9] == "$" else valores[9]
    direcao2 = D if valores[10] == "D" else (E if valores[10] == "E" else I)
    
    simboloSaida3 = ' ' if valores[12] == "$" else valores[12]
    simboloDestino3 = ' ' if valores[13] == "$" else valores[13]
    direcao3 = D if valores[14] == "D" else (E if valores[14] == "E" else I)
    
    transicoes[(estadoSaida, simboloSaida1, simboloSaida2, simboloSaida3)] = (estadoDestino, simboloDestino1, simboloDestino2, simboloDestino3, direcao1, direcao2, direcao3)
    
mt = turing.TuringMachine(transicoes, inicial, finais)

arquivo = open("entrada.txt", "r")

for linha in arquivo:
    print("Processando " + linha.split()[0])
    print(mt.processWord(linha.split()[0]))
