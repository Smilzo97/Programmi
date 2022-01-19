#importo librerie
import pandas as pd
import random
import string

sequence = []
word = " "

#dichiaro funzione per importare file csv con le parole
def import_word_file():
    #uso libreria Pandas per la gestione del file csv
    df_words = pd.read_csv("https://raw.githubusercontent.com/Smilzo97/Programmi/Inizio/lista_parole.csv")
    #il risultato dell'import è sottoforma di dataset
    #attraverso la seguente riga, estraggo le parole nella colonna "PAROLE"
    words_list =df_words["PAROLE"]   
    return words_list

def chosen_word(w_list):
    #Genero un numero i randomico ed estraggo la parola in posizone i
    iw = random.randint(0, len(w_list)-1)
    #restituisco la parola in maiuscolo
    return w_list.iloc[iw].upper()

def insert_player():
    #inserisco il nome del giocatore
    player = input('Inserisci nome giocatore: ')
    return player

def initialize():
    #genrto variabili 
    winner = ""
    global keyboard
    global word
    keyboard = []

    #importo e scelgo la parola
    wl = import_word_file()
    word = str(chosen_word(wl))
    #popolo la mia tastiera con le lettere della parola e casuali
    #sono tutte in maisucolo
    i = 0
    for i in range(18 - (len(word))):
        keyboard.append(random.choice(string.ascii_letters).upper())  

    #per ogni lettera nella parola da indovinare, genero un _ e lo aggiungo ad una lista
    for char in word:
        global sequence 
        sequence.append("_ ")
        #aggiungo la lettera alla tastiera
        keyboard.append(char.upper())  
    #eseguo uno shuffle per mischiare le lettere
    random.shuffle(keyboard)
    return word, sequence

def reveal_char(c):
    global ok_reveal
    #controllo che la lettera inserita corrisponda ad una o più lettere nella parola da indovinare
    i = 0
    for i in range(len(word)):
        if c == word[i]:
           global sequence
           #sostituisco
           sequence[i] = c
        
        #controllo se ha indovinato o no
        if count == 0:
           ok_reveal = False
        else:
            ok_reveal = True
    
    return ok_reveal

def delete_char(c):
    #controllo ogni elemento della lista ed elimino l'elemento in caso di corrispondenza
    index = 0
    for index in keyboard:
        if index == c:
            keyboard.remove(index)
           
def check_char(c, word, errors):
    #controllo ogni lettera
    if c in word:
        #se è presente la rilevo e la elimino
        print("--  Lettera presente  --")
        ok = reveal_char(c)
        delete_char(c)

    else:
        print(" --  Lettera NON presente  --")
        #se non è presente aumento il numero degli errori 
        errors = errors+1
        delete_char(c)
        ok = False
    return ok, errors

#controllo se il giocatore ha vinto o no
def check_word_status(sequence, word, err):
    mystr =""
    end = True
    i = 0
    for i in sequence:
        mystr=mystr+i

    if mystr == word:
        print("")
        print("******************************************")
        print("HAI VINTO! La parola era: "+ word)
        print("Gioco finito")
        print("******************************************")
        end = False

    if err == 6:
        print("")
        print("******************************************")
        print("HAI PERSO! MOSSE ESAURITE! La parola era: "+word)
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
        end_char =True

        while play:
            #print(name + " tocca a te")à
            in_seq = True
            #mostro gli spazi e la tastiera
            print()
            print("Mosse a disposizione: "+ str(6-errors))
            print("Errori: "+ str(errors))
            print("")
            print(sequence)
            print("")
            print(keyboard)
            #print("Scegli una lettera")
            global inchar
            #chiedo inserimento lettera. Finchè non inserisce una lettera presente nella tastiera, non va avanti
            while in_seq:
                inchar=input('Inserisci lettera: ')
                if inchar.upper() in keyboard:
                    in_seq = False       
                else:
                    print("Inserisci un'altra lettera")
                    print()      
            #controlli   
            check_char_res, errors = check_char(inchar.upper(),word, errors)            
            play = check_word_status(sequence, word, errors)
            print()
            print("----------------------------------------------------")
        #chiedo se vuole rigiocare e finchè non inserisce S (Si) o n (no) non va avanti
        while end_char:
            another_game = input("Vuoi fare un'altra partita (S/n)?    ")
            if another_game =="S" or another_game == "n":
                end_char = False
        #pulisco la sequenza
        sequence.clear()

        if another_game == "n":
            finish = False

    print("Arrivederci")            

if __name__ == "__main__":
    main()
else:
    print("Errore nell'avvio dell'applicazione")