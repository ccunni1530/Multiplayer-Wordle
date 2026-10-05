from enum import Enum
import json
#TODO: Implement logging
#import logging

class ResponseCode(Enum):
    SUCCESS = 0
    INVALID_JSON = -1
    INVALID_GUESS = -2
    INVALID_ANSWER = -3

class Feedback(Enum):
    UNCHECKED = 0
    WRONG_LETTER = 1
    VALID_LETTER = 2
    CORRECT_LETTER = 3

class Evaluation:
    GUESS_FIELD = "guess"
    ANSWER_FIELD = "answer"
    RESPONSE_CODE_FIELD = "response_code"
    FEEDBACK_FIELD = "feedback"
    WRONG_LETTER = "b"
    VALID_LETTER = "y"
    CORRECT_LETTER = "g"
    LETTERS_IN_WORD = 5

    def evaluate_raw(self, raw: bytes) -> bytes:
        try:
            obj = dict(json.loads(raw))

            if not obj.get(self.GUESS_FIELD) or not obj.get(self.ANSWER_FIELD):
                raise json.JSONDecodeError #TODO: Write custom errors?
            else:
                response = {
                    self.RESPONSE_CODE_FIELD: ResponseCode.SUCCESS.value,
                    self.FEEDBACK_FIELD: self._compare(obj[self.GUESS_FIELD], obj[self.ANSWER_FIELD])
                }
                return json.dumps(response)
            
        except json.JSONDecodeError:
            print("Unable to decode into JSON")
            return json.dumps({"response": ResponseCode.INVALID_JSON.value, "feedback": []})

    def _compare(self, user_guess: str, correct_answer: str) -> str:
        
        if len(user_guess) != self.LETTERS_IN_WORD or len(correct_answer) != self.LETTERS_IN_WORD:
            return None
        
        to_match = []
        for letter in correct_answer:
            to_match.append((letter, Feedback.UNCHECKED))

        match_feedback = ""
        for i in range(len(user_guess)):
            colored = False
            for j in range(len(to_match)):
                print(f"Comparing {user_guess[i]} to {to_match[j][0]} with feedback {to_match[j][1]}")

                # Green letters must be in the same position and match the letter
                if i == j and user_guess[i] == to_match[j][0]:
                    to_match[j] = (to_match[j][0], Feedback.CORRECT_LETTER)
                    match_feedback += self.CORRECT_LETTER
                    colored = True
                    break

                # Yellow letters only appear if the letter it matches to isn't already perfectly matched
                elif user_guess[i] == to_match[j][0] and to_match[j][0] != user_guess[j]:
                    to_match[j] = (to_match[j][0], Feedback.VALID_LETTER)
                    match_feedback += self.VALID_LETTER
                    colored = True
                    break

            # Black letters will appear even if the letter is in the answer but is covered by a previous yellow
            if not colored:
                match_feedback += self.WRONG_LETTER

        return match_feedback

#print(Evaluation().evaluate_raw(b'{"guess": "bbcde", "answer": "abcde"}'))