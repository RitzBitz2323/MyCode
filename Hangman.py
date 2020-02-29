def game():
    wordList = ["book", "godlike", "wallet", "martini", "government", "winter", "wanted", "fish", "ford", "ferrari", "tissue", "laptop","nintendo","pencil"]
    x = randint(0,len(wordList) - 1)
    word = wordList[x]
    winCond = false





print("Hangman Game")
name = ""
name = input("What's your name?")
print("Well hello" + name + " , Welcome to Hangman")
print("The rules are simple, A random word will be generated, and you'll have to guess it.")
print("You have 9 tries till you lose.")
print("GL HF")
