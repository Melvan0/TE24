#instruktioner : https://resource.itslearning.com/ViewFile.aspx?mode=FileOnly&Accessibility=False&allowedhtmlcodelevel=Restricted&ApiSessionId=6e76d0f2e9ad417c8d0b1837a32e622a&ContextRole=Learner&countrycode=SE&createcontentwithai=False&CustomerId=901426&educationsegment=1&Encoding=utf8&extrauserinformationpermissions=None&FirstName=Melvin&functionalityprivatefiles=True&functionalitywebfiles=True&isextensionmanager=False&itslearningenvironmentid=eu1&itslearningversion=2026.2.5.53&Language=sv-SE&LastName=Nilsson&LearningObjectId=468164007&LearningObjectInstanceId=625392950&Locale=sv-SE&LocationId=1408&myfilesfunctionality=True&OlsonTimeZoneId=Europe%2fStockholm&openedforpreview=False&OpenedFromCourse=True&Permissions=Read%2c+Participate&personid=401296&ReadOnly=False&Role=Learner&Use12HTimeFormat=False&UserId=153531872&UserName=emelnil%40utb.hoglandet.se&userrightsprivacy=None&WindowsTimeZoneId=W.+Europe+Standard+Time&Timestamp=2026-02-26T13%3a02%3a48&EditInBrowser=false&isPopUp=true&Signature=724d4ada070b9a20e9cd44cd446f1c35
#text to ASCII: https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=3D-ASCII&text=BlackJack
#image to Ascii: https://www.asciiart.eu/image-to-ascii

print(r"""

     🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎
         ________  ___       ________  ________  ___  __          ___  ________  ________  ___  __       
        |\   __  \|\  \     |\   __  \|\   ____\|\  \|\  \       |\  \|\   __  \|\   ____\|\  \|\  \     
        \ \  \|\ /\ \  \    \ \  \|\  \ \  \___|\ \  \/  /|_     \ \  \ \  \|\  \ \  \___|\ \  \/  /|_   
         \ \   __  \ \  \    \ \   __  \ \  \    \ \   ___  \  __ \ \  \ \   __  \ \  \    \ \   ___  \  
          \ \  \|\  \ \  \____\ \  \ \  \ \  \____\ \  \\ \  \|\  \\_\  \ \  \ \  \ \  \____\ \  \\ \  \ 
           \ \_______\ \_______\ \__\ \__\ \_______\ \__\\ \__\ \________\ \__\ \__\ \_______\ \__\\ \__\
            \|_______|\|_______|\|__|\|__|\|_______|\|__| \|__|\|________|\|__|\|__|\|_______|\|__| \|__|

     🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃍 🃎
                """)
#print("♥️♣️")

import random
import os

#dictionary for the available values one can get
value = {
    #number cards - worth the number on the card
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    #face cards - always worth 10
    "knight":10,
    "queen":10,
    "king":10,
    #ace - worth 11 if the hand is worth less than 21 and worth 1 if the hand is worth more than 21
    "ace":[11, 1]
}

#list of suits
suit = ["spades", "hearts", "diamond", "clubs"]

#players hand and value
phand = ["ace", "10",]
phand_value = 0
#dealer hand and value
dhand = []
dhand_value = 0

#function for calculating the value of a hand
def hand_value(hand):
    hand_value = 0
    for card in hand: #for every card in the hand, the program does the following
        if card != "ace":
            print(value[card])
            hand_value += value[card]
    #an ace needs to be processed differently
    for card in hand:
        if card == "ace":
            if 21 > hand_value + 11:
                hand_value += 1
            elif 21 <= hand_value + 11:
                hand_value += 11

    print(hand_value)
        
hand_value(phand)
hand_value(dhand)


#print("test")
#os.system('cls')
#print("är allt borta?")

