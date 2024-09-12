from exercicio import Exercicio

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicio()
        self.num = 0
        self.num1 = 0
        self.num2 =0

    def mostrarMenu (self):
        print('\n----MENU ---\n\n'+
              'Escolha una das opções abaixo: '+
                '\n0. Sair'+
                '\n1. Somar'+
                '\n2. Subtrair'+
                '\n3. Dividir'+
                '\n4. Multiplicar'+
                '\n5. Potência'+
                '\n6. Raiz'+
                '\n7. Tabuada'+
                '\n8. exercicio01' +
                '\n9. exercicio02' +
                '\n10. exercicio03'+
                '\n11. exercicio04' +
                '\n12. exercicio05'+
                 '\n13. exercicio06'+
                 '\n14. exercicio07'+
                 '\n15. exercicio08')

    def coletar(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))

    def colet(self):
        self.num \
            = int(input("Informe o primeiro número: "))


    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()

            self.opcao = int(input('Escolha umas das opções acima:'))
            if self.opcao == 0:
                print('Obrigado!!!')
            if self.opcao == 1:
                self.coletar()
                print(f'A soma dos números é: {self.exer.somar(self.num1, self.num2)}')

            elif self.opcao == 2:
                self.coletar()
                print(f'Asubtração dos números digitados é: {self.exer.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()
                print(f'Asubtração dos números digitados é: {self.exer.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'A subtração dos números digitados é: {self.exer.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()
                print(f'A potência dos números digitados é: {self.exer.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'A tabuada do é: {self.exer.raiz(self.num1)}')
                print(f'A tabuada do  é: {self.exer.raiz(self.num2)}')


            elif (self.opcao == 7):
                self.coletar()
                print(f'A tabuada do é: {self.exer.tabuada(self.num1)}')
                print(f'A tabuada do  é: {self.exer.tabuada(self.num2)}')

            elif(self.opcao == 8):
                print(self.exer.exercicios01())

            elif (self.opcao == 9):
                print(self.exer.exercicios02())

            elif (self.opcao == 10):
                print(self.exer.exercicios03())

            elif (self.opcao == 11):
                print(self.exer.exercicios04())

            elif (self.opcao == 12):
                num1 = int(input("Informe o primeiro número: "))
                print(self.exer.exercicios05(num1))

            elif (self.opcao == 13):
                num1 = int(input("Informe o primeiro número: "))
                print(self.exer.exercicios06(num1))

            elif (self.opcao == 14):
                self.colet()
                print(self.exer.exercicios07(self.num))

            else:
                print("codigo escolhido não é válido!")








