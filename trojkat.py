def trojkat(rozmiar):
    gwiazdka = "*"
    i = 1
    while i <= rozmiar:
        print(gwiazdka * i)
        i += 1


trojkat(2)
trojkat(3)
trojkat(4)


def trojkatOdwrotny(rozmiaro):
    for i in range(rozmiaro,0,-1):
        print('*' * i)


trojkatOdwrotny(3)
trojkatOdwrotny(4)
trojkatOdwrotny(5)


def trojkatPiramida(h):
    s=h-1
    spacje = range(h,0,-1)
    x = enumerate(spacje)
    x = list(x)
    x.reverse()
    print(x)


h=5
trojkatPiramida(h)

