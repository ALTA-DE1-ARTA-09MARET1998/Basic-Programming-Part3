import pandas as pd

def faktorial(bilangan):
    faktor = []
    for pembagi in range(1,bilangan+1):
        if bilangan % pembagi == 0:
            faktor.append(pembagi)
    return faktor

bilangan = int(input("Silahkan masukkan bilangan: "))
faktor = faktorial(bilangan)
f = pd.Series(faktor)
faktor.sort(reverse=True)

print("Faktor dari",bilangan,"adalah: ",faktor)