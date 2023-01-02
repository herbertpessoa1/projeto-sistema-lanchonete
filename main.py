nome = input("Olá, somos da quase três lanches, para fazer seu pedido, digite seu nome")
print(nome)
valor = 0
nome_lanche = ""

opcao = int(input(
    "Bem vindo a quase três lanches,faça o seu pedido, aperte 1 para PIZZA 25.00 R$ , 2 para LANCHE 10.00R$ , 3 para SALGADINHO 5.00 R$ :"))

if opcao == 1:
    valor = 25.0
    nome_lanche = "PIZZA"
elif opcao == 2:
    valor = 10.0
    nome_lanche = "LANCHE"
elif opcao == 3:
    valor = 5.0
    nome_lanche = "PIZZA"

opcao = int(input(
    "Você gostaria de confirmar seu pedido? se sim aperte 1 para confirmar o pedido e a taxa de serviço no valor de  de 10,00 R$."
    " para cancelar o pedido aperte 2 :"))

if opcao == 1:
    valor = 25.0
    nome_lanche = "PIZZA"
elif opcao == 2:
    valor = 10.0
    nome_lanche = "LANCHE"

opcao = int(input(
        "Chegou a hora de pagar aperte 1 para Debito, 2 para Credito, 3 para especie   :"))

if opcao == 1:
   debito

elif opcao == 2:
   credito

elif opcao == 3:
   especie




