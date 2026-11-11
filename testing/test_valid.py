# to run this test file, use the command: 
# pytest -v testing/test_valid.py
import json
import random
from engine.validation.validation import is_valid
from engine.validation.create_trie import trie, WORDS_FILE


# Test for valid words from the words file
def test_valid_word():
    with open(WORDS_FILE, 'r') as file:
        for line in file:
            if line[0] != "#" and line != "\n":
                assert is_valid(line.strip()) == True
                assert is_valid(line.strip().lower()) == True



# Basic test for special characters, may want to make it better later
def test_invalid_word():
    assert is_valid("啊 哎 哀 唉 埃") == False
    assert is_valid("12345") == False
    assert is_valid("") == False
    assert is_valid("!!!!!") == False


# Test for randomly generated invalid words
def test_random_invalid_word():
    word_list = []
    with open(WORDS_FILE, 'r') as file:
        for line in file:
            if line[0] != "#" and line != "\n":
                word_list.append(line.strip())

    word = generate_random_word(5)
    while word in word_list:
        word = generate_random_word(5)
    assert is_valid(word) == False
    assert is_valid(word.lower()) == False
    
    word = generate_random_word(4)
    assert is_valid(word) == False
    assert is_valid(word.lower()) == False
    word = generate_random_word(6)
    assert is_valid(word) == False
    assert is_valid(word.lower()) == False


# Helper function to generate random words for testing
def generate_random_word(length):
    word = ''
    for i in range(length):
        word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return word
    

    


# spanish words are not supported in the current implementation, so these tests are commented out for now.

# def test_spanish_word():
#     assert is_valid("árbol") == True


# def test_spanish_invalid_word():
#     assert is_valid("árboles") == False
