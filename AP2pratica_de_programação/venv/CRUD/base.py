


linha = '~' * 50
titulo = '\33[1:35mCadastro de vendas\33[m'
menu = '\33[1:33mMenu principal\33[m'
print(linha)
print(titulo.center(50))
print(linha)
print(menu.center(50))
print(linha)
opção = 0
while opção != 5:
    print('''   
     \33[1:33m1\33[m - \33[0:34mCadastrar Clientes\33[m
     \33[1:33m2\33[m - \33[0:34mCadastrar Motos\33[m
     \33[1:33m3\33[m - \33[0:34mComprar Motos\33[m
     \33[1:33m4\33[m - \33[0:34mConsultar Vendas\33[m
     \33[1:33m5\33[m - \33[0:34mSair\33[m
     ''')
    opção = int(input('     O que deseja fazer? '))

    if opção == 1:
        clientes = []
        while True:
            clientes.append(str(input('Qual o seu nome? ')))
            resp = str(input('Deseja cadastrar mais algum cliente?[S/N]'))
            if resp in 'nN':
                break
    elif opção == 2:
        motos = []
        while True:
            motos.append(str(input('Marca: ')))
            motos.append(str(input('Modelo: ')))
            motos.append(int(input('Ano: ')))
            motos.append(float(input('Preço: ')))

            resp = str(input('Quer adicionar mais motos? [S/N] '))
            if resp in 'nN':
                break