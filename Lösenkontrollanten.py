print(r"""    
 ________  ________  ________   ________  ___       __   ________  ________  ________          ___      ___ ________  ___       ___  ________  ________  _________  ________  ________     
|\   __  \|\   __  \|\   ____\ |\   ____\|\  \     |\  \|\   __  \|\   __  \|\   ___ \        |\  \    /  /|\   __  \|\  \     |\  \|\   ___ \|\   __  \|\___   ___\\   __  \|\   __  \    
\ \  \|\  \ \  \|\  \ \  \___|_\ \  \___|\ \  \    \ \  \ \  \|\  \ \  \|\  \ \  \_|\ \       \ \  \  /  / | \  \|\  \ \  \    \ \  \ \  \_|\ \ \  \|\  \|___ \  \_\ \  \|\  \ \  \|\  \   
 \ \   ____\ \   __  \ \_____  \\ \_____  \ \  \  __\ \  \ \  \\\  \ \   _  _\ \  \ \\ \       \ \  \/  / / \ \   __  \ \  \    \ \  \ \  \ \\ \ \   __  \   \ \  \ \ \  \\\  \ \   _  _\  
  \ \  \___|\ \  \ \  \|____|\  \\|____|\  \ \  \|\__\_\  \ \  \\\  \ \  \\  \\ \  \_\\ \       \ \    / /   \ \  \ \  \ \  \____\ \  \ \  \_\\ \ \  \ \  \   \ \  \ \ \  \\\  \ \  \\  \| 
   \ \__\    \ \__\ \__\____\_\  \ ____\_\  \ \____________\ \_______\ \__\\ _\\ \_______\       \ \__/ /     \ \__\ \__\ \_______\ \__\ \_______\ \__\ \__\   \ \__\ \ \_______\ \__\\ _\ 
    \|__|     \|__|\|__|\_________\\_________\|____________|\|_______|\|__|\|__|\|_______|        \|__|/       \|__|\|__|\|_______|\|__|\|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|
                       \|_________\|_________|                                                                                                                                             

      """)

pword_list  = ["password", "PAssWOrd", "PWord1234567890", "Pass", "LabCoat1337", "WillThisWork?", "pawssord", "132", "12345678", "87654321", "One1Two2Three3", "pa ss wo rd"] #list of passwords



def validate_pword(pword_list): #validate_pword function that checks which passwords are valid
    valid_pwords = [] #list of valid passwords
    for pword in pword_list: #for each password in the list, do the following:
        #print(pword)
        #print(len(pword))
        if "password" not in pword and " " not in pword and "123" not in pword and len(pword) >= 8: #if "password", "123", a space are not in the password and its longer than 8 characters the password is valid
            valid_pwords.append(pword)
        else:
            print(f'{pword} is not a valid password! Password must not include "password", "123" or a space and must be at least 8 characters long!\n') #if the password is not valid then it sends a message per password
    print(', '.join(valid_pwords), "are valid passwords 👍 \n")

validate_pword(pword_list) #calls on the validate_pword function