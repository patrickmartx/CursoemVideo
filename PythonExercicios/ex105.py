# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas | A maior nota | A menor nota | A média da turma | A situação (opcional)
# Adcione também as docstrings da função
def notas(* vals, sit=False):
    """
    Uma função que mostra quantas notas foram lidas, qual foi a maior, a menor, a média e situação do aluno, no caso de desejar ver.
    :param vals: Recebe uma ou mais notas dos alunos
    :param sit: Valor opcional, indicando se deve ou não mostrar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(vals)
    r['Maior'] = max(vals)
    r['Menor'] = min(vals)
    r['Média'] = (sum(vals) / len(vals))
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


# Programa principal
resp = notas(3, 4, 9.5, 9.5, 8.5, sit=True)
print(resp)
