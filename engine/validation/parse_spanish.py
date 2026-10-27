# Parses spanish dictionary and adds words to a file spanish_words.txt

import pandas as pd
import requests
from io import StringIO
import unicodedata

# if a letter has an accent return the uppercase version of the letter
# if a letter does not have an accent return the letter
def is_accented(letter):
    normalized = unicodedata.normalize('NFD', letter)
    if len(normalized) > 1:
        return normalized[0].upper()
    return letter 

# loops through each letter in the word and captializes the letter if it has an accent
def update_word(word):
    word_list = list(word)
    for i in range(len(word_list)):
        word_list[i] = is_accented(word_list[i])
        updated_word = "".join(word_list)

    return updated_word

url = "https://www.spanishdict.com/guide/five-letter-spanish-words"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers, timeout=30)
response.raise_for_status()

tables = pd.read_html(StringIO(response.text))

file_path = "../../resources/spanish-valid-words.txt"
with open(file_path, 'w', encoding="utf-8") as file:
    for table in tables:
        for row in range(table.shape[0]):
            updated_word = update_word(table.iloc[row, 0])
            file.write(f"{updated_word}\n")

