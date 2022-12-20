lista = []

def crypto(execute, op):
    idx = 0
    global n_precisa
    if not '-' in execute:
        for i in range(len(execute)+1):
            print(op[i], end='')
            n_precisa = True
        print('')
    if not '+' in execute:
        for i in op[::-1]:
            print(i, end='')
            n_precisa = True
        print('')
    else:
        for sinal in execute:
            if sinal == '-':
                if op[idx] > op[idx+1]:
                    idx += 1
                    continue
                else:
                    op[idx], op[idx+1] = op[idx+1], op[idx]
                    idx += 1
                    crypto(execute, op)
                    break
            if sinal == '+':
                if op[idx] < op[idx+1]:
                    idx += 1
                    continue
                else:
                    op[idx], op[idx+1] = op[idx+1], op[idx]
                    idx += 1
                    crypto(execute, op)
                    break
                

def deYodafy(entrada):
    cont = 0
    pontuacao = entrada[-1]
    string = entrada[:-1].split()
    idx = len(string) - 1
    saida = []
    while (idx >= 0):
      saida.append(string[idx])
      idx = idx - 1
    for char in saida:
        if cont < len(saida)-1:
            print(char, end=' ')
            cont += 1
        else:
            print(char, end='')
    print(pontuacao)

def merge(coord):
    cont = 0
    coord.sort(key=lambda x: x[0])
    pos = [coord[0]]
    for i in coord:
        pos1 = pos[-1]
        if i[0] <= pos1[1]:
            pos1[1] = max(pos1[1], i[1])
        else:
            pos.append(i)
    for listop in pos:
        if cont < len(pos)-1:
            print(listop, end=' ')
            cont += 1
        else:
            print(listop, end='')
    print('')
        
    
while True:
    comando = input()
    if comando[0] == 'a':
        entrada = comando.split()
        num = int(''.join(entrada[1:]))
        listinha = []
        contador = 0
        while contador < num:
            funcao = input()
            listinha.append(funcao)
            contador += 1
        lista.append(listinha)
        
    elif comando == 'process':
        if lista:
            primeiro = lista[0][0].split()
            comando = ''.join(primeiro[0])
            execute = ' '.join(primeiro[1:])
    
            if comando == 'crypto':
                n_precisa = False
                cont = 0
                op = []
                execute = list(execute)
                for i in range(len(execute)+1):
                    cont += 1
                    op.append(cont)
                crypto(execute, op)
                if n_precisa == False:    
                    for i in op:
                        print(i, end='')
                    print('')
                lista[0].pop(0)
                if lista[0] == []:
                    lista.pop(0)
                else:
                    movendo = lista.pop(0)
                    lista.append(movendo)
            if comando == 'deYodafy':
                deYodafy(execute)
                lista[0].pop(0)
                if lista[0] == []:
                    lista.pop(0)
                else:
                    movendo = lista.pop(0)
                    lista.append(movendo)
            if comando == 'merge':
                coord = []
                nums = execute[1:-1].split('] [')
                for n in nums:
                    n = n.split(',')
                    i, j = n
                    coord.append([int(i),int(j)])
                merge(coord)
                lista[0].pop(0)
                if lista[0] == []:
                    lista.pop(0)
                else:
                    movendo = lista.pop(0)
                    lista.append(movendo)
                    
    else:
        orfaos = 0
        for listinha in lista:
            orfaos += len(listinha)
        print(f'{len(lista)} processo(s) e {orfaos} comando(s) órfão(s).')
        break
