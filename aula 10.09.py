#INTERATIVO

# def fatorial(n):
#     if n < 0:
#         return "Fatorial de número negativo não existe"

#     resultado = 1
#     for i in range (1, n+1):
#         resultado *= i
#     return resultado

# resultado = fatorial(0)
# print(resultado)


# #Recursivo
# def fatorial_1 (n):
#     if n == 0 or n == 1:        
#         return 1
#     return n * fatorial_1(n-1)

# resultado = fatorial_1(5)
# print(resultado)



# import random
# import string

# def algoritimo(b, e):
#     if e == 0: 
#         return 1
#     return b * algoritimo(b, e-1)

# resultado = algoritimo(2, 4)
# print(resultado)

# def fibonacci(n):                            
#     if n<=1:                                 
#         return n                             
#     else:                                   
#         return fibonacci(n-1)+fibonacci(n-2)  

# resultado = fibonacci (7)
# print(resultado)

def somadig(n):
    if n == 0:
        return 0
    else:
        return somadig(n-1) + somadig(n+1)





# def palindromo(n):
#     if str(palindromo) == "".join(reversed(palindromo)):
#         return "Palindromo"
#     else:
#         return "Não é Palindromo"
    
# resultado = palindromo("ama")
# print(resultado)





    









