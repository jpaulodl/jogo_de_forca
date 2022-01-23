import random

def jogar():

    imprime_msg_abertura()

    imprime_tema()

    tema = int(input('Qual o tema: '))
    if (tema == 1):
        palavra = frutas()
    elif (tema == 2):
        palavra = paises()
    else:
        palavra = objetos()
    

    letras_acertadas = inicializa_letras_acertada(palavra)
    
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        
        chute = pede_chute()

        if(chute in palavra):
            marca_chute_correto(chute,letras_acertadas,palavra)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        vencedor()
    else:
        perdedor(palavra)


def imprime_msg_abertura():
    print('****************************')
    print('|Bem vindo ao jogo de Forca|')
    print('****************************\n')

def imprime_tema():
    print('Escolha o tema!\n')
    print('(1) Frutas')
    print('(2) Países')
    print('(3) Objetos\n')

def frutas():
    arquivo = open('frutas.txt', 'r')
    lista = []

    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista))
    palavra = lista[numero].upper()
    return palavra

def paises():
    arquivo = open('paises.txt', 'r')
    lista = []

    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista))
    palavra = lista[numero].upper()
    return palavra

def objetos():
    arquivo = open('objetos.txt', 'r')
    lista = []

    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(lista))
    palavra = lista[numero].upper()
    return palavra

def inicializa_letras_acertada(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute,letras_acertadas,palavra):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def perdedor(palavra):
    print('')
    print(f"A palavra era {palavra}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == '__main__'):
    jogar()
