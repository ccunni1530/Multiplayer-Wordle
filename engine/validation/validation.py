import engine.validation.create_trie as create_trie
import engine.validation.create_spanish_trie as create_spanish_trie

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

def is_valid_spanish(word):
    trie = create_spanish_trie.trie

    if len(word) != 5:
        return False

    ##do not .upper() for spanish bc will mess up accents
    word = word.strip()

     ##check for valid chars
    if not all('A' <= c <= 'Z' or 'a' <= c <= 'z' for c in word):
        return False

    return trie.search(word)