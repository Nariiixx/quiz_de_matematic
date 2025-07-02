from random import choice, randrange
import time


class Quiz:
    
    def __init__(self):
        self.ponto = 0
        self.tempocorrido = 0
    def menu(self):
            print("1. começar quiz\n2. sair")
            escolha = input("escolha uma opção:")
            if escolha == "1":
                print("iniciando quiz...")
                self.estagio1()
            elif escolha == "2":
                print("saindo do quiz...")
                exit()
            else:
                print("opção inválida, tente novamente")
                self.menu()
    def estagio1(self):
        print("o estagio 1 vai ser iniciado, é baseado em soma")
        inicio = time.perf_counter()
        i = 1
        while i <= 6:
            var = randrange(1, 999)
            var1 = randrange(1, 999)
            print("soma de dois numeros aleatórios")
            print("Questao {}:".format(i))
            resposta = int(input("{} + {} = ".format(var, var1)))
            soma = var + var1
            if resposta == soma:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print("tempo gasto no estagio 1: {:.2f} minutos".format(self.tempocorrido))
        print("estagio 1 finalizado, você esta {} pontos".format(self.ponto))
        esc=int(input("digite a opcao\n1-proximo estagio digite\n2-retornar ao menu: "))
        if esc == 1:
            self.estagio2()
        elif esc == 2:
            self.menu()

    def estagio2(self):
        print("o estagio 2 vai comecar, será baseado em subtracao")
        i = 1
        inicio = time.perf_counter()
        while i <= 6:
            var = randrange(1, 999)
            var1 = randrange(1, 999)
            print("subtração de dois numeros")
            print("Questao {}:".format(i))
            resposta = int(input("{}-{} = ".format(var, var1)))
            subtracao = var - var1
            if resposta == subtracao:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print("tempo gasto no estagio 2: {:.2f} minutos".format(self.tempocorrido))
        print("estagio 2 finalizado, você esta {} pontos".format(self.ponto))
        esc=int(input("digite a opcao\n1-proximo estagio digite\n2-retornar ao menu: "))
        if esc == 1:
            self.estagio3()
        elif esc == 2:
            self.menu()
    def estagio3(self):
        print("o estagio 3 vai comecar sera baseado em multiplicação")
        i=1
        inicio = time.perf_counter()
        while i <=6:
            var = randrange(1,10)
            var1 = randrange(1,10)
            print("multiplicacao de dois numeros")
            print("questao{}:".format(i))
            resposta = int(input("{} * {} = ".format(var, var1)))
            multiplicacao = var * var1
            if resposta == multiplicacao:
                print("resposta correta!")
                self.ponto+= 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print("tempo gasto no estagio 3: {:.2f} minutos".format(self.tempocorrido))
        print("estagio 3 finalizado, você esta {} pontos".format(self.ponto))
        esc=int(input("digite a opcao\n1-proximo estagio digite\n2-retornar ao menu: "))
        if esc == 1:
            self.estagio4()
        elif esc == 2:
            self.menu()
    def estagio4(self):
        print("o estagio 4 vai comecar sera baseado em divisao")
        print("lembrando que o divisor de decimal no terminal é . e não ,")
        i = 1
        inicio = time.perf_counter()
        while i <= 6:
            var = randrange(1, 999)
            print("divisão de dois numeros")
            print("Questao {}:".format(i))
            resul= var / 2
            resposta = float(input("{} / 2 = ".format(var)))
            if resposta == resul:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print("tempo gasto no estagio 4: {:.2f} minutos".format(self.tempocorrido))
        print("estagio 4 finalizado, você esta {} pontos".format(self.ponto))
        esc=int(input("digite a opcao\n1-proximo estagio digite\n2-retornar ao menu: "))
        if esc == 1:
            self.estagio5()
        elif esc == 2:
            self.menu()
    def estagio5(self):
        print("o estagio 5 vai comecar sera baseado em potencias")
        i = 1
        inicio = time.perf_counter()
        while i <= 6:
            var = randrange(1, 10)
            print("potencia de um numero")
            print("Questao {}:".format(i))
            resposta = int(input("{} ** 2 = ".format(var)))
            potencia = var ** 2
            if resposta == potencia:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print("tempo gasto no estagio 5: {:.2f} minutos".format(self.tempocorrido))
        print("estagio 5 finalizado, você esta {} pontos".format(self.ponto))
        esc=int(input("digite a opcao\n1-proximo estagio digite\n2-retornar ao menu: "))
        if esc == 1:
            self.estagio6()
        elif esc == 2:
            self.menu()
    def estagio6(self):
        print("o estagio 6 vai comecar sera baseado em radiciação")
        i = 1
        inicio = time.perf_counter()
        while i <= 6:
            var = randrange(1, 10)
            print("raiz quadrada de um numero")
            print("Questao {}:".format(i))
            raiz = var * var 
            resposta = float(input("raiz quadrada de {} = ".format(raiz)))
            if resposta == var:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print("tempo gasto no estagio 6: {:.2f} minutos".format(self.tempocorrido))
        time.sleep(1)
        print("estagio 6 finalizado, você esta {} pontos".format(self.ponto))
        esc=int(input("digite a opcao\n1-fim do quiz digite\n2-retornar ao menu: "))
        if esc == 1:
            print("fim do quiz, você terminou com {} pontos, e com o tempo de {} minutos".format(self.ponto, self.tempocorrido))
            exit()
        elif esc == 2:
            self.menu()
    
jojo = Quiz()
jojo.menu()