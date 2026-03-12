#1) verifique se o número é par ou impar :
print('atividade 1, verifique se o número é par ou impar:')

numero = int(input("Digite um número: "))

match numero % 2:
    case 0:
        print("O número é par")
    case _:
        print("O número é ímpar")
#---------------------------------
#2) verifique se um número é positivo, negativo ou zero :
print('atividade 2, verifique se um número é positivo, negativo ou zero :')

numero = int(input("Digite um número: "))

match numero:
    case n if n > 0:
        print("Número positivo")
    case n if n < 0:
        print("Número negativo")
    case _:
        print("Número é zero")

#------------------------------------------
#3) verifique se uma string é vazia ou não:
print('atividade 3, verifique se uma string é vazia ou não:')

texto = input("Digite uma palavra: ")

match texto:
    case "":
        print("A string está vazia")
    case _:
        print("A string não está vazia")

#---------------------------------------        
#4) verifique se um número é maior, menor ou igual a 10:

print('atividade 4, verifique se um número é maior, menor ou igual a 10:')

numero = int(input("Digite um número: "))

match numero:
    case n if n > 10:
        print("Maior que 10")
    case 10:
        print("Igual a 10")
    case _:
        print("Menor que 10")

#5) classifique uma idade em faixas etárias - criança(12), adolecente(17), jovem(35), adulto (35 >< 64), idoso(65):
print('atividade 5, classifique uma idade em faixas etárias - criança(12), adolecente(17), jovem(35), adulto (35 >< 64), idoso(65):')

idade = int(input("Digite a idade: "))

match idade:
    case n if n <= 12:
        print("Criança")
    case n if n <= 17:
        print("Adolescente")
    case n if n <= 20:
        print("Jovem")
    case n if n <= 35:
        print("Adulto")
    case _:
        print("Idoso")

#-------------------------------------