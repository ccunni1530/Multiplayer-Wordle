import json
from engine.validation.create_trie import Node, trie


# returns an list of all the valid wordle guesses
def setup_word_list_english():
    word_list = []

    with open(trie.words_file, "r") as file:
        for line in file:
            # first check that the line is not a comment or empty
            if line[0] != "#" and line != "\n":
                word_list.append(line.strip())

    return word_list

# returns the number of valid wordle guesses
def find_num_words(word_list):
    return len(word_list)

# tests that all of the valid wordle guesses have been inserted into Trie
def test_english_trie():
    word_list = setup_word_list_english()
    num_of_words = find_num_words(word_list)
    correct_words_count = 0

    for word in word_list:
        result = trie.search(word)
        if result:
            correct_words_count = correct_words_count + 1

    assert correct_words_count == num_of_words
    
