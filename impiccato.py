import pandas as pd
import random
import string

sequence = []
word = " "

def import_word_file():
    df_words = pd.read_csv("https://raw.githubusercontent.com/Smilzo97/Programmi/Inizio/lista_parole.csv")
    #print(df_words)
    words_list =df_words["PAROLE"]   
    #print(words_list)
    return words_list

def chosen_word(w_list):
    #print(len(w_list))
    i = random.randint(0, len(w_list)-1)
    #print(w_list.iloc[i])
    return w_list.iloc[i].upper()

def insert_player():
    player = input('Inserisci nome giocatore: ')
    return player

def initialize():
    winner = ""
    global keyboard
    global word
    keyboard = []
    #print(word)
    wl = import_word_file()
    word = str(chosen_word(wl))
    for i in range(15 - (len(word))):
        keyboard.append(random.choice(string.ascii_letters).upper())  
    #print(keyboard)
    for char in word:
        global sequence 
        sequence.append("_ ")
        keyboard.append(char.upper())  
    #print(keyboard)
    random.shuffle(keyboard)
    #print(keyboard)
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

def delete_char(c):
    for index in range(len(keyboard)):
        print(keyboard[index])
        if keyboard[index] == c:
            keyboard.pop(index)
           
def check_char(c, word, errors):
    print(c)   
    if c in word:
        print("Lettera presente")
        ok2 = reveal_char(c)
        delete_char(c)
        #print(sequence)
        #print(ok2)
    else:
        print("Lettera NON presente")
        errors = errors+1
        delete_char(c)
        ok2 = False
    return ok2, errors

def check_word_status(sequence, word, count):
    mystr =""
    end = True
    for i in sequence:
        mystr=mystr+i

    if mystr == word:
        print()
        print("******************************************")
        print("HAI VINTO! La parola era: "+ word)
        print("Gioco finito")
        print("******************************************")
        end = False

    if count == len(word):
        print("******************************************")
        print("HAI ESAURITO LE MOSSE! La parola era: "+word)
        print("Gioco finito")
        print("******************************************")
        end = False
    return end

def main():
    global play
    global count
    global errors
    finish = True
    player = insert_player()
   

    while finish:
        word = ""
        word,sequence = initialize()
        #il gioco inizia
        count = 0
        errors = 0
        play = True 

        while play:
            #print(name + " tocca a te")à
            in_seq = True
            print()
            print("Mosse a disposizione: "+ str(len(word)-count))
            print("Errori: "+ str(errors))
            print()
            print(sequence)
            print(keyboard)
            print("Scegli una lettera")
            global inchar
            while in_seq:
                inchar=input('Inserisci lettera: ')
                if inchar.upper() in keyboard:
                    in_seq = False       
                else:
                    print("Inserisci un'altra lettera")
                    print()         
            check_char_res, errors = check_char(inchar.upper(),word, errors)
            if check_char_res == True:
                print()
            else:
                count= count+1
            play = check_word_status(sequence, word, count)
    
        another_game = input("Vuoi fare un'altra partita (S/n)?    ")
        sequence.clear()

        if another_game == "n":
            finish = False

    print("Arrivederci")            

if __name__ == "__main__":
    main()
else:
    print("Errore nell'avvio dell'applicazione")