# ataque1 = "espada"
# ataque2 = "flecha"
# ataque3 = "lança"

# dano1 = 10
# dano2 = 13

# escudo = 10 

# print("Escolha qual vai ser o ataque: ")

# print("Ataque 1 -- Espada")
# print("Ataque 2 -- Flecha")
# print("Ataque 3 -- Lança")

# input("Qual será o ataque? ")

# if int(escudo and ataque1 > dano1):
#     print("Você está morto")
# elif dano1 <= escudo:
#     print("Você sobreviveu por pouco!")
# elif dano2 and escudo < 10:
#     print("Você está morto!")

escudo = 10

dano = int(input("Digite um valor de ataque: "))

if dano > 10 and escudo == 0:
    print("Você está morto!")
elif dano < 10:
    print("Você sobreviveu por pouco!")