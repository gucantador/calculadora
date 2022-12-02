from math import exp, log10, sin, cos, tan, factorial, degrees, sqrt, log10


class calculadora():

    def __init__(self):  # CONSTRUTOR INICIA AS OPERAÇÕES
        resultado = 0
        print("BEM VINDOA CALCULADORA\n*******************************")
        self.listar_operacoes()  # METODO QUE LISTA AS OPERAÇÕES, FORA DO WHILE PARA INICIALIZAR A PRIMEIRA VEZ
        while True:
            try:  # PARA O CODIGO NAO QUEBRAR POR ERRO DE INPUT DO USUARIO
                resultado = self.rodar(
                    resultado)  # VARIAVEL RESULTADO INICIADA COM 0 A CIMA, MAS DEPOIS RECEBE DO LOOPING IFINITO
                if resultado == "break":
                    break

                if resultado == "listar":
                    self.listar_operacoes()  # METODO PARA LISTAR OPERAÇÕES CASO DESEJADO PELO USUARIO
                else:
                    print('%.2f' % resultado)
            except:  # INFORMA O USUARIO QUE ELE REALIZOU UM INPUT ERRADO
                print("Houve algum erro de input, verifique as instruções")
                pass

    def prin_finan():  # 'PRINT' DEDICADO PARA CALCULADORA FINANCEIRA
        x = float(input("Montante Inicial (R$): "))
        y = float(input("Taxa de Juros (%): "))
        z = float(input("Periodo (mês): "))
        return (x, y, z)

    def listar_operacoes(self):  # METODO QUE LISTA OPERAÇÕES
        print("1 - somar")
        print("2 - subtrair")
        print("3 - multiplicar")
        print("4 - dividir")
        print("5 - elevar ao quadrado")
        print("6 - raiz quadrada")
        print("7 - elevar a x")
        print("8 - raiz x")
        print("9 - log base 10")
        print("10 - fatorial")
        print("11 - sen")
        print("12 - cos")
        print("13 - tg")
        print("14 - juros simples")
        print("15 - juros compostos")

    def rodar(self, res):  # METODO QUE RODA O CODIGO, CONDIÇÕES DE OPÇÕES DO USUARIO

        a = int(input("Escolha sua operação, digite 0 para encerrar ou 45 para listar operações: "))

        if a == 45:
            return "listar" # RETORNA LISTAR QUE É USADO NO INIT PARA A CONDIÇÃO DE LISTAR OPERAÇÕES NO LOOPING INFINITO
        if a == 0:
            return "break" #RETORNA A STRING BREAK PARA QUE SEJA USADO COMO CONDIÇÃO PARA PARAR A EXECUÇÃO DO CODIGO CASO O USUARIO DIGITE 0
        if a in [5, 6, 9, 10, 11, 12, 13]: # CONDIÇÃO PARA RECEBER APENAS UM INPUT
            x = float(input("Digite um numero ou r para resultado anterior: "))
            y = None #Y É NONE POIS PARA ESSAS OPERAÇÕES SE NECESSITA APENAS UM INPUT
            if x == "r":
                x = res

        if a in [14, 15]: # CONDIÇÃO PARA EXIBIR A CALCULADORA FINANCEIRA
            x, y, z = calculadora.prin_finan()

        if a in [1, 2, 3, 4, 7, 8]: #CONDIÇÃO PARA RECEBER 2 INPUTS
            x = input("Digite um numero ou r para resultado anterior: ")
            if x == "r":
                x = res
            else:
                x = float(x)

            y = input("Digite um numero ou r para resultado anterior: ")
            if y == "r":
                y = res
            else:
                y = float(y)

        # -------------Simples----------------#

        if a == 1:
            c = calculadora.simples(x, y)
            resultado = c.somar()

        if a == 2:
            c = calculadora.simples(x, y)
            resultado = c.subtrair()

        if a == 3:
            c = calculadora.simples(x, y)
            resultado = c.multiplicar()

        if a == 4:
            c = calculadora.simples(x, y)
            resultado = c.dividir()
        # -------------Cientifica----------------#
        if a == 5:
            c = calculadora.cientifica(x, y)
            resultado = c.elevado_quadrado()

        if a == 6:
            c = calculadora.cientifica(x, y)
            resultado = c.raiz_quadrada()

        if a == 7:
            c = calculadora.cientifica(x, y)
            resultado = c.elevar_a_x()

        if a == 8:
            c = calculadora.cientifica(x, y)
            resultado = c.raiz_x()

        if a == 9:
            c = calculadora.cientifica(x, y)
            resultado = c.log()

        if a == 10:
            c = calculadora.cientifica(x, y)
            resultado = c.fatorial()

        if a == 11:
            c = calculadora.cientifica(x, y)
            resultado = c.sen()

        if a == 12:
            c = calculadora.cientifica(x, y)
            resultado = c.cos()

        if a == 13:
            c = calculadora.cientifica(x, y)
            resultado = c.tg()

            # -------------Financeira---------------#
        if a == 14:
            c = calculadora.Financeira(x, y, z)
            resultado = c.Juros_Simples()

        if a == 15:
            c = calculadora.Financeira(x, y, z)
            resultado = c.Juros_Composto()

        c = None #destrutor
        return resultado


    class simples():  # SUBCLASSE DA CALCULADORA SIMPLES, REALIZA OPERAÇÕES SIMPLES
        def __init__(self, a, b):  # CONSTRUTOR RECEBE OS PARAMETROS
            self.a = a
            self.b = b

        def somar(self):
            return self.a + self.b

        def subtrair(self):
            return self.a - self.b

        def multiplicar(self):
            return self.a * self.b

        def dividir(self):
            while self.b == 0:
                print("Nao existe divisao por 0, tente novamente")
                self.a = float(input("Digite um numero: "))
                self.b = float(input("Digite um numero: "))
            return self.a / self.b

    class cientifica(): #SUBCLASSE CALCULADORA CIENTIFICA

        def __init__(self, a, b):  # CONSTRUTOR RECEBE OS PARAMETROS
            self.a = a
            self.b = b

        def elevado_quadrado(self):
            # return self.a*self.a
            c = calculadora.simples(self.a, self.a)  #
            return c.multiplicar()

        def raiz_quadrada(self):
            return sqrt(self.a)

        def elevar_a_x(self):
            return self.a**self.b

        def raiz_x(self):
            return self.a**(1/self.b)
            
        def log(self):
            return log10(self.a)

        def fatorial(self):
            return factorial(self.a)

        def sen(self):
            return (sin(self.a))  # Resultado em Radiano

        def cos(self):
            return (cos(self.a))  # Resultado em Radiano

        def tg(self):
            return (tan(self.a))  # Resultado em Radiano

    class Financeira(): #SUBCLASSE CALCULADORA FINANCEIRA
        def __init__(self, P, I, N): #CONSTRUTOR RECEBE PARAMETROS
            self.P = P  # Montante Inicial (R$)
            self.I = I  # Taxa de Juros (%)
            self.N = N  # Periodo (mês)

        def Juros_Simples(self):
            J_S = (self.P + (self.P * (self.I / 100) * self.N))
            return J_S

        def Juros_Composto(self):
            J_C = self.P * ((1 + (self.I / 100)) ** self.N)
            return J_C


calculadora()