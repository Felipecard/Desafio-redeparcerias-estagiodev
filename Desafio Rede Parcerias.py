

def pergunta_nome():
    return (input('Qual seu nome? '))


def nome_correto(n = ''):
    while(n.isnumeric()):
        print('Este campo não aceita números, digite um nome:')
        n = pergunta_nome()

    if(n == ''):
        print('Olá, Mundo!')
    else:
        print(f'Olá, {n.title()}!')


# MAIN

continuar = 'S'
while(continuar == 'S'):
    nome = pergunta_nome()
    nome_correto(nome)
    
    continuar = str(input('Deseja testar outro nome? [S/N]'))
    continuar = continuar.upper()