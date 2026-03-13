print('atividade 1, parte 1:')
print('numeros de zero a mil')

for numero in range(1,1001):
    print(numero)
    
#-------------------------------

print('atividade 1, parte 2:')
print('loop de nomes')

nomes = []
contador = 0

while contador < 10:
    nome = input("Digite o nome da pessoa: ")
    nomes.append(nome)
    contador += 1

print("\nLista de pessoas digitadas:")

contador = 0
while contador < len(nomes):
    print(nomes[contador])
    contador += 1

#------------------------------------
print('atividade 2:')

print('sistema de notas')

# Sistema de notas de alunos

usuario_correto = "professor"
senha_correta = "1234"

tentativas = 0
acesso = False

# Sistema de login (3 tentativas)
while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso permitido!")
        acesso = True
        break
    else:
        tentativas += 1
        print("Usuário ou senha incorretos.")

if acesso == False:
    print("Conta bloqueada. Senha incorreta 3 vezes.")
else:
    alunos = []
    notas = []

    quantidade = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(quantidade):
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        media = (nota1 + nota2) / 2

        alunos.append(nome)
        notas.append(media)

    print("\nResultado final:")

    for i in range(len(alunos)):
        print("Aluno:", alunos[i], "- Média:", notas[i])

input("Digite enter para sair:")


