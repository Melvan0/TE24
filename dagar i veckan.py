dagar_i_veckan = ["måndag", "tisdag", "onsdag", "torsdag", "fredag"] #Skapar listan dagar_i_veckan

dagar_i_veckan.append("lördag") #Lägg till söndag
dagar_i_veckan.append("söndag") #Lägg till söndag

print(f"{dagar_i_veckan[-1]}") #Printar sista elementet i listan (-1 söndag)

dagar_i_veckan.remove("lördag")

dagar_i_veckan[1] = "Tisdag" #Ändrar andra elementet "tisdag" till "Tisdag" (stor bokstav)
print(dagar_i_veckan) #Printar listan dagar_i_veckan