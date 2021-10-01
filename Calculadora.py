
calculadora = print(input("Digite (S) para continuar:  ").upper())

while calculadora == "S":
    print("--------------------------------------------")
    break
else:
    print("Obrigado por participar do meu projeto.")

num1 = int(input("Entre num1: "))
num2 = int(input("Entre num2: "))
acao = str(input("Escolha entre (a), (s), (m), (d) para exeturar sua acao: Somar(a), Subtrair(s), Multiplicar(m), Dividir(d) -> "))

print("O resultado é ",end="")
if acao == "a":
    print(num1 + num2)
elif acao == "s":
    print(num1 - num2)
elif acao == "m":
    print(num1 * num2)
else:
    print(num1 / num2)

print("--------------------------------------------")
