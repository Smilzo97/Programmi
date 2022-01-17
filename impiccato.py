import pandas as pd
import random
import string

winners_list=[]
winner = ""
sequence = []
word = " "
ok = True
#global state2
#state2 = True 

global state2
def import_word_file():
    df_words = pd.read_csv("https://raw.githubusercontent.com/Smilzo97/Programmi/Inizio/lista_parole.csv")
    #print(df_words)
    words_list =df_words["PAROLE"]   
    print(words_list)
    return words_list

def chosen_word(w_list):
    #print(len(w_list))
    i = random.randint(0, len(w_list)-1)
    print(w_list.iloc[i])
    return w_list.iloc[i]

def insert_player():
    player = input('Inserisci nome giocatore: ')
    return player

def initialize():
    winner = ""
    wl = import_word_file()
    global word
    word = str(chosen_word(wl))
    global keyboard
    keyboard = []
    #print(word)
    for i in range(20 - (len(word))):
        keyboard.append(random.choice(string.ascii_letters).upper())  
    #print(keyboard)
    for char in word:
        global sequence 
        sequence.append("_ ")
        keyboard.append(char.upper())  
    #print(keyboard)
    random.shuffle(keyboard)
    print(keyboard)

def turn (name):
    print(name + " tocca a te")
    print(sequence)
    print("Scegli una lettera")
    inchar=input('Inserisci lettera: ')
    state = check_char(inchar,word)
    return state

def reveal_char(c):
    global ok
    count = 0 
    for i in range(len(word)):
        if c == word[i]:
           global sequence
           sequence[i] = c
           count= count+1

        if count == 0:
           ok = False
        else:
            ok = True
    print(ok)
    return ok

           
def check_char(c, word):
    print(word)
    if c in word:
        print("letetra presente")
        keyboard.remove(c.upper())
        ok2 = reveal_char(c)
        print(sequence)
        print(ok2)
        return ok2

def check_word():
    mystr =""
    for i in sequence:
        mystr=mystr+i

    if mystr == word:
        print("hai vinto")

def main():
    player1 = insert_player()
    player2 = insert_player()
    while True:
        initialize()
        #il gioco inizia
        global state2
        state2 = True
        while state2:
            state2 = turn(player1)
            check_word()
        turn(player2)
        break

if __name__ == "__main__":
    main()
else:
    print("Errore nell'avvio dell'applicazione")