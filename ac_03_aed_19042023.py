# elaborar um codigo em python que 
# calcule a media de 2 alunos baseado em 4 provas e dizer se cada um foi aprovado
# ou reprovado sabendo que a média é 7.0
# A atividade deve ser entregue individualmente, salvar o arquivo da seguinte maineira AC3_seunome.ipynb
#  Apos salvar faça o download do arquivo e anexe na atividade

def ac_03(aluno):
    import json
    nota_1 = float(input('Digite a nota 1: \n'))
    nota_2 = float(input('Digite a nota 2: \n'))
    nota_3 = float(input('Digite a nota 3: \n'))
    nota_4 = float(input('Digite a nota 4: \n'))
    media = (nota_1 + nota_2 + nota_3 + nota_4)/4
    # return media
    if ((nota_1 + nota_2 + nota_3 + nota_4)/4) < 7:
        status = False
        # return media
        notas_aluno = {
            "Nota 1" : {nota_1},
            "Nota 2" : {nota_2},
            "Nota 3" : {nota_3},
            "Nota 4" : {nota_4},
            "Media" : {media},
            "Aluno Aprovado" : {status}
        }
        resposta = json.dump(notas_aluno, 4)
        return resposta.json()
    else:
        status = True
        # return media
        notas_aluno = {
            "Nota 1" : {nota_1},
            "Nota 2" : {nota_2},
            "Nota 3" : {nota_3},
            "Nota 4" : {nota_4},
            "Media" : {media},
            "Aluno Aprovado" : {status}
        }
        resposta = json.dump(notas_aluno, 4)
        return resposta.json()
print(ac_03('Vinicios'))