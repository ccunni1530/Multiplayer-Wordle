# CMSC447 - Multiplayer-Wordle
# test_valid.py
# File to test the validation of wordle guesses


from engine.validation.validation import is_valid


def test_valid_word():
    assert is_valid("APPLE") == True
    assert is_valid("apple") == True




def test_invalid_word():
    assert is_valid("apples") == False
    assert is_valid("啊 哎 哀 唉 埃") == False
    assert is_valid("12345") == False
    assert is_valid("abcde") == False
    assert is_valid("ABCD") == False


# spanish words are not supported in the current implementation, so these tests are commented out for now.

# def test_spanish_word():
#     assert is_valid("árbol") == True


# def test_spanish_invalid_word():
#     assert is_valid("árboles") == False