# Multiplayer Wordle Logic
## Background
This repository supports the middle-layer systems for a multiplayer Wordle. Players will alternate submitting a guess, to achieve the goal of correctly guessing the five-letter target. All clues revealed will become public knowledge to all players. This repository contains the logic components behind the game; it performs validation checks on the given user input, ensuring it's a valid fiver-letter word. 

This project is based on the requirements specified in the CMSC 447 Capstone Project Portfolio. This project is expected to take around 2.5 to 3 months to complete.

## Components

├── README.md

├── docs

├── engine

│   ├── evaluation

│   └── validation

└── testing

[//]: # (This tree layout can be retrieved by running the "tree" command in bash)

### engine
The directory containing all of the logic for the system. `engine/evaluation` compares the input to the answer and provides feedback (letter presence, placement, etc.). `engine/validation` efficiently performs a word lookup to check that the user input is a real word. For maximum performance, word validation is done before evaluation.