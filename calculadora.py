class calculadora():


    def __init__(self):
        while True: 
            # self.rodar()
            
            resultado = self.rodar()
            if resultado == 0:
                break
            print(resultado)
            
            
        

    def rodar():
        
        a = int(input("Escolha sua operação: "))

        if a == 0:
            return 0

        x = float(input("Digite um numero: "))
        y = float(input("Digite um numero: "))


        
            

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

        return resultado

    class simples():
        def __init__(self, a, b):
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
                self.b =float(input("Digite um numero: "))
            return self.a/self.b

    class cientifica():
        def elevado_quadrado(a):
            pass



calculadora()     
    

# c = calculadora.simples(2,4)


# print(c.somar())