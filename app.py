from flask import Flask, render_template, request

app = Flask(__name__)

OPERACOES = {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/",
}


def calcular(opcao, num1, num2):
    if opcao == "1":
        return num1 + num2
    if opcao == "2":
        return num1 - num2
    if opcao == "3":
        return num1 * num2
    if opcao == "4":
        if num2 == 0:
            raise ZeroDivisionError
        return num1 / num2


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None
    valores = {"num1": "", "num2": "", "opcao": "1"}

    if request.method == "POST":
        valores["num1"] = request.form.get("num1", "")
        valores["num2"] = request.form.get("num2", "")
        valores["opcao"] = request.form.get("opcao", "1")

        if valores["opcao"] not in OPERACOES:
            erro = "Opção inválida! Tente novamente."
        else:
            try:
                num1 = float(valores["num1"].replace(",", "."))
                num2 = float(valores["num2"].replace(",", "."))
                resultado = f"{calcular(valores['opcao'], num1, num2):g}"
            except ValueError:
                erro = "Entrada inválida! Digite apenas números."
            except ZeroDivisionError:
                erro = "Erro: não é possível dividir por zero!"

    return render_template(
        "index.html",
        resultado=resultado,
        erro=erro,
        valores=valores,
        operacoes=OPERACOES,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

