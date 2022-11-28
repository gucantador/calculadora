
class calculadora():


    def __init__(self): #CONSTRUTOR INICIA AS OPERAÇÕES 
        resultado = 0    
        print("BEM VINDOA CALCULADORA\n*******************************")
        self.listar_operacoes() #METODO QUE LISTA AS OPERAÇÕES, FORA DO WHILE PARA INICIALIZAR A PRIMEIRA VEZ
        while True: 
            try: #PARA O CODIGO NAO QUEBRAR POR ERRO DE INPUT DO USUARIO
                resultado = self.rodar(resultado)  #VARIAVEL RESULTADO INICIADA COM 0 A CIMA, MAS DEPOIS RECEBE DO LOOPING IFINITO
                if resultado == "break":
                    break
                print('%.2f' % resultado)
                
                if resultado == "listar":
                    self.listar_operacoes() #METODO PARA LISTAR OPERAÇÕES CASO DESEJADO PELO USUARIO

            except: #INFORMA O USUARIO QUE ELE REALIZOU UM INPUT ERRADO
                print("Houve algum erro de input, verifique as instruções")
                pass

    def prin_finan(): # 'PRINT' DEDICADO PARA CALCULADORA FINANCEIRA
        x = float(input("Montatnte Inicial (R$): "))
        y = float(input("Taxa de Juros (%): "))
        z = float(input("Periodo (mês): "))
        return(x,y,z)

    def listar_operacoes(self): #METODO QUE LISTA OPERAÇÕES
        print("1 - somar")
        print("2 - subtrair")
        print("3 - multiplicar")
        print("4 - dividir")
        print("5 - elevar ao quadrado")
        print("6 - raiz quadrada")
        print("7 - elevar a x")
        print("8 - raiz x")
        print("9 - log")
        print("10 - fatorial")
        print("11 - sen")
        print("12 - cos")
        print("13 - tg")
        print("14 - juros simples")
        print("15 - juros compostos")
        

    def rodar(self, res): #METODO QUE RODA O CODIGO, CONDIÇÕES DE OPÇÕES DO USUARIO
        
        a = int(input("Escolha sua operação, digite 0 para encerrar ou 45 para listar operações: "))

        if a == 45:
            return "listar"
        if a == 0:
            return "break"
        if a == 14 or a == 15:
            x,y,z = calculadora.prin_finan() 


        if a == 5:
            x = float(input("Digite um numero ou r para resultado anterior: "))
            y = None
            if x == "r":
                x = res


        else: 
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

        #----------------------------------------

        if a == 1:
            c = calculadora.simples(x, y)
            # print(c.somar())
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



        if a == 5:
            c = calculadora.cientifica(x, y)
            resultado = c.elevado_quadrado()


        if a == 14:
            c = calculadora.Financeira(x,y,z)
            resultado = c.Juros_Simples()

        if a == 15:
            c = calculadora.Financeira(x,y,z)
            resultado = c.Juros_Composto()

        return resultado

    class simples(): #SUBCLASSE DA CALCULADORA SIMPLES, REALIZA OPERAÇÕES SIMPLES
        def __init__(self, a, b): #CONSTRUTOR RECEBE OS PARAMETROS
            self.a = a
            self.b = b

        def somar(self):
            return self.a+self.b
        
        def subtrair(self):
            return self.a-self.b
        
        def multiplicar(self):
            return self.a*self.b

        def dividir(self):
            while self.b == 0:
                print("Nao existe divisao por 0, tente novamente")
                self.a = float(input("Digite um numero: "))
                self.b = float(input("Digite um numero: "))
            return self.a/self.b

    class cientifica():










        def __init__(self, a, b=0): #CONSTRUTOR RECEBE OS PARAMETROS
            self.a = a
            self.b = b

        def elevado_quadrado(self):
            # return self.a*self.a
            c = calculadora.simples(self.a, self.a)
            return c.multiplicar()

            











    class Financeira():
        def __init__(self, P, I, N):
            #self.M = M # Montante
            self.P = P # Montante Inicial (R$)
            self.I = I # Taxa de Juros (%)
            self.N = N # Periodo (mês)


        def Juros_Simples(self):
            J_S = (self.P + (self.P * (self.I/100) * self.N))
            return J_S

        def Juros_Composto(self):
            J_C = self.P * ((1 + (self.I/100))**self.N)
            return J_C

calculadora()     
