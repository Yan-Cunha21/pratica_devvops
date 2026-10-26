
while True:
    print("\n===== CALCULADORA =====")
    print("1 - Adicao (+)")
    print("2 - Subtracao (-)")
    print("3 - Multiplicacao (*)")
    print("4 - Divisao (/)")
    print("0 - Sair")

    opcao = input("Escolha uma operacao: ")

    if opcao == "0":
        print("Calculadora encerrada. Ate mais!")
        break

    if opcao not in ("1", "2", "3", "4"):
        print("Opcao invalida! Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))

        if opcao == "1":
            resultado = num1 + num2
        elif opcao == "2":
            resultado = num1 - num2
        elif opcao == "3":
            resultado = num1 * num2
        elif opcao == "4":
            if num2 == 0:
                print("Erro: não é possível dividir por zero!")
                continue
            resultado = num1 / num2

        print(f"Resultado: {resultado:g}")

    except ValueError:
        print("Entrada inválida! Digite apenas números.")
