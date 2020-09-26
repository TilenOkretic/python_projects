import os


# PATTERN FOR THE GAME
def switch(i):
    switcher = {
        0: '___',
        1: '_|_',
        2: " | \n_|_",
        3: " | \n | \n | \n_|_",
        4: " |¯¯¯ \n | \n | \n_|_",
        5: ' |¯¯0 \n |  \n | \n_|_',
        6: ' |¯¯0 \n |  ^\n |  \n_|_',
        7: " |¯¯0 \n |  ^\n |  |\n |\n_|_",
        8: " |¯¯0 \n |  ^\n |  |\n |  ^\n_|_"
    }
    return switcher.get(i, "Invalid day of week")

target = ""
guessed = []
wrong = 0

def setAWord():
    global target
    os.system('clear')
    target=input('Set A word to guess:\n')
    os.system('clear')

def prepare():
    global target
    global guessed
    if(len(guessed) <= 0):
        os.system('clear')
        for i in range(len(target)):
            guessed.append("_")
    tmp = ""
    for l in guessed:
        tmp += l
    print(tmp)
    if(tmp.lower() == target.lower()):
        return True
    print('\n\n')
    print(switch(wrong))

def check(n):
    global target
    global guessed
    global wrong
    i = target.find(n)
    return False if (i == -1) else  i

def process(n,wd):
    global wrong
    global guessed
    os.system('clear')
    if(n is False or guessed[n] != "_"):
        wrong += 1
        if(wrong > len(target)):
            print("Game Over: You Lose!")
            return False
    else:
        guessed[n] = wd


def guess():
    val = input("\nGuess a letter:\n")
    if(process(check(val), val) is False):
        return
    else:
        game_loop()

def game_loop(): 
    global target
    global wrong
    global guessed
    if prepare():
        print('Game Over: You won!')
        return
    guess()
    #print(guessed)
setAWord()
game_loop()