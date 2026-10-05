import json
#TODO: Implement logging
#import logging

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
            obj = dict(json.load(raw))

            if not obj.get(self.GUESS_FIELD) or not obj.get(self.ANSWER_FIELD):
                raise json.JSONDecodeError #TODO: Write custom errors?
            else:
                response = {
                    self.RESPONSE_CODE_FIELD: 0,
                    self.FEEDBACK_FIELD: self._compare(obj[self.GUESS_FIELD], obj[self.ANSWER_FIELD])
                }
                return json.dumps(response)
            
        except json.JSONDecodeError:
            print("Unable to decode into JSON")
            return json.dumps({"response": -1, "feedback": []})

    def _compare(self, user_guess: str, correct_answer: str) -> str:
        
        if len(user_guess) != self.LETTERS_IN_WORD or len(correct_answer) != self.LETTERS_IN_WORD:
            return None
        
        to_match = []
        for letter in correct_answer:
            to_match.append((letter, False))

        match_feedback = ""
        for i in range(len(user_guess)):
            for j in range(len(to_match)):
                if user_guess[i] == to_match[j][0] and not to_match[j][1] and i == j:
                    to_match[j] = (to_match[j][0], True)
                    match_feedback += self.CORRECT_LETTER
                    break
                elif user_guess[i] == to_match[j][0] and not to_match[j][1]:
                    to_match[j] = (to_match[j][0], True)
                    match_feedback += self.VALID_LETTER
                    break
                else:
                    match_feedback += self.WRONG_LETTER
                    break

        return match_feedback