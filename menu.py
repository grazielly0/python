from exercicio import Exercicio

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicio()
        self.num = 0
        self.num1 = 0
        self.num2 =0
        self.num3 = 0
        self.num4 = 0

    def mostrarMenu (self):
        print('\n----MENU ---\n\n'+
              'Escolha una das opções abaixo: '+
              '\n0.  Sair'+
              '\n1.  Somar'+
              '\n2.  Subtrair'+
              '\n3.  Dividir'+
              '\n4.  Multiplicar'+
              '\n5.  Potência'+
              '\n6.  Raiz'+
              '\n7.  Tabuada'+
              '\n8.  exercicio01' +
              '\n9.  exercicio02' +
              '\n10. exercicio03'+
              '\n11. exercicio04' +
              '\n12. exercicio05'+
              '\n13. exercicio06'+
              '\n14. exercicio07'+
              '\n15. exercicio08' +
              '\n16. exercicio09' +
              '\n17. exercicio10'+
              '\n18. exercicio11'+
              '\n19. exercicio12' +
              '\n20. exercicio13' +
              '\n21. exercicio14' +
              '\n22. exercicio15' +
              '\n23. exercicio16' +
              '\n24. exercicio17' +
              '\n25. exercicio18' +
              '\n26. exercicio19' +
              '\n27. exercicio20' +
              '\n28. exercicio21' +
              '\n29. exercicio22' +
              '\n30. exercicio23' +
              '\n31. exercicio24' +
              '\n32. exercicio25' +
              '\n33. exercicio26' +
              '\n34. exercicio27' +
              '\n35. exercicio28' +
              '\n36. exercicio29' +
              '\n37. exercicio30' +
              '\n38. exercicio31' +
              '\n39. exercicio32' +
              '\n40. exercicio33' +
              '\n41. exercicio34' +
              '\n42. exercicio35' +
              '\n43. exercicio36' +
              '\n44. exercicio37' +
              '\n45. exercicio38' +
              '\n46. exercicio39' +
              '\n47. exercicio40' )






    def coletar(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))


    def colet(self):
        self.num = int(input("Informe o primeiro número: "))

    def coletarr(self):
        self.num1 = int(input("Informe sua idade: "))
        self.num2 = int(input("Informe o dia : "))
        self.num3 = int(input("Informe o mês: "))


    def colect(self):
        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número : "))



    def cole(self):
        self.num1 = int(input("Informe votos brancos: "))
        self.num2 = int(input("Informe votos nulos: "))
        self.num3 = int(input("Informe  votos validos: "))
        self.num4 = int(input("Informe  eleitores: "))


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

            elif (self.opcao == 15):
                self.colet()
                print(self.exer.exercicios08(self.num))

            elif (self.opcao == 16):
                self.colet()
                print(self.exer.exercicios09(self.num))

            elif (self.opcao == 17):
                print(self.exer.exercicios10())

            elif (self.opcao == 18):
                self.colet()
                print(self.exer.exercicios11(self.num))

            elif (self.opcao == 19):
                self.colet()
                print(self.exer.exercicios12(self.num))

            elif (self.opcao == 20):
                print(self.exer.exercicios13())


            elif (self.opcao == 21):
                self.colet()
                print(self.exer.exercicios14(self.num))

            elif (self.opcao == 22):
                self.colet()
                print(self.exer.exercicios15(self.num))


            elif (self.opcao == 23):
                self.colet()
                print(self.exer.exercicios16())


            elif (self.opcao == 24):
                self.colet()
                print(self.exer.exercicios17(self.num))



            elif (self.opcao == 25):
                self.colet()
                print(self.exer.exercicios18(self.num))



            elif (self.opcao == 26):
                self.colet()
                print(self.exer.exercicios19(self.num))


            elif (self.opcao == 27):
                self.colet()
                print(self.exer.exercicios20(self.num))


            elif (self.opcao == 28):
                self.colet()
                print(self.exer.exercicios22(self.num))


            elif (self.opcao == 29):
                self.coletar()
                print(f'A área do triangulo é: {self.exer.exercicios23(self.num1,self.num2)}')

            elif (self.opcao == 30):
                self.coletarr()
                print(self.exer.exercicios24(self.num1, self.num2, self.num3))


            elif (self.opcao == 31):
                self.colect()
                print(self.exer.exercicios25(self.num1, self.num2, self.num3))



            elif (self.opcao == 32):
                self.coletar()
                print(f'Seu novo salário é: {self.exer.exercicios26(self.num1, self.num2)}')


            elif (self.opcao == 33):
                self.colet()
                print(self.exer.exercicios27(self.num))


            elif (self.opcao == 34):
                self.coletar()
                print(self.exer.exercicios28(self.num1, self.num2, self.num3))




            elif (self.opcao == 35):
                self.colet()
                print(self.exer.exercicios29(self.num))


            elif (self.opcao == 36):
                self.colet()
                print(self.exer.exercicios30(self.num))


            elif (self.opcao == 37):
                self.coletar()
                print(f'Seu novo salário é: {self.exer.exercicios31(self.num1, self.num2)}')

            elif (self.opcao == 38):
                self.colet()
                print(self.exer.exercicios32)


            elif (self.opcao == 39):
                self.colet()
                print(self.exer.exercicios33(self.num))

            else:
                print("codigo escolhido não é válido!")








