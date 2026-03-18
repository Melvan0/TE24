current_year = 2026 #current year
birthyears = [4, 100, 400, 1998, 2000, 2004, 2010, 2024] #list of birth years, 4, 100 and 400 are just to demonstrate that it works as intended

print(birthyears) #prints birthyears so you know what years the program is working with

def analyze_birthyears(birthyears): #function for analyzing birthyears
    leap_born = [] #list for people born on leap years
    leap_born_count = 0 #count of how many are born on leap year
    adult = [] #list for people that are adults
    adult_count = 0 #count of how many are adults
    for year in birthyears: #for every birthyear the program does the following
        #print(year) 
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: #if the birthyears can be divided evenly with 4 and not 100 unless also with 400 the program does the following
            leap_born.append(year) #adds the birthyear to a list of leap years
            leap_born_count = leap_born_count + 1 #counts how many are born on leap years
        if current_year - year >= 18: #if the birthyears say that the people are adult, the program does the following
            adult.append(year) #adds the birthyear to an adult list
            adult_count = adult_count + 1 #counts how many are adults
    #print(leap_born)
    #print(adult)
    print(f"\nThere are {leap_born_count} people born on a leap year and {adult_count} people are adults") #prints how many are born on leap years and how many are adults
    
 
analyze_birthyears(birthyears) #calls for the function to analyze the birth years