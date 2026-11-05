import sys, json
sys.path.append(".")
from engine.validation.validation import is_valid
from engine.evaluation.evaluator import *
from random import choice

def get_random_word() -> str:
    with open("resources/wordle-valid-words.txt", "r") as f:
        return choice(f.readlines()[10:8000]).lower().strip()

if __name__ == "__main__":
    repeat = True
    evaluator = Evaluation()
    while repeat:
        playing = True
        answer = get_random_word()
        
        while playing:
            guess = input("Guess a 5-letter word: ")
            input_json = json.dumps({"guess": guess, "answer": answer})
            if is_valid(guess):
                response = json.loads(evaluator.evaluate_raw(input_json))
                code = response.get("response_code", -1)
                if code < 0:
                    raise json.JSONDecodeError
                else:
                    feedback = response.get("feedback")
                    print(f"Feedback:\n{feedback}")
                    if feedback == "ggggg":
                        print("You win!")
                        playing = False
            else:
                print("Invalid word! Try again.")

        repeat = True if input("Play again?\n").lower() == "yes" else False

    print("Thanks for playing! Goodbye!")