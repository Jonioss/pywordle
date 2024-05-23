from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import choice

url3 = 'https://scrabble.collinsdictionary.com/word-lists/three-letter-words-in-scrabble/'
url4 = 'https://scrabble.collinsdictionary.com/word-lists/four-letter-words-in-scrabble/'
url5 = 'https://scrabble.collinsdictionary.com/word-lists/five-letter-words-in-scrabble/'
words = []
MAXGUESSES = 7
def fetchWords(n): ## Uses BeautifulSoup4 to download the list of 3-letter words
    print("Fetching list of words...")
    temp = []
    url = ""
    if n == 3:
        url = url3
    elif n == 4:
        url = url4
    elif n == 5:
        url = url5
    page = urlopen(url)
    html = page.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    for line in soup.getText().split('\n'):
        if len(line) == n:
            temp.append(line.lower()) ## Add the 3-letter word to the list
    print("Done.")
    return temp ## Return the list
def play(n): ## Play the game
    guesses = 0
    word = choice(words) ## Get a random word from the list
    ## print(f"Hidden word is: {word}")
    while(guesses < MAXGUESSES):
        guess = str(input("Guess a word > "))
        if(len(guess) != n): ## If word isn't 3 letters long
            print("Invalid Guess. Try Again.")
            continue
        if guess not in words: ## If word isn't valid
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


n = int(input("Number of letters in each word(3, 4 or 5): ")) ## words will contain n letters
if n not in [3, 4, 5]:
    print("Invalid number.")
    exit()
words = fetchWords(n) ## Get the list of words.
result, word = play(n) ## Play the game. Result = 0 means the user lost, result = 1 means the user won.

## Print appropriate game result
if(result == 0):
    print(f"\nYou lost! The correct word was {word}\n")
else:
    print("You won!")
