livro = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def ampli():
    #calcula a amplitude do livro
    #a amplitude é a diferença entre o maior e o menor número
    print("amplitude do livro: ", max(livro) - min(livro))
    print("maior numero do livro: ", max(livro))
    print("menor numero do livro: ", min(livro))
    print("soma dos numeros do livro: ", sum(livro))
    print("media dos numeros do livro: ", sum(livro) / len(livro))
    print("quantidade de numeros no livro: ", len(livro))
#ampli()
    
livr = "python"    
def imprime(x):
    #imprime uma string letra por letra
    for i in range(len(x)):
        print(x[i])
#imprime(livr)


def peso():
    peso = int(input("digite seu peso: "))
    peso1 = peso * 5
    if peso <= 10:
        print(f"o valor a ser pago é {peso1} reais")
    elif peso > 11 and peso <=20:
        print(f"o valor a ser pago é {peso1} reais")
    elif peso > 20:
        print("transporte não é aceito")
        
#peso()