import pandas as pd
import random
import string

winners_list=[]
winner = ""
sequence = []
word = " "
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
    return word, sequence

def reveal_char(c):
    global ok
    for i in range(len(word)):
        if c == word[i]:
           global sequence
           sequence[i] = c
        if count == 0:
           ok = False
        else:
            ok = True
    #print(ok)
    return ok

           
def check_char(c, word):
    print(word)
    if c in word:
        print("Lettera presente")
        keyboard.remove(c.upper())
        ok2 = reveal_char(c)
        #print(sequence)
        #print(ok2)
    else:
        print("Lettera NON presente")
        ok2 = False
    return ok2

def check_word_status(sequence, word, count):
    mystr =""
    end = True
    for i in sequence:
        mystr=mystr+i

    if mystr == word:
        print("HAI VINTO!")
        print("Gioco finito")
        end = False

    if count == len(word):
        print("HAI ESAURITO LE MOSSE")
        print("Gioco finito")
        end = False
    return end

def main():
    finish = True
    player = insert_player()
    while finish:
        word = ""
        word,sequence = initialize()
        #il gioco inizia
        global count
        count = 0
        global play
        play = True 
        while play:
            #print(name + " tocca a te")
            print(sequence)
            print("Scegli una lettera")
            inchar=input('Inserisci lettera: ')
            check_char_res = check_char(inchar,word)
            if check_char_res == True:
                print()
            else:
                count= count+1
            play = check_word_status(sequence, word, count)
    
        another_game = input("Vuoi fare un'altra partita (S/n)?    ")
        sequence.clear()
        
        if another_game == "n":
            finish = False
            

if __name__ == "__main__":
    main()
else:
    print("Errore nell'avvio dell'applicazione")