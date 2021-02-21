def apelidos(nomes):
    nomes.sort(key = lambda n : (len(n.split())-1,n))
    return nomes