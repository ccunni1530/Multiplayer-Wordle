from enum import Enum
import json
#TODO: Implement logging
#import logging

class ResponseCode(Enum):
    SUCCESS = 0
    INVALID_JSON = -1
    INVALID_GUESS = -2 # The guess parameter is invalid (i.e. wrong length or violates constraint)
    INVALID_ANSWER = -3 # The answer parameter is invalid (i.e. wrong length)

    def __int__(self):
        return self.value
    
class Feedback(Enum):
    UNCHECKED = 0
    WRONG_LETTER = 1
    VALID_LETTER = 2
    CORRECT_LETTER = 3

    def __int__(self):
        return self.value

class Evaluation:
    GUESS_FIELD = "guess"
    ANSWER_FIELD = "answer"
    CONSTRAINT = "constraint"
    KNOWN_LETTERS = "known_letters"
    RESPONSE_CODE_FIELD = "response_code"
    FEEDBACK_FIELD = "feedback"
    WRONG_LETTER = "b"
    VALID_LETTER = "y"
    CORRECT_LETTER = "g"
    LETTERS_IN_WORD = 5

    """
    Gets the raw bytes containing a JSON-formatted guess and evaluates
    the user submission against a given answer (with an optional
    constraint check, as well). Returns the raw bytes containing a
    JSON-formatted response that has G/Y/B feedback alongside a
    response code.
    """
    @classmethod
    def evaluate_raw(cls, raw: bytes) -> bytes:
        try:
            obj = dict(json.loads(raw))

            if not obj.get(cls.GUESS_FIELD) or not obj.get(cls.ANSWER_FIELD):
                raise json.JSONDecodeError("Missing fields", "request", 0) #TODO: Write custom errors?
            else:

                # Check if the guess fits the current constraint (if any)
                guess = obj.get(cls.GUESS_FIELD)
                answer = obj.get(cls.ANSWER_FIELD)
                constraint = obj.get(cls.CONSTRAINT)
                known_letters = obj.get(cls.KNOWN_LETTERS)
                if constraint and known_letters and not cls._check_constraint(guess, answer, constraint, known_letters):
                    return json.dumps({cls.RESPONSE_CODE_FIELD: ResponseCode.INVALID_GUESS.value, "feedback": []})
                elif constraint and not known_letters:
                    return json.dumps({cls.RESPONSE_CODE_FIELD: ResponseCode.INVALID_JSON.value, "feedback": []})
                    
                response = {
                    cls.RESPONSE_CODE_FIELD: ResponseCode.SUCCESS.value,
                    cls.FEEDBACK_FIELD: cls._compare(obj[cls.GUESS_FIELD], obj[cls.ANSWER_FIELD])
                }
                return json.dumps(response)

        except json.JSONDecodeError:
            print("Unable to decode into JSON")
            return json.dumps({cls.RESPONSE_CODE_FIELD: ResponseCode.INVALID_JSON.value, "feedback": []})

    """
    Checks if the user's guess works within the current constraints of the
    game. Returns True if it does and False otherwise.
    """
    @classmethod
    def _check_constraint(cls, guess: str, answer: str, constraint: str, \
                          known_letters: str) -> bool:
        known_frequencies = {}
        for i in range(cls.LETTERS_IN_WORD):

            # Must be correct letter in position
            if constraint[i] == cls.CCORRECT_LETTER and guess[i] != answer[i]:
                return False

            # Cannot use letter in position the user knows it's not
            elif constraint[i] in [cls.WRONG_LETTER, cls.VALID_LETTER] and guess[i] == answer[i]:
                return False

            # Tally yellow letters to ensure they're all used
            elif constraint[i] == cls.VALID_LETTER:
                if not known_frequencies.get(answer[i]):
                    known_frequencies[answer[i]] = 1
                else:
                    known_frequencies[answer[i]] += 1

        # Confirm tally match for guess and answer
        for i in range(cls.LETTERS_IN_WORD):
            if guess[i] in known_frequencies.keys() \
                and constraint[i] != cls.CORRECT_LETTER: # Doesn't double-count greens
                    known_frequencies[guess[i]] -= 1

        # Ensure yellow letter frequency matches in answer and guess
        for tally in known_frequencies.values():
            if tally != 0:
                return False

    """
    Returns the difference between the user's guess and the answer in
    the form of G/Y/B feedback.
    """
    @classmethod
    def _compare(cls, user_guess: str, correct_answer: str) -> str:
        
        if len(user_guess) != cls.LETTERS_IN_WORD or len(correct_answer) != cls.LETTERS_IN_WORD:
            return None
        
        to_match = []
        for letter in correct_answer:
            to_match.append((letter, Feedback.UNCHECKED))

        match_feedback = ""
        for i in range(len(user_guess)):
            colored = False
            for j in range(len(to_match)):

                # Green letters must be in the same position and match the letter
                if i == j and user_guess[i] == to_match[j][0]:
                    to_match[j] = (to_match[j][0], Feedback.CORRECT_LETTER)
                    match_feedback += cls.CORRECT_LETTER
                    colored = True
                    break

                # Yellow letters only appear if the letter it matches to isn't already perfectly matched
                elif user_guess[i] == to_match[j][0] and to_match[j][0] != user_guess[j]:
                    to_match[j] = (to_match[j][0], Feedback.VALID_LETTER)
                    match_feedback += cls.VALID_LETTER
                    colored = True
                    break

            # Black letters will appear even if the letter is in the answer but is covered by a previous yellow
            if not colored:
                match_feedback += cls.WRONG_LETTER

        return match_feedback