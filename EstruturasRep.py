inicio = int(input("Qual valor deseja começar a contagem? "))
fim = int(input("Qual valor deseja terminar a contagem? "))
x = inicio

while x <= fim:
    if (x % 2 == 0):
        print(x)

    x += 1

soma = 0
cont = 1
while cont <= 5:
    num = float(input(f'Digite a {cont}ª nota: '))
    soma += num
    cont += 1
    media = soma / 5
print(f'A média das notas é: {media}')

## # VALIDANDO DADOS DE ENTRADA COM WHILE

x = int(input("Digite um valor maior do que zero: "))

while x <= 0:
    print("Valor inválido! Digite novamente.")
    x = int(input("Digite um valor maior do que zero: "))   #O LOOP FICARÁ REPETINDO ATÉ QUE O USUÁRIO DIGITE UM VALOR VÁLIDO
    if x > 0:
        print(f'Valor válido! Iniciando programa')

x = int(input("Digite um valor maior do que zero: "))

while x <= 0:
    x = int(input("Digite um valor maior do que zero: "))     #O LOOP REPETIRÁ SEMPRE NA MESMA MENSAGEM, SEM COMENTAR COM O USUÁRIO O ERRO, FINALIZANDO O COMANDO SOMENTE SE O USUÁRIO DIGITAR UM VALOR VÁLIDO
print(f'Você digitou {x}. Encerrando o programa...')

#INTERROMPENDO UM LOOP COM BREAK

print("Digite uma mensagem para que seja repetida em sequência: ")
print("Caso queira encerrar o programa, digite 'sair'.")

while True:
    msg = input("Digite a mensagem: ")
    if msg == 'sair':
        break
    print(msg)
print("Programa encerrado.")

#VOLTANDO AO INÍCIO DO LOOP COM CONTINUE

while True:
    nome = input("Qual o seu nome? ")
    if nome != 'Gabriel':
        continue            #VOLTA PARA O INÍCIO DO LOOP, CASO NÃO SEJA O NOME 'GABRIEL', NÃO PERMITINDO QUE O USUÁRIO DIGITE OUTRO NOME

    senha = input("Qual a sua senha? ")
    if senha == '12345':
        break           #ENCERRA O LAÇO

print(f'Bem-vindo, {nome}! Você conseguiu acessar o sistema.')

  #VALORES TRUTHY AND FALSEY

