# .lower / .upper doesnt work
# if 

import random

play = "y"

while play == "y" or "yes": #makes it loop

    word_list = ["guy", "man", "penis", "mattias", "cocaine", "fence", "bone", "fist", "fish", "wrist", "arm", "leg", "jimmy", "adam", "bin", "laden", "balls", "soup", "hang", "rope", "fork", "fire", "melvin", "apple", "pen", "down", "syndrome", "blue", "green", "purple", "red", "orange", "door", "velociraptor", "stegosaur", "wonderful", "extraordinary", "end"]
    word = random.choice(word_list) #chooses a random word from the list above
    length = len(word) #checks the length of the word
    word_ch = set(word) #
    ch_length = len(word_ch) #check how many characters are in the word

    #guess_word = ("-\n" * length)
    guess_word = []
    guesses = 10
    right_guesses = 0
    word_letters = list(word)
    guessed_letters = []

    for index, letter in enumerate (word):
        guess_word.append("_")

    #print(word)
    #print(length)
    #print(ch_length)

    while right_guesses != ch_length and guesses != 0:
        print("\n" + ''.join(guess_word))
        if guessed_letters != []:
            print("\n" + ', '.join(guessed_letters))
        guess = input("\nGuess: ")
        if guess in guess_word:
            print("\nLetter has already been guessed! ")
        elif guess not in word_letters:
            guesses = guesses - 1
            if guess not in guessed_letters:
                guessed_letters.append(guess)
            print(f"\nIncorrect guess! You have {guesses} guesses left ")
        else:
            right_guesses = right_guesses + 1        
        for i, letter in enumerate (word):
            if guess == letter:
                guess_word[i] = guess
                  
    if right_guesses == length:
        print(f"\nWell done! The word was {word} ")
    else:
        print(f"\nToo bad! The word was {word} ")

    play.lower() == input("\nPlay again? y/n ")

print("\nThank you for playing! 😊\n")





    #Testkod nr 4
#while right_guesses != ch_length:
#    guess = input("Gissa goddamn it!: ").lower
#    if guess in word:
#        right_guesses = right_guesses + 1    
#        print(right_guesses)
#        for index, letter in enumerate(word):
#            print(guess)
#    else:
#        print("du suger")

    #Test-kod nr 3
#print("test", guess_word, "test")
#while guess_word != word:
    #guess = input("Gissa en bokstav: ").lower
    #for index, letter in enumerate(word):
        #if guess not in word:
            #guesses = guesses - 1
            #print(f"Fel! Du har {guesses} kvar! ")
        #else:             

    #Testkod nr 2
#while word != no_word:
    #print(no_word, "\n")
    #print(f"Du har {guesses} gissningar")
    #guess = input("Gissa en bokstav: ").lower()
    #for index, letter in enumerate(word):
        #if guess not in word: 
            #print(no_word)

    #Testkod nr 1
#while word != no_word:
    #print(no_word, "\n")
    #print(f"Du har {guesses} gissningar")
    #guess = input("Gissa en bokstav: ").lower()
    #for index, letter in enumerate(word):
        #if guess == letter:
            #hidden = (f"{guess}")
            #print(hidden)
        #elif guess not in word:
            #print("-")
            #guesses = guesses - 1
            #print(f"Du har {guesses} kvar")