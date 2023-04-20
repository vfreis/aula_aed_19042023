
# XI - Faça um algoritimo que verifique entre dois números quem é o maior.
def ex_11(n1, n2):
    if n1 == n2:
        return 'números iguais'
    elif n1 > n2:
        return 'numero 1 é maior'
    else:
        return 'numero 2 é maior'

# XII - Faça um algoritimo que verifique se um número é par ou impar.
def ex_12(n1):
    if n1 % 2 == 0:
        return True
    else:
        return False

# XIII - Escreva um código que pergunte o salário de um funcionário e depois aplique um aumento salárial.
# Para valores menores ou iguais a 2600 reais aplicar um aumento de 7,2% mais um fixo de 200 reais e para um salário maior que 2600 reais aplicar um aumento de 5,9% mais um fixo de 300 reais.
def ex_13(salario):
    if salario <= 2600:
        fixo = 200
        salario_novo = salario + ((salario/100) * 7.6) + fixo
        return salario_novo
    if salario > 2600:
        fixo = 300
        salario_novo = salario + ((salario/100)* 5.9) + fixo
        return salario_novo

# XIV - Elabore um programa que calcule o valor do desconto que o funcionário assalariado terá em seu salário seguindo a tabela abaixo 
# até  1.903,98 => Isento.
# de  1.903,99 a  2.826,65 => 7,5% -  142,80.
# de  2.826,66 a  3.751,05 => 15% -  354,80.
# de  3.751,06 a  4.664,68 => 22,5% -  636,13.
# acima de  4.664,68 - 27,5% =>  869,36.

# salario * % imposto da fx - desconto_base
def ex_14(salario):
    if salario <= 1903.98:
        return 0
    elif salario > 1903.98 and salario <= 2826.65:
        percentual_imposto = 7.5
        desconto_base = 142.80
        imposto = ((percentual_imposto / 100) * salario) - desconto_base
        return imposto
    elif salario > 2826.65 and salario <= 3751.05:
        percentual_imposto = 15
        desconto_base = 354.80
        imposto = ((percentual_imposto / 100) * salario) - desconto_base
        return imposto
    elif salario > 3751.05 and salario <= 4664.68:
        percentual_imposto = 22.5
        desconto_base = 636.13
        imposto = ((percentual_imposto / 100) * salario) - desconto_base
        return imposto
    elif salario > 4664.68:
        percentual_imposto = 27.5
        desconto_base = 869.36
        imposto = ((percentual_imposto / 100) * salario) - desconto_base
        return imposto



# XV - Biblioteca math

# Essa biblioteca é necessária quando precisarmos fazer cálculos com funções 
# trigonométricas, logarítmicas, exponenciais, raízes.

# syntax

# import math as ma

# x = ma.pi

# Elabore um algoritmo que calcule a aréa de uma circunferência dado o raio

# Área da circunferência = $\pi.r^2$

# De sua resposta com 4 casas decimais de precisão
def ex_15(raio):
    import math as ma
    pi = ma.pi
    area_circunferencia = pi * raio**2
    return round(area_circunferencia, 2)

# Biblioteca Numpy

# NumPy, que significa Numerical Python, é uma poderosa biblioteca da linguagem de programação Python, que consiste em objetos chamados de arrays (matrizes), que são multidimensionais. Além disso, essa biblioteca vem com uma coleção de rotinas para processar esses arrays.

# import numpy as np

# XV - Elabore um programa que resolva a equação do 2° grau através da formula de Bhaskara

# $x=\frac{-b\ \pm \sqrt{\Delta}}{2.a}$

# $\Delta = b^2-4.a.c$

# Se $\Delta < 0$  informar ao usuário que a equação não tem raiz pois não existe raiz de número negativo.


def ex_16(a, b, c):
    import numpy as np
    delta = (b ** 2) - (4 * a * c)
    if delta < 0: 
        return False
    else:
        raiz_1 = (-b + np.sqrt(delta))/(2 * a)
        raiz_2 = (-b - np.sqrt(delta))/(2 * a)
        return round(raiz_1, 4), round(raiz_2, 4)

# Exercicio XVI
# Vamos agora estudar as estruturas de repetição
# While
# for
# Imprimir os 5 primeiros números positivos

def ex_17_gerarinteiros(qtd):
    i = 1
    while(i<=qtd):
        print(i)
        i += 1


 
