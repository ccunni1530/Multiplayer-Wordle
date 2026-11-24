# Overview

The evaluation module is used to get feedback for a user's submitted
guess against a given answer and optional constraint. This is handled
through a singleton Evaluation class, which can take a JSON containing
each of these arguments and then return a response JSON.

# Evaluation Class

## Fields

- LETTERS_IN_WORD: describes the length of the words the class expects
(defaults to 5), and can be modified by calling set_word_length().

## Functions

- set_word_length(length: int)->None: Takes an integer length and sets
LETTERS_IN_WORD to it.

- evaluate_raw(raw: bytes)->bytes: Takes the raw bytes of a JSON and
evaluates the contents. Returns the bytes of a JSON response containing
feedback and a response code.