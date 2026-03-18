#instruktioner : https://resource.itslearning.com/ViewFile.aspx?mode=FileOnly&Accessibility=False&allowedhtmlcodelevel=Restricted&ApiSessionId=6e76d0f2e9ad417c8d0b1837a32e622a&ContextRole=Learner&countrycode=SE&createcontentwithai=False&CustomerId=901426&educationsegment=1&Encoding=utf8&extrauserinformationpermissions=None&FirstName=Melvin&functionalityprivatefiles=True&functionalitywebfiles=True&isextensionmanager=False&itslearningenvironmentid=eu1&itslearningversion=2026.2.5.53&Language=sv-SE&LastName=Nilsson&LearningObjectId=468164007&LearningObjectInstanceId=625392950&Locale=sv-SE&LocationId=1408&myfilesfunctionality=True&OlsonTimeZoneId=Europe%2fStockholm&openedforpreview=False&OpenedFromCourse=True&Permissions=Read%2c+Participate&personid=401296&ReadOnly=False&Role=Learner&Use12HTimeFormat=False&UserId=153531872&UserName=emelnil%40utb.hoglandet.se&userrightsprivacy=None&WindowsTimeZoneId=W.+Europe+Standard+Time&Timestamp=2026-02-26T13%3a02%3a48&EditInBrowser=false&isPopUp=true&Signature=724d4ada070b9a20e9cd44cd446f1c35
#text to ASCII: https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=3D-ASCII&text=BlackJ%C3%A1ck
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
win = 0 #decides if someone has won, 0 means no one has won the current round, 1 means dealer wins, 2 means player wins
dealer_hand = 0
player_hand = 0
cards = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

cards[10:13] = [10, 10, 10]
cards[0] = 11

def ace():
    if cards[0] in hand and hand > 21:
        cards[0] = 1

