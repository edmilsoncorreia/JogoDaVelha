def novoTabuleiro():
    return [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

def imprimirTabuleiro(tabuleiro):
    for indice, valor in enumerate(tabuleiro):
        if valor == 0:
            print(" ", indice + 1, sep="", end='')
        elif valor == 1:
            print(" X", end='')
        else:
            print(" O", end='')

        if indice == 2 or indice == 5:
            print("\n---=---+---\n", end='')
        elif indice < 8:
            print (" |", end='')
    print("\n")

#IMPLEMENTAÇÃO

tabuleiro = novoTabuleiro()

jogador = "X"
jogadas = 0

imprimirTabuleiro(tabuleiro)