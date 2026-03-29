#instruktioner : https://resource.itslearning.com/ViewFile.aspx?mode=FileOnly&Accessibility=False&allowedhtmlcodelevel=Restricted&ApiSessionId=6e76d0f2e9ad417c8d0b1837a32e622a&ContextRole=Learner&countrycode=SE&createcontentwithai=False&CustomerId=901426&educationsegment=1&Encoding=utf8&extrauserinformationpermissions=None&FirstName=Melvin&functionalityprivatefiles=True&functionalitywebfiles=True&isextensionmanager=False&itslearningenvironmentid=eu1&itslearningversion=2026.2.5.53&Language=sv-SE&LastName=Nilsson&LearningObjectId=468164007&LearningObjectInstanceId=625392950&Locale=sv-SE&LocationId=1408&myfilesfunctionality=True&OlsonTimeZoneId=Europe%2fStockholm&openedforpreview=False&OpenedFromCourse=True&Permissions=Read%2c+Participate&personid=401296&ReadOnly=False&Role=Learner&Use12HTimeFormat=False&UserId=153531872&UserName=emelnil%40utb.hoglandet.se&userrightsprivacy=None&WindowsTimeZoneId=W.+Europe+Standard+Time&Timestamp=2026-02-26T13%3a02%3a48&EditInBrowser=false&isPopUp=true&Signature=724d4ada070b9a20e9cd44cd446f1c35
#text to ASCII: https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=3D-ASCII&text=BlackJack
#image to Ascii: https://www.asciiart.eu/image-to-ascii

import random
import os
import time

def blackjack():
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
#blackjack()
#print("♥️♣️")

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
#phand_value = 0
#dealer hand and value
dhand = []
hidden_card = []
#dhand_value = 0

#function for dealing into a hand
def deal(hand):
    while True:
        temp_value = random.choice(list(value.keys())) #draws a random value
        temp_suit = random.choice(suit) #draws a random suit
        if used_cards.count([temp_value, temp_suit]) < 4: #if the value and suit has been used less than 4 times it can be used, otherwise it draws another value and suit
            temp_card = [temp_value, temp_suit] #the value and suit are put together into a card
            used_cards.append(temp_card) #adds the card into a list of used cards
            break #stops the loop
    #hand.append(temp_card)
    hand.append(' '.join(temp_card)) #adds the card to the hand which is being dealt to

#function for calculating the value of a hand
def hand_value(hand):
    hand_value = 0
    for card in hand: #for every card in the hand:
        split_card = card.split(' ')[0] #splits the card at the space and saves the first part which is the value of the card into its own variable
        if split_card != 'Ace': #if the value of the card is not an ace:
            hand_value += value[split_card] #adds the value of the card to the hand value
        elif split_card == 'Ace': #if the value of the card is an ace:
            hand_value += value[split_card][0] #adds the value of the card to the hand value
    hand_len = len(hand) #checks how many elements are in the hand
    #print((', '.join(hand[:hand_len])), f"\nValue of hand: {hand_value}") #prints all the elements in the hand, used for testing
    if hand_value > 21: #if the value of the hand is more than 21:
        for card in hand: #for every card in the hand:
            split_card = card.split(' ')[0] #splits the card at the space and saves only the first part which is the value of the card
            if split_card == 'Ace': #if the value is an ace:
                hand_value -= (value['Ace'][0] - value ['Ace'][1]) #the value of the ace is changed from 11 to 1 
                if hand_value <= 21: #if the value of the hand is 21 or less:
                    break #breaks the loop
    hand_len = len(hand) #checks how many elements are in the hand
    #if hand == phand: #if the function is called with the players hand:
        #print((', '.join(hand[:hand_len])), f"\nValue of hand: {hand_value}") #prints all the cards in the hand
    if hand == dhand and hand_len > 1: #if the function is called with the dealers hand:
        hidden_card.append(hand[1]) #adds the dealers first card to the hidden_card list to remember it 
        if hand[1].split(' ')[0] == 'Ace': #if the second card in the hand is an ace:
            hand_value -= value[hand[1].split(' ')[0]][0] #remove the value of the ace from the value of the hand
        else:
            hand_value -= value[hand[1].split(' ')[0]] #removes the hidden cards value from the value of the hand
        #print(hidden_card) #prints the hidden card, used only for testing
        hand[1] = "Hidden" #changes the second card into a hidden one
    print((', '.join(hand[:hand_len])), f"\nValue of hand: {hand_value}") #prints all the elements of the hand

blackjack()
start = input('Welcome to Blakcjack! Type "start" to start the game, type "stop" to stop the game: ')
while True:
    if start == "start":
        os.system('cls') #clears the terminal
        #game on!
        print(r"""
         ________  ________  _____ ______   _______           ________  ________   ___       
        |\   ____\|\   __  \|\   _ \  _   \|\  ___ \         |\   __  \|\   ___  \|\  \      
        \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|        \ \  \|\  \ \  \\ \  \ \  \     
         \ \  \ ___\ \   __  \ \  \\|__| \  \ \  \_|/__       \ \  \\\  \ \  \\ \  \ \  \    
          \ \  \|\  \ \  \ \  \ \  \    \ \  \ \  \_|\ \       \ \  \\\  \ \  \\ \  \ \__\   
           \ \_______\ \__\ \__\ \__\    \ \__\ \_______\       \ \_______\ \__\\ \__\|__|   
            \|_______|\|__|\|__|\|__|     \|__|\|_______|        \|_______|\|__| \|__|   ___ 
                                                                                        |\__\
                                                                                        \|__|  """)
        break                                                                                      
    elif start == "stop":
        print(r"""
        ________  ___  ___  ___  ___          ________      ___    ___ _______   ___       
        |\   __  \|\  \|\  \|\  \|\  \        |\   __  \    |\  \  /  /|\  ___ \ |\  \      
        \ \  \|\ /\ \  \\\  \ \  \\\  \       \ \  \|\ /_   \ \  \/  / | \   __/|\ \  \     
         \ \   __  \ \  \\\  \ \   __  \       \ \   __  \   \ \    / / \ \  \_|/_\ \  \    
          \ \  \|\  \ \  \\\  \ \  \ \  \       \ \  \|\  \   \/  /  /   \ \  \_|\ \ \__\   
           \ \_______\ \_______\ \__\ \__\       \ \_______\__/  / /      \ \_______\|__|   
            \|_______|\|_______|\|__|\|__|        \|_______|\___/ /        \|_______|   ___ 
                                                           \|___|/                     |\__\
                                                                                       \|__|
                                                                                    
          """)
        exit
        break
    else:
        print("ERROR: input is invalid!")
        start = input('Type "start" to start the game, type "stop" to stop the game: ')
time.sleep(5)
os.system('cls')
blackjack()
#deals the first cards
deal(dhand)
deal(phand)
hand_value(phand)
time.sleep(3)
print("""
      



""")
hand_value(dhand)
time.sleep(5)
os.system('cls')
deal(dhand)
deal(phand)
hand_value(phand)
time.sleep(3)
print("""
      



""")
hand_value(dhand)



#print("test")
#os.system('cls')
#print("är allt borta?")

