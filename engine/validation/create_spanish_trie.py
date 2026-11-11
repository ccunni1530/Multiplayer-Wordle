from pathlib import Path

ROOT_DIRECTORY = Path(__file__).resolve().parent.parent.parent
DEFAULT_WORDS_FILE = ROOT_DIRECTORY / "resources" / "spanish-valid-words.txt"
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Node:
    def __init__(self):
        self.children = [None] * len(ALPHABET)
        self.isEndOfWord = False


class Trie:
    def __init__(self, words_file=DEFAULT_WORDS_FILE):
        self.root = Node()
        self.words_file = Path(words_file)
        self.load_words_from_file()

    def load_words_from_file(self):
        with self.words_file.open(encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                if word and not word.startswith("#"):
                    self.insert(word)

    def insert(self, word):
        curr = self.root

        for letter in word:
            index = ALPHABET.find(letter)
            if index == -1:
                raise ValueError(f"Unsupported character in Spanish word: {letter!r}")

            if curr.children[index] is None:
                curr.children[index] = Node()

            curr = curr.children[index]

        curr.isEndOfWord = True

    def search(self, key):
        curr = self.root
        for letter in key:
            index = ALPHABET.find(letter)
            if index == -1 or curr.children[index] is None:
                return False

            curr = curr.children[index]

        return curr.isEndOfWord


trie = Trie()
