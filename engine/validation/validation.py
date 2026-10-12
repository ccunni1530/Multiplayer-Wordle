##Trey working on this section
##Then efficiently performs a word lookup to check that the user input is a real word.
##Validate that the word guessed by the user is one of the 8636 real 5-letter words provided in the wordle dictionary. Create a search function to traverse trie data structure.


import create_trie

def is_valid(trie, word):

    ##Check for valid length (may not matter at all)
    if len(word) != 5:
        return False

    ##check for valid chars
    if not all('A' <= c <= 'Z' for c in word):
        return False

    ##make sure word matches format of our library
    word = word.strip().upper()


    return trie.search(word)
