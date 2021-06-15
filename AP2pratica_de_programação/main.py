from time import sleep


# Menu ---------------------------------------------
linha = '~' * 50
titulo = '\33[1:35mCadastro de vendas\33[m'
menu = '\33[1:33mMenu principal\33[m'
print(linha)
print(titulo.center(50))
print(linha)
print(menu.center(50))
print(linha)
opcao = 0
while opcao != 7:
    print('''   
     \33[1:33m1\33[m - \33[0:34mCadastrar Clientes\33[m
     \33[1:33m2\33[m - \33[0:34mCadastrar Motos\33[m
     \33[1:33m3\33[m - \33[0:34mVender Motos\33[m
     \33[1:33m4\33[m - \33[0:34mConsultar Vendas\33[m
     \33[1:33m5\33[m - \33[0:34mRemover/Editar Motos\33[m
     \33[1:33m6\33[m - \33[0:34mRemover/Editar Clientes\33[m
     \33[1:33m7\33[m - \33[0:34mSair\33[m
     ''')
# Validando inputs ---------------------------------------------
    try:
        print(linha*2)
        opcao = (int(input(('\33[1:33mO que deseja fazer? \33[m'))))

    except:
        print('Opção inválida. Tente novamente.')
        sleep(1)
    if 7 < opcao < 0:
        print('Opção inválida. Tente novamente.')
        sleep(1)
    # ------------------------------------------Cadastrando Clientes------------------------------------------------
    if opcao == 1:
        while True:
            novoCliente = (str(input('     Qual o seu nome? ')))
            CPFcliente = (str(input('     Qual o seu CPF? (XXX.XXX.XXX-XX) ')))
            with open('cadastro_clientes.txt', 'a', encoding="utf-8") as cadastro_clientes:
                cadastro_clientes.write( f'|  Cliente: {novoCliente}  |  CPF: {CPFcliente}  \n ')
            resp = str(input('Deseja cadastrar mais algum cliente?[S/N]'))
            if resp in 'nN':
                break
    # -----------------------------------------Cadastrando Motos-----------------------------------------------------
    elif opcao == 2:
        while True:
            marca = str(input('Marca: ')).upper()
            modelo = str(input('Modelo: ')).upper()
            ano = int(input('Ano: '))
            preco = float(input('Preço: R$'))
            placa = str(input('Placa (XXX-XXXX): ')).upper()
            novoMoto = f'Marca: {marca}  |  Modelo: {modelo}  |  Ano: {ano}  |  Preço: {preco:.2f}  |  Placa: {placa} \n'
            with open('cadastro_motos.txt', 'a', encoding="utf-8") as cadastro_motos:
                cadastro_motos.write(novoMoto)

            resp = str(input('Quer adicionar mais motos? [S/N] '))
            if resp in 'nN':
                break

# Comprando motos -------------------------------------------------------------------------------------------------
    elif opcao == 3:
        while True:
            print(linha)
            with open('cadastro_motos.txt', 'r', encoding="utf-8") as cadastro_motos:
                for moto in cadastro_motos:
                    print(f'{moto}', end='')
            print(linha)
            placa = str(input('Digite a placa do veículo (Formato LLL-NNNN): ')).upper().strip()
            if len(placa) == 8 and '-' in placa or placa == '0':
                break
            print('\n\033[1;31mA placa está incorreta. Digite-a na forma LLL-NNNN ou LLL-NLNN ou 0 para cancelar'
                  '\n\033[m')


        with open('cadastro_motos.txt', 'r+', encoding="utf-8") as cadastro_motos:
            texto = cadastro_motos.readlines()
            confirm = 'sS'
            for moto in texto:
                if placa in moto:
                    print('Veículo selecionado:')
                    print(moto)
                    confirm = str(input('Deseja vender o veículo?(S/N)\n'))
                    if confirm in 'sS':

                        with open('lista_vendas.txt', 'w+', encoding="utf-8") as lista_vendas:
                            salvar = lista_vendas.write(moto)
                        texto.remove(moto)
                        cadastro_motos = open("cadastro_motos.txt", "w", encoding="utf-8")
                        cadastro_motos.writelines(texto)
                        cadastro_motos.close()
                        print('\033[1;32mVendendo veículo...\033[m')
                        sleep(1.5)
                        print('\033[1;32mVeículo vendido com sucesso\033[m')
                        break
            else:
                if confirm in 'sS':
                    print('\n\033[1;31mEsta placa não foi encontrada ou já foi vendida. Tente novamente.\033[m')

# Mostrando Motos ---------------------------------------------------------------------------------------------------
    elif opcao == 4:
        print(linha * 2)
        print("{:^100}".format('\33[1:33mListagem de vendas\33[m'))
        print(linha * 2)
        with open('lista_vendas.txt', 'r', encoding="utf-8") as lista_vendas:
            for moto in lista_vendas:
                print(f'{moto}', end='')
        print()
        print(linha*2)

# -----------------------------------------Editar cadastro Motos-----------------------------------------------------

    elif opcao == 5:
        quest = str(input('Digite R para Remover e E para Editar ?(R/E)\n'))
        if quest in 'eE':
            while True:
                print(linha)
                placa = str(input('Digite a placa do veículo (Formato LLL-NNNN): ')).upper().strip()
                if len(placa) == 8 and '-' in placa:
                 break
                print('\n\033[1;31mA placa está incorreta. Digite-a na forma LLL-NNNN ou LLL-NLNN ou 0 para cancelar'
                     '\n\033[m')

            with open('cadastro_motos.txt', 'r+', encoding="utf-8") as cadastro_motos:
                texto = cadastro_motos.readlines()
                confirm = 'sS'

                for moto in texto:
                    if placa in moto:
                        print('Cadastro selecionado:')
                        print(moto)
                        confirm = str(input('Deseja editar este cadastro?(S/N)\n'))
                        if confirm in 'sS':

                            cadastro_motos = open("cadastro_motos.txt", "w+", encoding="utf-8")
                            texto.remove(moto)
                            cadastro_motos.writelines(texto)
                            marca = str(input('Marca: ')).upper()
                            modelo = str(input('Modelo: ')).upper()
                            ano = int(input('Ano: '))
                            preco = float(input('Preço: R$'))
                            placa = str(input('Placa (XXX-XXXX): ')).upper()
                            editMoto = f'Marca: {marca}  |  Modelo: {modelo}  |  Ano: {ano}  |  Preço: {preco:.2f} | Placa: {placa} \n'
                            cadastro_motos.writelines(editMoto)
                            cadastro_motos.close()
                            print('\033[1;32mSalvando alterações...\033[m')
                            sleep(1.8)
                            print('\033[1;32mcadastro editado com Sucesso\033[m')
                            sleep(1.5)
                            break
                else:
                    if confirm in 'sS':
                        print('\n\033[1;31mEsta placa não consta no nosso cadastro. Tente novamente.\033[m')


# --------------------------------- Remover cadastro motos -----------------------------------------------------------
        if quest in 'rR':
            while True:
                print(linha)
                placa = str(input('Digite a placa do veículo (Formato LLL-NNNN): ')).upper().strip()
                if len(placa) == 8 and '-' in placa:
                    break
                print('\n\033[1;31mA placa está incorreta. Digite-a na forma LLL-NNNN ou LLL-NLNN ou 0 para cancelar''\n\033[m')

            with open('cadastro_motos.txt', 'r+') as cadastro_motos:
                texto = cadastro_motos.readlines()
                req = 'sS'
                for moto in texto:
                    if placa in moto:
                        print('Veículo selecionado:')
                        print(moto)
                        req = str(input('Deseja remover o cadastro?(S/N)\n'))
                        if req in 'sS':
                            texto.remove(moto)
                            cadastro_motos = open("cadastro_motos.txt", "w")
                            cadastro_motos.writelines(texto)
                            cadastro_motos.close()
                            print('\033[1;32mRemovendo cadastro...\033[m')
                            sleep(1.5)
                            print('\033[1;32mcadastro removido com Sucesso\033[m')
                            break
                else:
                    if req in 'sS':
                        print('\n\033[1;31mEsta placa não foi encontrada ou já foi removida. Tente novamente.\033[m')



# --------------------------------- Remover cadastro motos -------------------------------------------------------------





# -----------------------------------------Editar cadastro Clientes-----------------------------------------------------