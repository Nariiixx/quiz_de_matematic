from random import choice, randrange
import time
import mysql.connector
from tabulate import tabulate
import bacn
from dotenv import load_dotenv
import os

class Quiz:
    
    def __init__(self):
        self.ponto = 0
        self.tempocorrido = 0
        self.nomedojogador =""
    def menu(self):
        while True:
            print("1. começar quiz\n2. sair\n3. ver pontuação")
            escolha = input("escolha uma opção:")
            if escolha == "1":
                print("iniciando quiz...")
                self.estagio1()
            elif escolha == "2":
                print("saindo do quiz...")
                exit()
            elif escolha == "3":
                load_dotenv()
                user = os.getenv("DB_USER")
                senha = os.getenv("DB_PASSWORD")
                host = os.getenv("DB_HOST")
                db = os.getenv("DB_NAME")
                conn = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=senha,
                    database=db
                )
                cursor = conn.cursor()
                
                cursor.execute("SELECT * FROM usuarios")
                dados = cursor.fetchall()
                tabela = [list(linha) for linha in dados]
                tabela.sort(key=lambda x: x[3], reverse=True)  # ordena por pontuação
                resultados = [["ID", "Nome", "Tempo (min)", "Pontuação"]] + tabela
                
                print(tabulate(resultados, headers="firstrow",tablefmt="grid"))
                
                cursor.close()
                conn.close()
                break
            else:
                print("opção inválida, tente novamente")
                self.menu()        
        
    def estagio1(self):
        self.nomedojogador = input("digite seu nome: ")
        print(f"Bem-vindo {self.nomedojogador} ao quiz de matemática!")
        print("o estagio 1 vai ser iniciado, é baseado em soma")
        inicio = time.perf_counter()
        i = 1
        while i <= 6:
            var = randrange(1, 999)
            var1 = randrange(1, 999)
            print("soma de dois numeros aleatórios")
            print(f"Questao {i}:")
            try:
                resposta = int(input(f"{var} + {var1} = "))
            except ValueError:
                print("entrada invalida, por favor insira um número inteiro.")
                continue
            soma = var + var1
            if resposta == soma:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print(f"tempo gasto no estagio 1: {self.tempocorrido:.2f} minutos")
        print(f"estagio 1 finalizado, você esta {self.ponto} pontos")
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
            print(f"Questao {i}:")
            try:
                resposta = int(input(f"{var}-{var1} = "))
            except ValueError:
                print("entrada invalida, por favor insira um número inteiro.")
                continue
            subtracao = var - var1
            if resposta == subtracao:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print(f"tempo gasto no estagio 2: {self.tempocorrido:.4f} minutos")
        print(f"estagio 2 finalizado, você esta {self.ponto} pontos")
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
            print(f"questao{i}:")
            try:
                resposta = int(input(f"{var} * {var1} = "))
            except ValueError:
                print("entrada invalida, por favor insira um número inteiro.")
                continue
            multiplicacao = var * var1
            if resposta == multiplicacao:
                print("resposta correta!")
                self.ponto+= 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print(f"tempo gasto no estagio 3: {self.tempocorrido:.2f} minutos")
        print(f"estagio 3 finalizado, você esta {self.ponto} pontos")
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
            print(f"Questao {i}:")
            resul= var / 2
            try:
                resposta = float(input(f"{var} / 2 = ".replace(',', '.')))
            except ValueError:
                print("entrada invalida, por favor insira um número decimal.")
                continue
            if resposta == resul:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print(f"tempo gasto no estagio 4: {self.tempocorrido:.2f} minutos")
        print(f"estagio 4 finalizado, você esta {self.ponto} pontos")
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
            print(f"Questao {i}:")
            try:
                resposta = int(input(f"{var} ** 2 = "))
            except ValueError:
                print("entrada invalida, por favor insira um número inteiro.")
                continue
            potencia = var ** 2
            if resposta == potencia:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print(f"tempo gasto no estagio 5: {self.tempocorrido:.2f} minutos")
        print(f"estagio 5 finalizado, você esta {self.ponto} pontos")
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
            print(f"Questao {i}:")
            raiz = var * var 
            try:
                resposta = float(input(f"raiz quadrada de {raiz} = ".replace(',', '.')))
            except ValueError:
                print("entrada invalida, por favor insira um número decimal.")
                continue
            if resposta == var:
                print("resposta correta!")
                self.ponto += 2.7777777778
            else:
                print("resposta errada!")
            i += 1
        fim = time.perf_counter()
        self.tempocorrido += (fim - inicio)/60
        print(f"tempo gasto no estagio 6: {self.tempocorrido:.2f} minutos")
        time.sleep(1)
        print(f"estagio 6 finalizado, você esta {self.ponto:.2f} pontos")
        
        esc=int(input("digite a opcao\n1-fim do quiz digite\n2-retornar ao menu: "))
        
        if esc == 1:
            print(f"fim do quiz, você terminou com {self.ponto:.2f} pontos, e com o tempo de {self.tempocorrido:.2f} minutos")
            bacn.banco(self.nomedojogador, self.tempocorrido, self.ponto)
            print("dados salvos no banco de dados")    
        elif esc == 2:
            self.menu()
        
    
    
    
jojo = Quiz()
jojo.menu()