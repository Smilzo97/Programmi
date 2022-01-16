import pandas as pd
import random

winners_list=[]
winner=""

 player1 = ""
 player2 = ""

def import_word_file():
    df_words = pd.read_csv("C:/Users/gianm/Desktop/lista_parole.csv", sep =";")
    words_list =df_words["PAROLE"]   
    print(words_list)
    return words_list

def chosen_word(w_list):
    #print(len(w_list))
    i = random.randint(0, len(w_list)-1)
    print(w_list.iloc[i])

def main():
    wl = import_word_file()
    word = chosen_word(wl)
   

if __name__ == "__main__":
    main()
else:
    print("Errore nell'avvio dell'applicazione")