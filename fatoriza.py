'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''
def factoriza(n):
    primfac = []
    d = 2
    res = [] 
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    for i in primfac: 
     if i not in res: 
            res.append(i) 
    x= sum (res)
    return x 