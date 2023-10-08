def faktorial(bilangan):
    faktor = []
    for pembagi in range(1,bilangan+1):
        if bilangan % pembagi == 0:
            faktor.append(pembagi)
    return faktor

bilangan = int(input("Silahkan masukkan bilangan: "))
faktor = faktorial(bilangan)
print("Faktor dari",str(bilangan),"adalah: ",faktor)