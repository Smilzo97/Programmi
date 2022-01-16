import pandas as pd

def import_word_file():
    df_words = pd.read_csv("C:/Users/gianm/Desktop/lista_parole.csv", sep =";")
    words =df_words("Gatto")
    print(words)

import_word_file()