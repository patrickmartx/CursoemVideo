# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
import datetime
def validarEmprestimo(valorCasa, salarioComprador, parcela):
    limiteSalario = salarioComprador * (30/100)
    valorParcela = valorCasa / parcela
    if limiteSalario > valorParcela:
        return print(f"EMPRESTIMO APROVADO!\nO valor da parcela será de R${valorParcela:.2f} por {parcela} meses!")
    else:
        return print(f"EMPRESTIMO NEGADO!\n30% de seu salário (R${limiteSalario:.2f}) excede o valor da parcela (R${valorParcela:.2f}).")


horaAtual = datetime.datetime.today().hour
if (horaAtual >= 0) and (horaAtual < 6):
    print("** Boa madrugada! Somos da central de atendimento para emprástimos. **")
elif (horaAtual >= 6) and (horaAtual < 12):
    print("** Bom dia! Somos da central de atendimento para emprástimos. **")
elif (horaAtual >= 12) and (horaAtual < 18):
    print("** Boa tarde! Somos da central de atendimento para emprástimos. **")
elif (horaAtual >= 18) and (horaAtual < 24):
    print("** Boa noite! Somos da central de atendimento para emprástimos. **")

print("Para que seu emprestimo seja aprovado, precisaremos de algumas informações:")
valorCasa = float(input("Qual é o valor da casa?\n> "))
salarioComprador = float(input("Qual o seu salário?\n> "))
# parcela = str(input("Vai parcelar?(Responda com S ou N)\n> ")).strip().upper()
# parcela = parcelas(parcela)
ano = int(input("Em quantos anos será pago a casa?\n> "))
parcela = ano * 12
validacao = validarEmprestimo(valorCasa, salarioComprador, parcela)
