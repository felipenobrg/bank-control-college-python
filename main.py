lista_do_codigo = []
lista_do_saldo = []

print("======================DEV BANK======================")
for n in range(10):
    codigo_da_conta = int(input("Informe o código da conta: "))
    saldo_da_conta = float(input("Informe o saldo da conta: "))

    if codigo_da_conta in lista_do_codigo:
        print("ERRO: Código de conta já existente. Tente novamente.")
        exit()

    lista_do_codigo.append(codigo_da_conta)
    lista_do_saldo.append(saldo_da_conta)
while True:
 print("1. Realizar Depósito")
 print("2. Realizar Saque")
 print("3. Consultar o ativo bancário")
 print("4. Finalizar Programa")

 escolha_do_usuario = int(input("Digite aqui: "))


 if escolha_do_usuario == 1:
    codigo_informado = int(input("Informe o código da conta: "))

    if codigo_informado in lista_do_codigo:
       indice_da_conta = lista_do_codigo.index(codigo_informado)
       valor_a_ser_depositado = float(input("Informe o valor a ser depositado: "))
       lista_do_saldo[indice_da_conta] += valor_a_ser_depositado
    
       print("Seu saldo atualizado é de: R$",lista_do_saldo[indice_da_conta])
    else:
        print("ERRO: Conta não encontrada")

 if escolha_do_usuario == 2:
    codigo_informado = int(input("Informe o código da conta: "))

    if codigo_informado in lista_do_codigo:
       indice_da_conta = lista_do_codigo.index(codigo_informado)
       valor_do_saque = int(input("Digite o valor do saque que deseja realizar: "))
       if valor_do_saque < lista_do_saldo[indice_da_conta]:
           lista_do_saldo[indice_da_conta] -= valor_do_saque
           print("Seu saldo atualizado é de: R$", lista_do_saldo[indice_da_conta])
       else: 
           print("Saldo insuficiente")
    else:
        print("ERRO: Conta não encontrada")

 if escolha_do_usuario == 3:
    ativo_bancario =  sum(lista_do_saldo)
    print("Ativo bancário: R$",ativo_bancario)

 if escolha_do_usuario == 4:
    print("======================Programa finalizado======================")
    exit()