from os import system
import math

def entrarlista():
    print(" +------------------------------------------------+")
    print(" |1 - Estrutura Sequencial           (18 questões)|")
    print(" |------------------------------------------------|")
    print(" |2 - Estrutura de Decisão           (28 questões)|")
    print(" |------------------------------------------------|")
    print(" |3 - Estrutura de Repetição         (51 questões)|")
    print(" |------------------------------------------------|")
    print(" |4 - Agrupamento de obj. (vetores)  (24 questões)|")
    print(" |------------------------------------------------|")
    print(" |5 - Funções                        (14 questões)|")
    print(" +------------------------------------------------+")
    lista = int(input(" Digite qual lista deseja consultar: "))
    #while lista >= 1 and x <= 5:
    if lista == 1:
        lista1()

    elif lista == 2:
        lista2()

    elif lista == 3:
        lista3()

    elif lista == 4:
        lista4()

    elif lista == 5:
        lista5()

    elif lista > 5:
        system("cls")
        entrarlista()

    elif lista <= 0:
        system("cls")
        entrarlista()


    return ""

def sairlista():
    escolha = int(input("\n Deseja sair do programa? 0 - Sim/ 1 - Não: " ))
    system("cls")
    if escolha >= 1:
        entrarlista()
    else:
        print(" Obrigado pela sua presença!")
    return ""


def lista1():
    lista1 = int(input(" Digite qual das 18 questões você deseja consultar: "))
    system("cls")
    if lista1 == 1:
        print("\nFaça um Programa que mostre a mensagem 'Alo mundo' na tela.\n\n","="*40,"1","="*40,"\n")
        print("Alô mundo.")

    elif lista1 == 2:
        print("\nFaça um Programa que peça um número e então mostre a mensagem O número informado foi [número]\n\n","="*40,"2","="*40,"\n")
        n1 = int(input("Digite um número: "))
        print("O número informado foi: {}.".format(n1))

    elif lista1 == 3:
        print("\nFaça um Programa que peça dois números e imprima a soma\n\n","="*40,"3","="*40,"\n")
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite um número: "))
        soma = n1+n2
        print("A soma de",n1,"+",n2,"= {}.".format(soma))

    elif lista1 == 4:
        print("\nFaça um Programa que peça as 4 notas bimestrais e mostre a média.\n\n","="*40,"4","="*40,"\n")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        nota4 = float(input("Digite a quarta nota: "))
        media = (nota1+nota2+nota3+nota4)/4
        print ("A média é: {}.".format(media))

    elif lista1 == 5:
        print("\nFaça um Programa que converta metros para centímetros.\n\n","="*40,"5","="*40,"\n")
        metro = float(input("Digite quantos metros deseja converter: "))
        cm = metro*100
        print(metro,"m equivale a {} cm.".format(cm))

    elif lista1 == 6:
        print("\nFaça um Programa que peça o raio de um círculo, calcule e mostre sua área.\n\n","="*40,"6","="*40,"\n")
        raio = float(input("Digite o tamanho do raio:"))
        area = math.pi*pow(raio,2)
        print("A área do circulo é {}.".format(area))

    elif lista1 == 7:
        print("\nFaça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.\n\n","="*40,"7","="*40,"\n")
        lado = float(input("Digite o lado do quardrado: "))
        area = lado*lado
        print("A área do quadrado é:",area,"e o seu dobro é: {}.".format(area*2))

    elif lista1 == 8:
        print("\nFaça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.\nCalcule e mostre o total do seu salário no referido mês.\n\n","="*40,"8","="*40,"\n")
        salhora = float(input("Digite o quanto você ganha por hora: "))
        horames = int(input("Digite a quantidade de horas trabalhadas no mês: "))
        salmes = salhora*horames
        print("O salário no referido mês é: R$ {}.".format(salmes))

    elif lista1 == 9:
        print("\nFaça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura\nem graus Celsius.\nC = 5 * ((F-32) / 9).\n\n","="*40,"9","="*40,"\n")
        F = float(input("Digite a temperatura em graus Fahrenheit: "))
        C = 5*((F-32)/9)
        print("A temperatura em graus Celsius é: {:.2f}º Celsius".format(C))

    elif lista1 == 10:
        print("\nFaça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.\n\n","="*40,"10","="*40,"\n")
        C = float(input("Digite a temperatura em graus Celsius: "))
        F = C*1.8
        print("A temperatura em graus Fahrenheit é: {:.2f}º Fahrenheit".format(F))

    elif lista1 == 11:
        print("\nFaça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:\na. o produto do dobro do primeiro com metade do segundo.\nb. a soma do triplo do primeiro com o terceiro.\nc. o terceiro elevado ao cubo.\n\n","="*40,"11","="*40,"\n")
        n1 = int(input("Digite o primeiro número inteiro: "))
        n2 = int(input("Digite o segundo número inteiro: "))
        n3 = float(input("Digite o terceiro número real: "))

        a = (n1*2)*(n2/2)
        b = (n1*3) + n3
        c = math.pow(n3,3)

        print("Solução A: {}.".format(a))
        print("Solução B: {:.2f}.".format(b))
        print("Solução C: {:.2f}.".format(c))

    elif lista1 == 12:
        print("\nTendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,\nusando a seguinte fórmula: (72.7*altura) - 58\n\n","="*40,"12","="*40,"\n")
        altura = float(input("Digite a sua altura: "))

        pesoIdeal = (72.7*altura)-58

        print("O peso ideal é: {:.2f}.".format(pesoIdeal))

    elif lista1 == 13:
        print("\nTendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,\nutilizando as seguintes fórmulas:\na. Para homens: (72.7*h) - 58\nb. Para mulheres: (62.1*h) - 44.7\n\n","="*40,"13","="*40,"\n")
        sexo = str(input("Digite F para sexo Feminino e M para sexo Masculino: "))
        h = float(input("Digite a sua altura: "))
        if sexo == 'F' or sexo == 'f':
            pesoIdeal = (62.1*h) - 44.7
            print("O peso ideal feminino neste caso é: {:.2f}.".format(pesoIdeal))
        elif sexo == 'M' or sexo == 'm':
            pesoIdeal = (72.7*h)-58
            print("O peso ideal masculino neste caso é: {:.2f}.".format(pesoIdeal))

    elif lista1 == 14:
        print("\nJoão Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.\nToda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo\n(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.\nJoão precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.\nGravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.\nImprima os dados do programa com as mensagens adequadas.\n\n","="*40,"14","="*40,"\n")
        peso = float(input("Digite peso de peixes: "))
        if peso > 50:
            excesso = peso - 50
            multa = excesso * 4
            print("O excesso é: {}kg".format(excesso),"e a multa é no valor de: R$ {}.".format(multa))
        else:
            print("Não houve peso excedente desta vez.")

    elif lista1 == 15:
        print("\nFaça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre\no total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8%% para o\nINSS e 5%% para o sindicato, faça um programa que nos dê:\n\na. salário bruto.\nb. quanto pagou ao INSS.\nc. quanto pagou ao sindicato.\nd. o salário líquido.\ne. calcule os descontos e o salário líquido, conforme a tabela abaixo:\n\n+ Salário Bruto : R$\n- IR (11%) : R$\n- INSS (8%) : R$\n- Sindicato ( 5%) : R$\n= Salário Liquido : R$\n\nObs.: Salário Bruto - Descontos = Salário Líquido.\n\n","="*40,"15","="*40,"\n")
        salhora = float(input("Digite o quanto você ganha por hora: "))
        horames = int(input("Digite a quantidade de horas trabalhadas no mês: "))
        salmes = salhora * horames
        inss = salmes*0.11
        ir = (salmes-inss)*0.08
        sindicato = (salmes-(ir+inss))*0.05
        salliquido = salmes-(ir+inss+sindicato)
        print("Salário Bruto: R$ {:.2f}.".format(salmes))
        print("Valor pago ao INSS: R$ {:.2f}.".format(inss))
        print("Valor pago ao Imposto de Renda: R$ {:.2f}.".format(ir))
        print("Valor pago ao Sindicato: R$ {:.2f}.".format(sindicato))
        print("Salário líquido: R$ {:.2f}.".format(salliquido))


    elif lista1 == 16:
        print("\n Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.\nConsidere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida\nem latas de 18\ litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem\ncompradas e o preço total.\n\n","="*40,"1","="*40,"\n")
        areapintada = float(input("Digite o tamanho em m² da área a ser pintada: "))
        qtdlitros = areapintada / 3
        latas = math.ceil(qtdlitros/18)
        valortotal = latas*80.0
        print("Quantidade de latas de tintas: {:.0f}.".format(latas),"\nTotal a pagar: {:.2f}".format(valortotal))

    elif lista1 == 17:
        print("\n Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área\na ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é\nvendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.\n\nInforme ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:\n* comprar apenas latas de 18 litros;\n* comprar apenas galões de 3,6 litros;\n* misturar latas e galões, de forma que o desperdício de tinta seja menor.\nAcrescente 10%% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.\n\n","="*40,"17","="*40,"\n")
        areapintada = float(input("Digite o tamanho em m² da área a ser pintada: "))
        qtdlitros = (areapintada/6)*1.1

        latas = math.ceil(qtdlitros/18)
        valortotalLatas = latas * 80.0
        galoes = math.ceil(qtdlitros/3.6)
        valortotalGaloes = galoes * 25

        # MISTURA LOUCA TESTE

        latamistas = math.trunc(qtdlitros/18)
        galaomistos = math.ceil(qtdlitros - latamistas*18)/3.6
        totalmisto = (latamistas * 80) + (galaomistos* 25)

        print("\n Quantidade de latas de tintas: {:.0f}.".format(latas), "\n Total a pagar pelas latas: {:.2f}".format(valortotalLatas))
        print("\n Quantidade de galoes de tintas: {:.0f}.".format(galoes), "\n Total a pagar pelos galões: {:.2f}".format(valortotalGaloes))
        print("\n Quantidade de galoes de tintas: {:.0f}.".format(math.ceil(galaomistos)),"\n Quantidade de latas de tintas: {:.0f}.".format(latamistas),"\n Total a pagar pelos galões e latas de tintas: {:.2f}".format(totalmisto))

    elif lista1 == 18:
        print("\n Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet\n(em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).\n\n","="*40,"18","="*40,"\n")
        tamAquivo = float(input(" Digite o tamanho do arquivo para download em MB: "))
        Mbps = float(input(" Digite a velocidade de internet: "))
        TempoaproxDown = ((tamAquivo*8)/Mbps)/60
        print(" O tempo de download aproximadamente é: {:.2f} minutos.".format(TempoaproxDown))

    elif lista1 > 18:
        entrarlista()

    return sairlista()

def lista2():
    lista2 = int(input(" Digite qual das 28 questões você deseja consultar: "))
    system("cls")
    if lista2 == 1:
        print("\n Faça um Programa que peça dois números e imprima o maior deles.\n\n","="*40,"1","="*40,"\n")
        n1 = int(input(" Digite um número: "))
        n2 = int(input(" Digite outro número: "))
        if n1 > n2:
            print("\n",n1,"é o maior número.")
        elif n1 < n2:
            print("\n",n2,"é o maior número.")
        else:
            print("\n Os números são iguais.")

    elif lista2 == 2:
        print("\n Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.\n\n","="*40,"2","="*40,"\n")
        n1 = int(input(" Digite outro número: "))
        if n1 > 0:
            print("\n O número é positivo.")
        elif n1 < 0:
            print("\n O número é negativo.")
        else:
            print("\n O número é neutro.")

    elif lista2 == 3:
        print("\n Faça  um  Programa  que  verifique  se  uma  letra  digitada  é  'F'  ou  'M'.  Conforme  a  letra\n escrever:  F  -  Feminino,  M  - Masculino, Sexo Inválido.\n\n======================================== 3 =============================================")
        sexo = str(input(" Digite F para feminino ou M para Masculino: "))
        if sexo == "F" or sexo == "f":
            print(" F - Feminino.")

        elif sexo == "m" or sexo == "M":
            print(" M - Masculino.")

        else:
            print(" Sexo Inválido.")

    elif lista2 == 4:
        print("\n Faça um Programa que verifique se uma letra digitada é vogal ou consoante. \n\n","="*40,"4","="*40,"\n\n")
        letra = str(input (" Digite uma letra: "))
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra ==  'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            print("\n A letra é uma vogal.")
        else:
            print("\n A letra é uma consoante.")

    elif lista2 == 5:
        print("\n Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média \n alcançada por aluno e apresentar: \n A mensagem 'Aprovado', se a média alcançada for maior ou igual a sete; \n A mensagem 'Reprovado', se a média for menor do que sete;\n A mensagem 'Aprovado com Distinção', se a média for igual a dez.\n\n","="*40,"5","="*40,"\n")
        nota1 = float(input(" Digite a primeira nota: "))
        nota2 = float(input(" Digite a segunda nota: "))
        media = (nota1+nota2)/2
        if media >=7 and media < 10:
            print("\n Media: {:.2f}.\n Aprovado. ".format(media))

        elif media < 7:
          print("\n Media: {:.2f}.\n Reprovado.  ".format(media))

        elif media == 10:
            print("\n Media: {:.2f}.\n Aprovado com Distinção.".format(media))

    elif lista2 == 6:
        print("\n Faça um Programa que leia três números e mostre o maior deles.\n\n","="*40,"6","="*40,"\n\n")
        n1 = float(input(" Digite o primeiro número: "))
        n2 = float(input(" Digite o segundo número: "))
        n3 = float(input(" Digite o terceiro número: "))

        if n1 >= n2 and n2 >= n3 and n1 >= n3:
            print("\n {:.1f} é o maior número.".format(n1))
        elif n2 >= n1 and n1 >= n3 and n2 >= n3:
            print("\n {:.1f} é o maior número.".format(n2))
        elif n3 >= n2 and n2 >= n1 and n3 >= n1:
            print("\n {:.1f} é o maior número.".format(n3))

        elif n1 >= n2  and  n1 >= n3:
            print("\n {:.1f} é o maior número.".format(n1))

        elif n2 >= n1  and  n2 >= n3:
            print("\n {:.1f} é o maior número.".format(n2))

        elif n3 >= n2  and  n3 >= n1:
            print("\n {:.1f} é o maior número.".format(n3))


    elif lista2 == 7:
        print("\n Faça um Programa que leia três números e mostre o maior e o menor deles.  \n\n","="*40,"7","="*40,"\n")
        n1 = float(input(" Digite o primeiro número: "))
        n2 = float(input(" Digite o segundo número: "))
        n3 = float(input(" Digite o terceiro número: "))

        if n1>n2 and n1>n3:
            if n2>n3:
                print(" Maior número: {}\n Menor número: {}.\n".format(n1,n3))
            else:
                print(" Maior número: {}\n Menor número: {}.\n".format(n1, n2))
        if n2>n1 and n2>n3:
            if n1 > n3:
                print(" Maior número: {}\n Menor número: {}.\n".format(n2, n3))
            else:
                print(" Maior número: {}\n Menor número: {}.\n".format(n2, n1))
        if n3 > n1 and n3 > n2:
            if  n1 > n2:
                 print(" Maior número:{}\n Menor número: {}\n.".format(n3, n2))
            else:
                print(" Maior número:{}\n Menor número: {}\n.".format(n3, n1))

        if n1 == n2 or n1 == n3 or n2==n3:
             print("\n Tente com números distintos da próxima vez.")


    elif lista2 == 8:
        print("\n Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,\n sabendo que a decisão é sempre pelo mais barato.\n\n","="*40,"8","="*40,"\n")
        p1 = float(input(" Digite o valor do 1º produto: "))
        p2 = float(input(" Digite o valor do 2º produto: "))
        p3 = float(input(" Digite o valor do 3º produto: "))
        if p1 <= p2 and p1 <= p3 :
            print("\n O produto com valor: R${} é o mais barato.".format(p1))
        elif p2 <= p1 and p2 <= p3:
            print("\n O produto com valor: R${} é o mais barato.".format(p2))
        elif p3 <= p1 and p3 <= p2:
            print("\n O produto com valor: R${} é o mais barato.".format(p3))





    elif lista2 == 9:
        print("\n\n")
    elif lista2 == 10:
        print("\nn")
    elif lista2 == 11:
        print("\n\n")
    elif lista2 == 12:
        print("\n\n")
    elif lista2 == 13:
        print("\n\n")
    elif lista2 == 14:
        print("\n\n")
    elif lista2 == 15:
        print("\n\n")
    elif lista2 == 16:
        print("\n\n")
    elif lista2 == 17:
        print("\n\n")
    elif lista2 == 18:
        print("\n\n")
    elif lista2 == 19:
        print("\n\n")
    elif lista2 == 20:
        print("\n\n")
    elif lista2 == 21:
        print("\n\n")
    elif lista2 == 22:
        print("\n\n")
    elif lista2 == 23:
        print("\n\n")
    elif lista2 == 24:
        print("\n\n")
    elif lista2 == 25:
        print("\n\n")
    elif lista2 == 26:
        print("\n\n")
    elif lista2 == 27:
        print("\n\n")
    elif lista2 == 28:
        print("\n\n")




    return sairlista()

def lista3():
    lista3 = int(input("Digite qual das 51 questões você deseja consultar: "))
    system("cls")
    if lista3 == 1:
        print("\n Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e\ncontinue pedindo até que o usuário informe um valor válido.\n")
    elif lista3 == 1:
        print("\n \n")

    elif lista3 == 2:
        print("\n \n")

    elif lista3 == 3:
        print("\n \n")

    elif lista3 == 4:
        print("\n \n")

    elif lista3 == 5:
        print("\n \n")

    elif lista3 == 6:
        print("\n \n")

    elif lista3 == 7:
        print("\n \n")
    elif lista3 == 8:
        print("\n\n")
    elif lista3 == 9:
        print("\n\n")
    elif lista3 == 10:
        print("\nn")
    elif lista3 == 11:
        print("\n\n")
    elif lista3 == 12:
        print("\n\n")
    elif lista3 == 13:
        print("\n\n")
    elif lista3 == 14:
        print("\n\n")
    elif lista3 == 15:
        print("\n\n")
    elif lista3 == 16:
        print("\n\n")
    elif lista3 == 17:
        print("\n\n")
    elif lista3 == 18:
        print("\n\n")
    elif lista3 == 19:
        print("\n\n")
    elif lista3 == 20:
        print("\n\n")
    elif lista3 == 21:
        print("\n\n")
    elif lista3 == 22:
        print("\n\n")
    elif lista3 == 23:
        print("\n\n")
    elif lista3 == 24:
        print("\n\n")
    elif lista3 == 25:
        print("\n\n")
    elif lista3 == 26:
        print("\n\n")
    elif lista3 == 27:
        print("\n\n")
    elif lista3 == 28:
        print("\n\n")

    elif lista3 == 29:
        print("\n \n")

    elif lista3 == 30:
        print("\n \n")
    elif lista3 == 31:
        print("\n\n")
    elif lista3 == 32:
        print("\n\n")
    elif lista3 == 33:
        print("\nn")
    elif lista3 == 34:
        print("\n\n")
    elif lista3 == 35:
        print("\n\n")
    elif lista3 == 36:
        print("\n\n")
    elif lista3 == 37:
        print("\n\n")
    elif lista3 == 38:
        print("\n\n")
    elif lista3 == 39:
        print("\n\n")
    elif lista3 == 40:
        print("\n\n")
    elif lista3 == 41:
        print("\n\n")
    elif lista3 == 42:
        print("\n\n")
    elif lista3 == 43:
        print("\n\n")
    elif lista3 == 44:
        print("\n\n")
    elif lista3 == 45:
        print("\n\n")
    elif lista3 == 46:
        print("\n\n")
    elif lista3 == 47:
        print("\n\n")
    elif lista3 == 48:
        print("\n\n")
    elif lista3 == 49:
        print("\n\n")
    elif lista3 == 50:
        print("\n\n")
    elif lista3 == 51:
        print("\n\n")



    return sairlista()
def lista4():
    lista4 = int(input("Digite qual das 24 questões você deseja consultar: "))
    system("cls")
    if lista4 == 1:
        print("\nFaça um Programa que leia um vetor de 5 números inteiros e mostre-os\n")

    return sairlista()


def lista5():
    lista5 = int(input("Digite qual das 14 questões você deseja consultar: "))
    system("cls")
    if lista5 == 1:
        print("")
    return sairlista()


entrarlista()