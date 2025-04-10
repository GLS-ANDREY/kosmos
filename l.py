def skaska(name,cifra):
    print("Рыбалка")
    print(str(name) + "с дедушкой собрались на рыбалку")
    print("Погода стояла жаркая, но рыба клевала")
    print("Они поймали " + str(cifra) + " карасей и веселые вернулись домой")

skaska("Петя ",5)
for cifra_for in [5,10,3]:
    skaska("Саня ", cifra_for)