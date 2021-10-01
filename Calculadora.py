print("---------------------------------------------------------")
print("--------------- C A L C U L A D O R A -------------------")
print("---------------------------------------------------------")

deseja_continuar = 0
rodada = 1
while (rodada > 0):

    num1 = int(input("Entre num1: "))
    num2 = int(input("Entre num2: "))
    acao = str(input("Escolha entre (a), (s), (m), (d) para exeturar sua acao: Somar(a), Subtrair(s), Multiplicar(m), Dividir(d) -> ").upper())
    
    print("O resultado é ",end="")
    if acao == "A":
        print(num1 + num2)
    elif acao == "S":
        print(num1 - num2)
    elif acao == "M":
        print(num1 * num2)
    else:
        print(num1 / num2)

    print("--------------------------------------------")

    deseja_continuar = input("Digite (1) para continuar ou (0) para sair:  ")
    rodada = int(deseja_continuar)






print("Obrigado por usar meu programa")



