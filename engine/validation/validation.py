# CMSC447 - Multiplayer-Wordle
# validation.py
# File to validate wordle guesses

import engine.validation.create_trie as create_trie

def is_valid(word):

    trie = create_trie.trie
    ##Check for valid length (may not matter at all)
    if len(word) != 5:
        return False

    ##make sure word matches format of our library
    word = word.strip().upper()

    ##check for valid chars
    if not all('A' <= c <= 'Z' for c in word):
        return False


    return trie.search(word)
