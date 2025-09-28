import pandas as pd
from prettytable import PrettyTable

HEADERS = ["Letter", "NATO Code"]

alphabet_data = pd.read_csv("nato_phonetic_alphabet.csv")
table = PrettyTable()
table.field_names = HEADERS
word = input("Enter a word: ").upper()

for letter in word:
    for (index, row) in alphabet_data.iterrows():
        if letter == row.letter:
            table.add_row([letter, row.code])

print(table)

#2


phonetic_dict = {row.letter:row.code for (index,row) in alphabet_data.iterrows()}
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
