import math

while True:
    arbete = input("Ange B för badrum H för hall och K för kök: ").upper()

    if not (arbete == "B" or arbete == "H" or arbete == "K"):
        print("Fel värde!! Gör om, gör rätt!!")
    else:
        try:
            kvm = float(input("Ange antal kvadratmeter: "))
            #k = kakel
            kplattor_pack = 32               #Antalet plattor per paket kakellattor
            kfix_säck = 5                    #Mängden kg kakelfix per säck
            kfog_säck = 3                    #Mängden kg kakelfox per säck
            
            kplattor = 0
            kfix = 0
            kfog = 0

            if (arbete == "B" and kvm > 0):              #Om arbete är definerat som B (Badrum)
                kplattor = 15 * kvm
                kfix = 0.7 * kvm
                kfog = 0.4 * kvm
                #print(kplattor, kfix, kfog) #print för att se om alla variablar fick rätt värde
            elif (arbete == "H" and kvm > 0):            #Om arbete är definerat som H (Hall)
                kplattor = 8 * kvm
                kfix = 0.3 * kvm
                kfog = 0.25 * kvm
                #print(kplattor, kfix, kfog) #print för att se om alla variablar fick rätt värde
            elif (arbete == "K" and kvm > 0):            #Om arbete är definerat som K (Kök)
                kplattor = 12 * kvm
                kfix = 0.2 * kvm
                kfog = 0.15 * kvm
                #print(kplattor, kfix, kfog) #print för att se om alla variablar fick rätt värde

            #res = resultat
            kplattor_res = kplattor / kplattor_pack
            kfix_res = kfix / kfix_säck
            kfog_res = kfog / kfog_säck

            #print(kplattor_res, kfix_res, kfog_res)

            kplattor_res = math.ceil(kplattor_res)
            kfix_res = math.ceil(kfix_res)
            kfog_res = math.ceil(kfog_res)
            if kplattor_res<=0:
                print("Error!")
            else:
                print("Det behövs ", kplattor_res, " paket kakelplattor, ", kfix_res, "säckar kakelfix och ", kfog_res, "säckar kakelfog")
        except ValueError:
            print("Aja baja din fula fisk, skriv ett positivt nummer din dummer!")

    
