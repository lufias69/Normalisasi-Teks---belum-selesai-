import pandas as pd
from unidecode import unidecode
fo = pd.read_excel('data/karakter.xlsx', sheet_name='Sheet1')
x = fo['karakter'].tolist() #
y = fo['replace'].tolist()
def gantiKarakter(str, x=x, y=y):
    for i in range(len(x)):
        if i == 0:
            n_word = str
        n_word = n_word.replace(x[i],y[i])
    return unidecode(n_word).lower()