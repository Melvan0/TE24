mer = False
liten = 80
stor = 120
extra = 15
feferoni = 10
pris = 0

print("Kött och video välkommen beställa! ")
while True:
    if mer == "ja":
        print("Du vill ha mer? varsågod beställa mer ")
    while True:
        storlek = input("vill du ha pizza stor eller pizza liten? ").lower()
        if storlek == "stor":
            print(f"Pizza stor absolut! \nDet blir {stor} kronor! ")
            pris = pris + 120
            break
        elif storlek == "liten":
            print(f"Pizza liten absolut! \nDet blir {liten} kronor!")
            pris = pris + 80
            break
        else:
            print("Jag förstår inte vad du säga till mig?! ")
    
    while True:
        extra = input("\nViljas extra något? Ost, feferoni, båda? ").lower()
        if extra == "ost":
            print("Ost extra absolut! \nDet blir extra 15 kronor ")
            pris = pris + 15
            break
        elif extra == "feferoni":
            print("Feferoni extra absolut! \nDet blir extra 10 kronor ")
            pris == pris + 10
            break
        elif extra == "båda":
            print("Ost och feferoni extra absolut!\n Det blir extra 25kr men du får 5 kr rabatt för du välja båda! ")
            pris == pris + 20
            break
        elif extra == "nej":
            break
        else:
            print("Du måste tala svenska vanlig jag fatta inte! ")
        break
    mer = input("Vill du bäställa mer pizza? ").lower
    if mer == "ja":
        print("UNDERBART! ")
    else:
        break  
print(f"Det blir {pris} kronor \n15 minuter en kvart välkommen hämta! ")
            




