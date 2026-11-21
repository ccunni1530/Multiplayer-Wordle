# Spanish word trie

`engine/validation/create_spanish_trie.py` loads `resources/spanish-valid-words.txt`
into a separate trie. Lookups are case-sensitive: uppercase letters in the
dictionary are retained as accent markers, so `aErea` matches while `aerea`
does not.

Run its tests with `pytest testing/test_spanish_trie.py`.