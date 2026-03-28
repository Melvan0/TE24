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
    "Two":2,
    "Three":3,
    "Four":4,
    "Five":5,
    "Six":6,
    "Seven":7,
    "Eight":8,
    "Nine":9,
    "Ten":10,
    #face cards - always worth 10
    "Knight":10,
    "Queen":10,
    "King":10,
    #ace - worth 11 if the hand is worth less than 21 and worth 1 if the hand is worth more than 21
    "Ace":[11, 1]
}

#list of suits
suit = ["Spades", "Hearts", "Diamond", "Clubs"]

#cards that have already been used
used_cards = []

#players hand and value
phand = []
phand_value = 0
#dealer hand and value
dhand = []
dhand_value = 0

#function for dealing into a hand
def deal(hand):
    while True:
        temp_value = random.choice(list(value.keys())) #draws a random value
        temp_suit = random.choice(suit) #draws a random suit
        if used_cards.count([temp_value, temp_suit]) < 4: #if the value and suit has been used less than 4 times it can be used, otherwise it draws another value and suit
            temp_card = [temp_value, temp_suit] #the value and suit are put together into a card
            used_cards.append(temp_card) #adds the card into a list of used cards
            break
    hand.append(temp_card)
    #hand.append(' '.join(temp_card)) #adds the card to the hand which is being dealt to

#function for calculating the value of a hand
def hand_value(hand):
    hand_value = 0
    for card in hand: #for every card in the hand, the program does the following
        print(card)
        #print(card[0])
        if card[0] != 'ace': #index 0 is always the value of the card and therefore can be used to identify aces
            #print(value[card[0]])
            hand_value += value[card[0]]
    #an ace needs to be processed differently    
        if card[0] == 'ace':
            if 21 > hand_value + 11:
                hand_value += 1
            elif 21 <= hand_value + 11:
                hand_value += 11

    print(hand_value)
        
#hand_value(phand)
#hand_value(dhand)

#print(used_cards)

#for card in phand:
    #print(card)
    #if card[0] in value:
        #print(value[card[0]])

#print(phand)
#hand_value(phand)
#print(phand)

#print("test")
#os.system('cls')
#print("är allt borta?")

