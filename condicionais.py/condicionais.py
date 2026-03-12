dados = {
'nomes':[],
'idades':[],
'quartos':["Simples", "Duplo" , "Luxo"],
'valores':[100.0,150.0,250.0]
}

quantidade_de_pessoas = int(input('Quantidade de Pessoas:'))

if quantidade_de_pessoas == 1:
    dados['nomes'].append(input('Digite  o nome: '))
    dados['idades'].append(input('Digite  a Idade: '))

# logica
    print('escolha um quarto:', dados['quartos'])


elif quantidade_de_pessoas == 2:
    dados['nomes'].append(input('Digite  o nome: '))
    dados['idades'].append(input('Digite  a Idade: '))    
    dados['nomes'].append(input('Digite  o nome: '))
    dados['idades'].append(input('Digite  a Idade: '))

    # logica

elif quantidade_de_pessoas == 3:
    dados['nomes'].append(input('Digite  o nome: '))
    dados['idades'].append(input('Digite  a Idade: '))    
    dados['nomes'].append(input('Digite  o nome: '))
    dados['idades'].append(input('Digite  a Idade: '))    
    dados['nomes'].append(input('Digite  o nome: '))
    dados['idades'].append(input('Digite  a Idade: '))    


    # logica

else:
    print('Digite algo válido... ')
