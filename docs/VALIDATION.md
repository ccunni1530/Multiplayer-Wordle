
# Overview

The validation module is responsible for determining whether the user
enters a valid guess. In order for a guess to be valid, it must be 
included in the official list of allowed wordle guesses for the 
corresponding English or Spanish dictionary. The users guess will be 
passed a string to the validation function.

## Functions

- is_valid(word): Takes the raw string entered by the user and returns 
a boolen. `True` indicates the word is in the valid English words dictionary.
`False` indicates the word is not in the valid English words dictionary.

- is_valid_spanish(word): Takes the raw string entered by the user and returns 
a boolen. `True` indicates the word is in the valid Spanish words dictionary.
`False` indicates the word is not in the valid Spanish words dictionary.

## Usage

Import the validation functions from `engine.validation.validation`.