try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados.")
except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__}")
else:
    print(f"O resultado é {r}")
finally:
    print("Volte sempre! Muito obrigado!")