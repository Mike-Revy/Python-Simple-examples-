import random

# make a list of words
words = [ 
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon']

while True:
    start = input("press enter/return to start, or enter Q to quit")
    if start.lower() == 'q':
        break
    # pick a random word - choise requires nonempty list - otherwise indexerror
    secret_word = random.choice(words)
    print("secret word length {}".format(len(list(secret_word))))
    bad_guesses = []
    good_guesses = []
    
    while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
        # make secretword a list .. not sure why you need this but ...
        # draw spaces for the letters 
        # draw guessed letters and strikes 
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
        print('')
        print('Strikes: {}/7'.format(len(bad_guesses)))
        print('')
        
        # take a guess 
        guess = input("Guess a letter: ").lower()
        # since all words are lower case ...
        if len(guess) != 1:
            print("You can only guess one letter!")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You already guessed that letter! ")
            continue
        elif not guess.isalpha():
            print("you can only try letters !")
            continue
        

        if guess in secret_word:
            good_guesses.append(guess)
            print("guess in secret word with length {}".format(len(good_guesses)))
            if len(good_guesses) == len(list(secret_word)):
                print("You win! The word was {}".format(secret_word))
                break
        else: 
            bad_guesses.append(guess)
    else:
        print("you did not guess it! My secret word was {}".format(secret_word))
    # print out win/lose 
    
