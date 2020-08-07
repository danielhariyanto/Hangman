import urllib.request
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_site)
txt = response.read().decode()
words = txt.splitlines()
word = random.choice(words)
word = word.lower()
letters_in_word = list(word)
game = list("-"*len(letters_in_word))
counter = (int(input("How many guesses would you like to have? ")))
y = []

def user_guesses():
    global counter
    i = str(input("Pick a letter: "))
    if i not in letters_in_word:
        counter = counter - 1
        y.append(i)
    else:
        for x in range(len(letters_in_word)):
            if i == letters_in_word[x]:
                game[x] = i
    return game

print(game)
print("------------------------------")

while counter != 0:
    print(user_guesses())
    print("You have",counter,"guesses left")
    print("Letters incorrectly guessed:", y)
    print("------------------------------")
    if "-" not in game:
        print("Game over - you won!")
        break

if counter == 0:
    print("Game over - you lost!")
    print("The word was", word)
