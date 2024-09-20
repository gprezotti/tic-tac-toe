import random  # Importa a biblioteca random para que o bot faça jogadas aleatórias

tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def imprimir_tabuleiro():
  for linha in tabuleiro:
    print("|".join(linha))  # Junta as linhas da matriz e as separa por um '|'
    print("-" * 5)  # Imprime uma separação de linhas com '-'

# FUNÇÃO QUE VERIFICA SE HÁ UM VENCEDOR NO JOGO
def verifica_vitoria():
  # Verifica se uma linha tem três elementos iguais e se não é vazia
  for linha in tabuleiro:
    if linha[0] == linha[1] == linha[2] and linha[0] != " ":
      return True

  # Verifica as colunas
  for coluna in range(3):
    if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != " ":
      return True

  # Verifica a diagonal principal
  if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
    return True
    
  # Verifica a diagonal secundária
  if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != " ":
    return True

  return False  # Se nenhuma condição for atendida, retorna False e o jogo continua

# FUNÇÃO QUE REALIZA UMA JOGADA NO TABULEIRO
def jogada_humano():
  while True:
    # Pede ao jogador a coordenada da linha e da coluna para ser realizada a jogada
    l = int(input("Qual linha quer fazer sua jogada (0-2)? "))
    c = int(input("Qual coluna quer fazer sua jogada (0-2)? "))

    # Se já tiver uma jogada na coordenada informada, pergunta novamente
    if tabuleiro[l][c] == "X" or tabuleiro[l][c] == "O":
      print("Uma jogada já foi feita nesse local. Por favor, escolha outras coordenadas!")

    # Se for uma coordenada vazia e estiver dentro da faixa numérica certa, o loop é interrompido
    elif (l >= 0 and l <= 2) and (c >= 0 and c <= 2):
      break
    else:
      print("Os valores têm que ser maior ou igual a 0, e menor ou igual a 2!")
  
  tabuleiro[l][c] = "X"  # Realiza a jogada do humano
  print("### JOGADA DO HUMANO ###")
  imprimir_tabuleiro()  # Imprime o tabuleiro novo após uma jogada

def jogada_bot():
  # Primeiro, o bot tenta bloquear a vitória do jogador
  for i in range(3):
    for j in range(3):
      if tabuleiro[i][j] == " ":
        tabuleiro[i][j] = "X"  # Simula a jogada do jogador
        if verifica_vitoria():
          tabuleiro[i][j] = "O"  # Bloqueia a vitória do jogador
          imprimir_tabuleiro()
          return
        tabuleiro[i][j] = " "  # Desfaz a jogada

  # Se não houver jogada para bloquear, faz uma jogada aleatória
  while True:
    l = random.randint(0, 2)
    c = random.randint(0, 2)
    if tabuleiro[l][c] == " ":
      tabuleiro[l][c] = "O"
      break

  imprimir_tabuleiro()

# FUNÇÃO QUE FAZ O JOGO ACONTECER
def main():
  contador = 0
  while contador < 9:  # Loop que vai até o número máximo de jogadas do tabuleiro
    if contador % 2 == 0:
      jogada_humano()  # Chama a função 'jogada_humano' para que uma jogada seja feita
    else:
      print("### JOGADA DO BOT ###")
      jogada_bot()  # Chama a função 'jogada_bot'

    # Verifica se o jogo tem um vencedor
    if verifica_vitoria():
      if contador % 2 == 0:
        print("O jogador 1 venceu!")
      else:
        print("O jogador 2 venceu!")
      break

    contador += 1

    # Verifica se o jogo deu velha
    if contador == 9 and not verifica_vitoria():
      print("Deu velha!")

main()