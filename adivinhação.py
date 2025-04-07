import random

# Dicionário para armazenar o número de tentativas de cada jogador
tentativas_por_jogador = {}

# Função principal do jogo
def adivinhar_numero():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    
    # Lista para armazenar os palpites do usuário
    palpites = []
    
    print("Bem-vindo ao jogo de adivinhar o número!")
    print("Eu pensei em um número entre 1 e 100. Tente adivinhar!")
    
    nome_jogador = input("Qual é o seu nome? ")
    tentativas = 0

    while True:
        palpite = int(input("Qual é o seu palpite? "))
        tentativas += 1
        palpites.append(palpite)  # Adiciona o palpite à lista
        
        # Verifica se o palpite está correto
        if palpite < numero_secreto:
            print("O número é maior. Tente novamente!")
        elif palpite > numero_secreto:
            print("O número é menor. Tente novamente!")
        else:
            print(f"Parabéns, {nome_jogador}! Você adivinhou o número em {tentativas} tentativas.")
            print(f"Seus palpites foram: {palpites}")
            tentativas_por_jogador[nome_jogador] = tentativas  # Armazena o número de tentativas no dicionário
            break

# Chama a função do jogo
()

# Exibe as tentativas de cada jogador
