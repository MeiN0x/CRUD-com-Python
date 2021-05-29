clientes = []
clientestxt = open('Clientes.txt', 'w+')
while True:
        clientes.append(str(input('Qual o seu nome? ')))
        resp = str(input('Deseja cadastrar mais algum cliente?[S/N]'))
        if resp in 'nN':
                break
clientestxt.write('Cliente')
with open('clientes.txt', 'a+') as bdd:
    for nome in clientes:
        bdd.write(str(nome) + '\n')