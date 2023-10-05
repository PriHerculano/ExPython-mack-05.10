#Um cinema possui capacidade de 100 lugares e está sempre com ocupação total.Certo dia, cada espectador teve que responder
#a um questionário, no qual constava: Sua idade(superior ou igual a 14 anos – validar!) Sua opinião em relação ao filme,
#segundo as seguintes notas:
#Escreva um programa em Python que, lendo esses dados, calcule e apresente:
#A-Otimo
#B-Bom
#C-Regular
#D-Ruim
#E-Pessimo
#a) a quantidade de respostas Ótimo;
#b) a média de idade de todas as pessoas;
#c) a porcentagem de respostas Péssimo;
#d) a maior idade entre as pessoas que responderam Bom;

qntdOtimo = 0
somaIdade = 0
porcentPessimo = 0
maiorIdadeBom = 0

for i in range(100):
    idade = int(input(f"Espectador idade {i+1} :"))

    if idade < 14:
        print("Idade inválida!")
        break

    opiniao=input(f"Opinião do espectador {i+1} A-Otimo, B-Bom, C-Regular, D-Ruim e E-Pessimo: ")

    opiniao = opiniao.upper()
    if opiniao =='A':
        qntdOtimo +=1
    if opiniao == 'E':
        porcentPessimo += 1
    if opiniao == 'B' and idade > maiorIdadeBom:
        maiorIdadeBom = idade

        somaIdade+=idade

    medIdade = somaIdade/100

    porcentPessimo = (porcentPessimo/100)*100

    print("Quantidade de respostas Ótimo: ", qntdOtimo)
    print("Média das idades: ", medIdade)
    print("Porcentagem de respostas Péssimo: ", porcentPessimo)
    print("Maior idade entre as pessoas que responderam Bom", maiorIdadeBom)