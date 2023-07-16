# A notação do dia:
# fiz o triangulo e arrumei as cores e erros de digitação
# FAZER O TRIANGULO EQUILATERO

# problema: Linha 144 problema de ponto flutuante

from clear import clear
from math import pow

vermelho = '\033[1;31m'  # Erro
fim = '\033[m'

qual = input('Qual calculadora você deseja utilizar?:\n[1] 2ºGrau\n[2] área\nR:')

# Repete até a arfimação ser verdadeira
while not qual in ['1', '2']:
    print(f'{vermelho}Invalido, por favor responda 1 ou 2 {fim}')
    qual = input('Qual calculadora você deseja utilizar?:\n[1] 2ºGrau\n[2] área\nR:')
    clear()  # Exclui do termianal todas as informações presentes

if qual == '1':

    a, b, c = [int(i) for i in input('\ninforme a,b e c: ').split(' ')]

    potencia = b ** 2
    xaxc = 4 * a * c
    delta = potencia - xaxc
    raiz = delta ** 0.5
    numeradorx1 = -b + raiz
    numeradorx2 = -b - raiz
    denominador = 2 * a
    X1 = numeradorx1 / denominador
    X2 = numeradorx2 / denominador

    print("\nΔ = b^2 – 4ac")
    print(f"Δ ={b}^2 - 4x{a}x{c}")
    print(f"Δ ={potencia} - {xaxc}")
    print(f"Δ ={delta}\n")

    if delta < 0:
        print("\nS = Ø ")
    else:

        print('''x = -b ± √Δ 
        2.a
         ''')

        print(f'''x = {-b} ± {raiz}
        {denominador}
        ''')
        print(f'''X1 = {-b} + {raiz}
         {denominador}
        ''')

        print(f'''X1 = {numeradorx1}
        {denominador}
    ''')
        print(f"X1 = {numeradorx1 / denominador}\n")
        print(f'''X2 = {-b} - {raiz}
         {denominador}
         ''')

        print(f'''X2 = {numeradorx2} 
        {denominador}
    ''')
        print(f"X2 = {numeradorx2 / denominador}\n")
        if X1 == X2:
            print(f"S = {X1}")
        else:
            print(f" S = {X1, X2}")
            exit()

# Fim do 2 Grau e começo da Área

elif qual == '2':
    clear()
    escolha = input('Qual área você deseja medir?\n[1]guadrado\n[2]retangulo\n[3]Tringulo\nR:')

    while escolha not in ['1', '2', '3']:
        print(f'{vermelho}Invalido, por favo responda 1,2 ou 3{fim}')
        escolha = input('Qual áre você deseja medir?\n[1]guadrado\n[2]retangulo\n[3]Tringulo\nR:')
        clear()

    if escolha == '1':  # Área do guadrado

        area = int(input('\nInforma a medida do guadrado: '))

        print(f'''A = l.l
A = {area}.{area}
A = {pow(area, 2)}''')

    elif escolha == '2':  # Área do retângulo

        medida, medida02 = [int(i) for i in input('\nqual medida do B e do H do retangulo: ').split(' ')]

        print(f'''A = b.h
A = {medida}.{medida02}1
A = {medida * medida02}''')

    elif escolha == '3':

        triangulo = input('\nO triangulo é:\n[1]Triângulo retangulo\n[2]Triângulo equilátero\nR:')

        while triangulo not in ['1', '2']:
            print(f'{vermelho}Invalido, por favor responda 1 ou 2\n{fim}')
            triangulo = input('O triangulo é:\n[1]Triângulo retangulo\n[2]Triângulo equilátero\nR:')
            clear()

        if triangulo == '1':  # Área do triângulo Retangulo

            b, h = [float(i) for i in input('\nInforma b e o h:(Na mesma linha e com espaço): ').split(' ')]

            print(f'''A = b.h
     2

A = {b}.{h}
     2

A = {b * h}
    2

A = {(b * h) / 2}''')

        else:  # Área do triângulo equilatero

            base, h = [float(i) for i in input('\nInforme a base (Valor inteiro) e a hipotensa: ').split(' ')]
            a = h * h
            b = base * base / 4
            altura = (a - b) ** 0.5

            print(f'''
{altura}= h

A = {b} x {altura} / 2

A= {(base * altura) / 2}''')