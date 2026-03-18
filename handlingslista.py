import math

ny_lista = "ja"
while ny_lista == "ja":

    lista = []

    kör = "ja"

    nr = 1

    while kör == "ja":

        yn = True

        vara = input("Vad ska köpas? ")

        pris = float(input("\nVad är dess styckpris? "))

        antal = int(input("\nHur många ska köpas? "))
        print(" ")

        totalt_pris = antal * pris

        saker = (f"vara nr {nr}: {vara} ({pris}kr/st), antal: {antal}, totalt pris: {totalt_pris}")
        print(saker)

        lista.append(saker)
        
        kör.lower() == input("\nVill du lägga till ännu en vara? Ja eller Nej: ")
        if kör == "ja":
            print("\nDin lista består än så länge av detta: ")
            print(' '.join(lista))
            nr = nr + 1
        elif kör == "nej":
            print("Din lista är nu klar! ")
            print(' '.join(lista))

    while True:
        ny_lista.lower() == input("\nVill du göra en ny lista? Ja eller Nej: ")
        if ny_lista == "nej":
            print("\nHa en trevlig dag! ")
            break
        elif ny_lista != "ja" or "nej":
            print("Error! Ogiltig inmatning ")