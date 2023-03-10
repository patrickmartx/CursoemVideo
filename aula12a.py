#Condições Aninhadas

nome = str(input("Qual o seu nome?\n")).strip().title()
if nome == 'Patrick':
    print("Que nome bonito!")
elif nome == "Ana" or nome == "Beatriz" or nome == "Ana Beatriz":
    print("Você é a mulher mais bonita do mundo!")
elif nome == "Enzo" or nome == "Lorenzo":
    print("KKKKKKKKKK você nasceu ontem")
else:
    print("Seu nome é bem normal.")
print(f"Tenha um bom dia, {nome}!")
