import math

#Antalet plattor/kg per paket/säck
kplattor_pack = 32               #Antalet plattor per paket kakellattor
kfix_säck = 5                    #Mängden kg kakelfix per säck
kfog_säck = 3                    #Mängden kg kakelfox per säck

#Antal plattor/kg per badrum
kplattor_B = 0
kfix_B = 0
kfog_B = 0

#Antal plattor/kg per hall
kplattor_H = 0
kfix_H = 0
kfog_H = 0

#Antal plattor/kg per kök
kplattor_K = 0
kfix_K = 0
kfog_K = 0
            
while True:
    work_B = input("\nSka du jobba på badrum? Ja/Nej ").lower()
    if not (work_B == "ja" or work_B =="nej"):
        print("Du måste skriva ja eller nej! Gör om gör rätt")
    elif work_B == "ja":
        try:
            sqm_B = float(input("Hur många kvadratmeter? "))
            kplattor_B = 15 * sqm_B
            kfix_B = 0.7 * sqm_B
            kfog_B = 0.4 * sqm_B
            print(kplattor_B, kfix_B, kfog_B)
        except ValueError:
            print("Aja baja din fula fisk, skriv ett positivt nummer din dummer!")

    work_H = input("\nSka du jobba på hall? Ja/Nej ").lower()
    if (work_H == "ja"):
        try:    
            sqm_H = float(input("Hur många kvadratmeter? "))
            kplattor_H = 15 * sqm_H
            kfix_H = 0.7 * sqm_H
            kfog_H = 0.4 * sqm_H
            print(kplattor_H, kfix_H, kfog_H)
        except ValueError:
            print("Aja baja din fula fisk, skriv ett positivt nummer din dummer!")
    else:
        print("Du måste skriva ja eller nej!" )

    work_K = input("\nSka du jobba på kök? Ja/Nej ").lower()
    if (work_K == "ja"):
        try:
            sqm_K = float(input("Hur många kvadratmeter? "))
            kplattor_K = 15 * sqm_K
            kfix_K = 0.7 * sqm_K
            kfog_K = 0.4 * sqm_K
            print(kplattor_K, kfix_K, kfog_K)
        except ValueError:
            print("Aja baja din fula fisk, skriv ett positivt nummer din dummer!")
    else:
        print("Du måste skriva ja eller nej!" )

    kplattor_res = kplattor_B + kplattor_H + kplattor_K
    kfix_res = kfix_B + kfix_H + kfix_K
    kfog_res = kfog_B + kfog_H + kfog_K
    print("\nTotalt behövs", kplattor_res, "kakelplattor,", kfix_res, "kg kakelfix och", kfog_res, "kg kakelfog")

    kplattor_res_pack = kplattor_res  / kplattor_pack
    kfix_res_pack = kfix_res / kfix_säck
    kfog_res_pack = kfog_res / kfog_säck

    kplattor_res_pack = math.ceil(kplattor_res_pack)
    kfix_res_pack = math.ceil(kfix_res_pack)
    kfog_res_pack = math.ceil(kfog_res_pack)
    print("\nTotalt behövs", kplattor_res_pack, "st paket kakelplattor,", kfix_res_pack, "st säckar kakelfix och", kfog_res_pack, "st säckar")

    