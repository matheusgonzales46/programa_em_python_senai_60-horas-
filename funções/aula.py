#atividade 1:


def comparar_par_impar(num1, num2):
    if num1 % 2 == 0:
        print(f"{num1} é PAR")
    else:
        print(f"{num1} é ÍMPAR")

    if num2 % 2 == 0:
        print(f"{num2} é PAR")
    else:
        print(f"{num2} é ÍMPAR")
#--------------------------------------------
# atividade 2:


def multiplicar(a, b, c):
    resultado = a * b * c  # variável local
    return resultado
#--------------------------------------------
# atividade 3:


def potencia(base, expoente):
    resultado = base ** expoente
    return resultado
#--------------------------------------------
# atividade 4:

def verificar_idade(idade):
    if idade == 18:
        print("Parabéns! Você tem 18 anos!")
    else:
        print("Idade diferente de 18.")     
#---------------------------------------------
#atividade 5:


def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade
#---------------------------------------------
#atividade 6:


def brasil_copa_1999():
    # Copa masculina de 1999 não existiu (foi 1998 e 2002)
    return "Não, o Brasil não ganhou a Copa de 1999."
#----------------------------------------------
#atividade 7:


def cumprimentar():
    print("Bem-vindo ao restaurante!")

def restaurante():
    cardapio = ["salada", "macarronada", "sanduiche", "sorvete"]

    while True:
        print("\nCardápio:")
        for i, item in enumerate(cardapio, 1):
            print(f"{i} - {item}")

        escolha = int(input("Escolha um número (0 para sair): "))

        if escolha == 0:
            print("Obrigado pela visita!")
            break
        elif 1 <= escolha <= len(cardapio):
            print(f"Você escolheu: {cardapio[escolha - 1]}")
        else:
            print("Opção inválida!") 
cumprimentar()
restaurante()           
