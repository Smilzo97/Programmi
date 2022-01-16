import pandas as pd
import random
import string

winners_list=[]
winner = ""
sequence ="_ "

def import_word_file():
    df_words = pd.read_csv("C:/Users/gianm/Desktop/lista_parole.csv", sep =";")
    words_list =df_words["PAROLE"]   
    print(words_list)
    return words_list

def chosen_word(w_list):
    #print(len(w_list))
    i = random.randint(0, len(w_list)-1)
    print(w_list.iloc[i])
    return w_list.iloc[i]

def insert_players():
    player1 = input('Inserisci nome giocatore1: ')
    player2 = input('Inserisci nome giocatore2: ')

def initialize():
    winner = ""
    wl = import_word_file()
    word = str(chosen_word(wl))
    keyboard = []
    #print(word)
    for i in range(20 - (len(word))):
        keyboard.append(random.choice(string.ascii_letters).upper())  
    #print(keyboard)
    for char in word:
        global sequence
        sequence = sequence + "_ "
        keyboard.append(char.upper())  
    #print(keyboard)
    random.shuffle(keyboard)
    print(keyboard)

def turn (name):
    print(name + " tocca a te")
    print(sequence)
    print("Scegli una lettera")

def main():
    while True:
        insert_players()
        initialize()
        
        #il gioco inizia
        turn("player")
        
        break

if __name__ == "__main__":
    main()
else:
    print("Errore nell'avvio dell'applicazione")