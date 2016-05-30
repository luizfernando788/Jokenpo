from Mecanica import Meca
from Jogador import Jogador

print("jogo jokempo\n")

meca1 = Meca()
meca2 = Meca()

j1 = Jogador()
j2 = Jogador()

rodando = True
print("Vamos Jogar!\n")

while rodando:

    acao1 = meca1.atributo()[1]
    acao2 = meca2.atributo()[1]

    print("Jogador 1, jogou", acao1, "e Jogador 2 jogou ", acao2)

    if acao1 == "pedra":
        if acao2 == "pedra":
            print("empate! Ninguem perde Pontos")
        elif acao2 == "papel":
            print("Jogador 2 venceu! E Jogador 1 perde um ponto")
            j1.pontos -= 1
        elif acao2 == "tesoura":
            print("Jogador 1 Venceu! E Jogador 2 perde um ponto")
            j2.pontos -= 1

    if acao1 == "papel":
        if acao2 == "pedra":
            print("Jogador 1 Venceu! E Jogador 2 perde um ponto")
            j2.pontos -= 1
        elif acao2 == "papel":
            print("empate! Ninguem perde Pontos")
        elif acao2 == "tesoura":
            print("Jogador 2 Venceu! E Jogador 2 perde um ponto")
            j1.pontos -= 1

    if acao1 == "tesoura":
        if acao2 == "pedra":
            print("Jogador 2 Venceu! E Jogador 1 perde um ponto")
            j1.pontos -= 1
        elif acao2 == "papel":
            print("Jogador 1 Venceu! E Jogador 2 perde um ponto")
            j2.pontos -= 1
        elif acao2 == "tesoura":
            print("empate! Ninguem perde Pontos")
        else:
            print("a")

    if j1.pontos or j2.pontos == 0:
        if j1.pontos == 0:
            print("Jogador 2 Venceu a Partida!")
            rodando = False
        else:
            print("Proxima Rodada!\n")

        if j2.pontos == 0:
            print("Jogador 1 Venceu a Partida!")
            rodando = False
        else:
            print("Proxima Rodada!\n")