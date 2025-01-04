import pandas as pd

#Criando uma variável para o "Banco de Dados".
registro = []
conf = ['S','N']
acento = ['é','á','è','é','ê','í','ì','î','ã','õ','ó','ò','ô']


pergunta = int(input('Quantos usuários vocÊ quer registrar?\nLEMBRANDO QUE QUANTIDADE QUE QUERER REGISTRAR VAI SER UM A MENOS '))
for i in range(0,pergunta):
    print(f'Registrando o {i+1} usuário:')
    
    #Programando uma caixa registrar o nome do cliente.
    nome = str(input(f'Qual é da nome da {i+1}º pessoa? ').title())
    while True:
        conf_n = str(input(f'{nome}, esta certo o seu nome? ').upper())
        if conf_n in conf[0]:
            print('OK')
            break
        elif conf_n in conf[1]:
            nome = str(input('Digite o nome novamente: ').title())
            print('OK')
        else:
            print('Entrada inválida, só digite S/N. ')
    #Regisstrar o CPF do usuário.
    while True:
        CPF = str(input(f'Digite o CPF do {nome}:'))
        if CPF.count('.') == 2 and CPF.count('-') == 1 and len(CPF) == 14:
            print('OK')
            break
        else:
            print('Seu CPF foi digitado incorretamente, digite novamente: ')

#Confirmar o CPF dele.
    while True:
        conf_CPF = str(input(f'{CPF}, está certo? ').upper())
        if conf_CPF in conf[0]:
            print('OK')
            break
        elif conf_CPF in conf[1]:
            CPF = str(input('Digite o CPF, novamente: '))
            break
        else:
            print('Entrada inválida, só digite S/N.')

            #Registrar o E-mail.
    while True:
        email = str(input(f'Digite 0 e-mail do {nome}: '))
        if ('@gmail.com' in email ) or ('@hotmail.com' in email) or ('@yahoo.com' in email):
            print('OK')
            break
        elif any(c in email for c in acento):
            email=str(input('E-mail inválido digite novamente: '))
        else:
            print('Você não digitou seu E-mail corretamente, digite seu novamente.')

    #Confirmar o E-mail (2X).
    while True:
        conf_e = str(input(f'{email}, está certo? ').upper())
        if conf_e in conf[0]:
            print('OK')
            break
        elif conf_e in conf[1]:
            email = input('Reescreva o E-mail: ')
        else:
            print('Entrada inválida, só pode digitar S/N: ')

    conf2_e = str(input('Reescreva seu email, para confirmar: '))
    while conf2_e not in email:
        print('Você digitou errado o email!')
        email = str(input('Digite novamente: '))
        print('OK')
        break
                

    salario = int(input(f'Quanto ganha o {nome}, por mês? '))
    while True:
        conf_s = input(f'{salario}, está certo? ').upper()
        if conf_s == conf[0]:
            print('Ok')
            break
        elif conf_s == conf[1]:
            salario  = int(input('Digite corretamente:'))
        else:
            print('Entrada inválida, digite somente S/N:')
            
    while True:
        if salario != None:
            aumento = salario * (1 + 0.2)
            print(aumento)
            break
        else:
            aumento = None
            break

    registro.append({'Id': i+1, 'Nome': nome, 'CPF':CPF, 'E-mail': email, 'Salário': salario, 'Promoção': aumento})

   

#Mostrar os dados do usuário.
tabela = pd.DataFrame(registro)
print(tabela)