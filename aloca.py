"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
    alocalist = prefs.items ()
    sorted_by_student = sorted(alocalist, key=lambda tup: tup[0])
    semprojeto = []
    projetos = []
    for aluno in alocalist:
        if aluno[1] in projetos:
            semprojeto.append (aluno[0])
        else:
            projetos.append (aluno [1])
    
    return semprojeto