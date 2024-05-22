from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import choice

words3 = []
MAXGUESSES = 10
def fetchWords(): ## Uses BeautifulSoup4 to download the list of 3-letter words
    print("Fetching list of words...")
    temp = []
    url = 'https://scrabble.collinsdictionary.com/word-lists/three-letter-words-in-scrabble/'
    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    for line in soup.getText().split('\n'):
        if len(line) == 3:
            temp.append(line.lower()) ## Add the 3-letter word to the list
    print("Done.")
    return temp ## Return the list
def play(): ## Play the game
    guesses = 0
    word = choice(words3) ## Get a random word from the list
    ## print(f"Hidden word is: {word}")
    while(guesses < MAXGUESSES):
        guess = str(input("Guess a word > "))
        if(len(guess) != 3): ## If word isn't 3 letters long
            print("Invalid Guess. Try Again.")
            continue
        if guess not in words3: ## If word isn't valid
            print("This word doesn't exist in this database. Try another.")
            continue
        if(guess == word): ## If the user guesses the word
            return [1, word]
        guesses += 1
        for i in range(0, len(word)): ## For every letter in the guessed word, we check its relation with the actual word
            if guess[i] == word[i]:
                print(f" -> {guess[i]}: In the correct spot")
            elif (guess[i] != word[i]) and (guess[i] in word):
                print(f" -> {guess[i]}: In the wrong spot")
            else:
                print(f" -> {guess[i]}: Not in the word")
    return [0, word]

words3 = fetchWords() ## Get the list of words.
result, word = play() ## Play the game. Result = 0 means the user lost, result = 1 means the user won.

## Print appropriate game result
if(result == 0):
    print(f"\nYou lost! The correct word was {word}\n")
else:
    print("You won!")
