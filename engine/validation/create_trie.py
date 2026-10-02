# Cmsc447 - Multiplayer-Wordle
# create_trie.py
# File to parse valid word list and create trie of words

# create trie
class Node:
    def __init__(self):
        self.children = [None] * 26 # 26 letters in alphabet
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    # function to insert word into trie 
    def insert(self, word):
        curr = self.root

        # iterate through each character in the word
        for c in word:
            # ord converts a char into is corresponding integer value
            index = ord(c) - ord('A')

            if curr.children[index] is None:
                # create new node
                new_node = Node()
                # add new_node at this index
                curr.children[index] = new_node

            # update curr pointer
            curr = curr.children[index]

        # last node/char will be marked as the end of the word
        curr.isEndOfWord = True

    # Function to search Trie for a word or prefix
    def search(self, key):
        curr = self.root
        for c in key:
            index = ord(c) - ord('A')

            # check if index exists in curr node's child
            if curr.children[index] is None:
                return False
            
            curr = curr.children[index]
            
        return curr.isEndOfWord

# Create Trie object
trie = Trie()

# open wordle-valid-words.txt and parse all the valid words to an array word_list
with open('../../resources/wordle-valid-words.txt', 'r') as file:
    for line in file:
        # first check that the line is not a comment or empty
        if line[0] != "#" and line != "\n":
            trie.insert(line.strip())