import pytest

from engine.validation.create_spanish_trie import Trie, trie


def test_spanish_trie_contains_all_dictionary_words():
    with trie.words_file.open(encoding="utf-8") as file:
        words = [line.strip() for line in file if line.strip() and not line.startswith("#")]

    assert words
    assert all(trie.search(word) for word in words)


def test_uppercase_letters_preserve_accent_markers():
    assert trie.search("aErea")
    assert not trie.search("aerea")


@pytest.mark.parametrize(
    ("marked_word", "accented_word"),
    [
        ("aErea", "área"),
        ("actUa", "actúa"),
        ("Agape", "ágape"),
        ("Anade", "ánade"),
    ],
)
def test_accent_markers_require_the_uppercase_placeholder(marked_word, accented_word):
    assert trie.search(marked_word)
    assert not trie.search(accented_word)
    assert not trie.search(marked_word.lower())


@pytest.mark.parametrize(
    "unknown_word",
    [
        "",
        "act",
        "actU",
        "12345",
        "aerea",
        "árbol",
    ],
)
def test_trie_rejects_missing_words_and_prefixes(unknown_word):
    assert not trie.search(unknown_word)


def test_search_distinguishes_words_from_prefixes():
    assert not trie.search("act")
    assert not trie.search("actU")
    assert trie.search("actUa")


def test_custom_trie_loads_comments_and_blank_lines(tmp_path):
    words_file = tmp_path / "spanish_words.txt"
    words_file.write_text("# dictionary\n\ncasa\ncAsa\n", encoding="utf-8")

    custom_trie = Trie(words_file)

    assert custom_trie.search("casa")
    assert custom_trie.search("cAsa")
    assert not custom_trie.search("CASA")
    assert not custom_trie.search("cas")


def test_insert_and_search_support_case_sensitive_words(tmp_path):
    words_file = tmp_path / "empty.txt"
    words_file.write_text("", encoding="utf-8")
    custom_trie = Trie(words_file)

    custom_trie.insert("nInO")

    assert custom_trie.search("nInO")
    assert not custom_trie.search("nino")
    assert not custom_trie.search("nI")


def test_insert_rejects_unsupported_characters(tmp_path):
    words_file = tmp_path / "empty.txt"
    words_file.write_text("", encoding="utf-8")
    custom_trie = Trie(words_file)

    with pytest.raises(ValueError, match="Unsupported character"):
        custom_trie.insert("árbol")

    assert not custom_trie.search("árbol")
