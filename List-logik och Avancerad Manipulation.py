temperaturer = [12.5, 14.0, 10.3, 16.8, 15.5, 18.1, 19.4] #lista på temperaturer
print(temperaturer) #printar temperaturer

omvand_temp = temperaturer[::-1] #gör listan til omvänd ordning och sparar det i omvand_temp
print(omvand_temp) #printar temperaturer i omvänd ordning

temperaturer[:3] = ([13.0, 13.0, 13.0] ) #ändrar de tre första elementen till 13.0
print(temperaturer) #printar temperaturer

for temp in (temperaturer):
    if temp > 15.0: #om temperaturer är över 15 så går den till nästa steg
        print(temp) #printar temperaturer över 15 grader

del temperaturer.remove[-2:] #tar bort de två sista elementen i temperaturlistan
print(temperaturer) #printar lottnummer