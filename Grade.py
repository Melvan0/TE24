while True:
    try:
        score=int(input("What was your score?\n"))      #Asks for score
    
        if  score <= 100 and score >= 0:                # If score is below 0 or above 100 it will move to line 14
            if score >= 90:
                print("MVG")
            elif 70 <= score < 90:
                print("VG")
            elif 50 <= score < 70:
                print("G")
            else:
                print("U")
        else:
            print("ERROR - OUTSIDE RANGE")              # ERROR if score is below 0 or over 100
    
    except ValueError:
        print("ERROR - WRONG FORMAT")                   # ERROR if score is not an integer