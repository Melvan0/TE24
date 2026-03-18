print(r'''
                                                                                                                             
    // | |                         //   / /    _ _                      ((   ))   ||   / /                              
   //__| |    // ( )  ___         //__ / /    ___    __  ___ __  ___     \\ //    ||  / / ( )  ___   /  ___      ___    
  / ___  |   // / / ((   ) )     //__  /    //   ) )  / /     / /        /\\/     || / / / / //   ) / //___) ) //   ) ) 
 //    | |  // / /   \ \        //   \ \   //   / /  / /     / /        // \\     ||/ / / / //   / / //       //   / /  
//     | | // / / //   ) )     //     \ \ ((___/ /  / /     / /        ((___\\    |  / / / ((___/ / ((____   ((___/ /   
       
      ''')

def pizza():
    storlek_val = True
    extra_val = True

    print("Välkommen till Alis kött & video!\n")

    while storlek_val == True:
        storlek = input("Hura stor dina pizza ska vara? ")
        if storlek == "stor":
            print("Absolut! Stora pizza du ska ha!")
            storlek_val = False
        elif storlek == "liten":
            print("Absolut! Liten pizza du ska ha!")
            storlek_val = False
        else:
            print("Du måste säga en storlek! Vad betyda detta?!")
    
    while extra_val == True:
        extra = input("Ska du ha extra ost eller feferoni? ")
        if extra == "ost":
            print("Absolut! Extra ost du ska ha!")
            extra_val = False
        elif extra == "feferoni":
            print("Absolut! Extra feferoni du ska ha!")
            extra_val = False
        elif extra == "nej" or "inget":
            print("Absolut! Extra ingenting du ska ha!")
            extra_val = False
        elif extra == "ja" or "allt" or "båda":
            print("Absolut! Extra allt du ska ha!")
            extra_val = False
        else:
            print("Du måste säga vad du vill ha! Vad betyda detta?!")

pizza()