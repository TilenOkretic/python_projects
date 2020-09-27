import os
import sys


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

target = "" if(len(sys.argv) <= 1) else sys.argv[1]
used = []
guessed = []
wrong = 0

def setAWord():
    global target
    os.system('clear')
    if(target is ""):
        target=input('Set A word to guess:\n')
    os.system('clear')

def prepare():
    global target
    global guessed
    if(len(guessed) <= 0):
        os.system('clear')
        for i in range(len(target)):
            if(target[i] != " "):
                guessed.append("_")
            else:
                guessed.append(" ")
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
    global used
    os.system('clear')
    if(n is False or guessed[n] != "_"):
        wrong += 1
        if(wrong > len(target)):
            print("Game Over: You Lose!")
            return False
    else:
        for i in range(len(target)):
            if(target[i] == wd):
                guessed[i] = wd
    if(not wd in used):
        used.append(wd + ", ")


def guess():
    used_tmp = ""
    for l in used:
        used_tmp += l
    print('\nUsed letters:\n',used_tmp)
    val = input("Guess a letter:\n")
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