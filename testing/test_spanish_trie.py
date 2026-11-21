from engine.validation.create_spanish_trie import trie


def test_spanish_trie_contains_all_dictionary_words():
    with trie.words_file.open(encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip() and not line.startswith("#")]

    assert words
    assert all(trie.search(word) for word in words)


def test_uppercase_letters_preserve_accent_markers():
    assert trie.search("aErea")
    assert not trie.search("aerea")
