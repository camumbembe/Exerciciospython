#exercicio 26:
# for element in range(1, 11):
#     print(element)


#exercicio 27:
# def aceleration(v1,v2,t1,t2):
#     a= (v2-v1)/(t2-t1)
#     return a

# print(aceleration(0,10,0,20))

#exercicio 28:
# def foo(a, b):
#     return a + b

# x = foo(2, 3) * 10

#exercicio 29:
# from math import pi
# def liqdvol(h, r=10):
#     v = (4*pi * r**3)/3 - (pi *h**2* (3*r-h) /3)
#     return v
# print(liqdvol(2))


#exercicios 30 ao 33 feitos mentalmente

#exercicio 34:
# def foo(): 
#     global c
#     c = 1 
#     return c 
# foo()
# print(c)
# print(foo())

#exercicio 35:
# def frase():
#     compr = input('Informe sua frase: ')
#     contando = compr.split(' ')
#     resultado = len(contando)
#     print('Sua frase tem', resultado, 'palavras')
#     return resultado
# frase()


#exercicio 36:
# def countwords(filename):
#     with open(filename, 'r') as file:
#         separar_texto = file.read()
#         separar = separar_texto.split(' ')
#         palvras = len(separar)
#         print('O arquivo contém', palvras, 'palavras')
#         return palvras
# countwords('words1.txt')


#exercicio 37:
# def countwords(filename):
#     with open(filename, 'r') as file:
#         separar_texto = file.read()
#         separar = separar_texto.replace(',', '').split(' ')
#         print(separar)
#         palvras = len(separar)
#         print('O arquivo contém', palvras, 'palavras')
#         return palvras
# countwords('words1.txt')

#exercico 38 mental

#exercicio 39 e 40:
# import math
# # print(math.cos(1))
# import math
# print(math.pow(2,2))

#exercicio 41:
# file = open('letras.txt', 'w')
# alfa = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
# for i in alfa:
#     resultado = file.write(i + '\n')
# file.close()

#exercicio 42:
# a = [1, 2, 3]
# b = (4, 5, 6)
# posicao = 0
# for i in a:    
#     soma = i + b[posicao]
#     print(soma)
#     posicao +=1
# #resposta usando zip
# for i, j in zip(a,b):
#     print(i+j)

#exercicio 43:
# import string
# with open("alfabet.txt", "w") as file:
#     for i, j in zip(string.ascii_lowercase[0::2],string.ascii_letters[1::2] ):
#        file.write(i + j + "\n")


#exercicio 44:
# import string
# with open("alfabety.txt", "w") as file:
#     for i, j, z in zip(string.ascii_lowercase[0::2],string.ascii_letters[1::2],string.ascii_letters[2::2] ):
#        file.write(i + j + z + "\n")


#exercicio 45:
# import string
# for i in string.ascii_lowercase:
#     file = open(i+'.txt', 'w')
#     file.write(i)
#     file.close()


#exercicio 46:
# import glob
# a = []
# for i in glob.glob('*.txt'):
#     with open(i, 'r') as linhas:
#         linha = linhas.readline()
#         a.append(linha)
# print(a)


#exercicio 47:
# import glob
# a = []
# for i in glob.glob('*.txt'):
#     with open(i, 'r') as linhas:
#         linha = linhas.readline()
#         if linha in 'python':
#             a.append(linha)
# print(a)

#exercicio 48:
# for letter in "Hello":
#     if letter == "e":
#         print(letter)


#exercicio 49:
# password = input("Please enter your password: ") 


#exercicio 50:
# age = input("What's your age? ")
# age_last_year = int(age) - 1
# print("Last year you were %s." % age_last_year)
