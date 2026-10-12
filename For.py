frase = "Lógica de Programação e Algoritmos"
for i in range(0, len(frase), 1):
    print(frase[i], end='')


x = 1
while x < 6:
    print(x)
    x += 1

for i in range(1, 6, 1):
    print(i)

media = 100
if media % 2 == 0:
    for i in range(1, 101):     
        print(i)
        media = i / 2
    print("Média: ", media)


