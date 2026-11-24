import json
import os.path
from engine.evaluation.evaluator import Evaluation as evaluator, ResponseCode, Feedback

def __run_engine(file_name: str) -> bytes:
    response = None
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "sample_input",
        file_name
    )
    with open(path, "rb") as f:
        response = evaluator.evaluate_raw(f.read())
    return json.loads(response)

def test_reject_null():
    decoded = dict(__run_engine("invalid2.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_JSON)

def test_reject_invalid():
    decoded = dict(__run_engine("invalid1.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_JSON)

def test_accept_1():
    decoded = dict(__run_engine("valid1.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.SUCCESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == "bbybb"

def test_accept_2():
    decoded = dict(__run_engine("valid2.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.SUCCESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == "bbbbb"

def test_accept_3():
    decoded = dict(__run_engine("valid3.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.SUCCESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == "ggggg"

def test_reject_dropped_green():
    decoded = dict(__run_engine("constraint_drop_green.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_GUESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == []

def test_accept_green_kept_yellow_moved():
    decoded = dict(__run_engine("constraint_accept_hasty.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.SUCCESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == "ggybb"

def test_reject_yellow_same_position():
    decoded = dict(__run_engine("constraint_yellow_same_spot.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_GUESS)

def test_accept_yellow_moved():
    decoded = dict(__run_engine("constraint_yellow_moved.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.SUCCESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == "bgggg"

def test_reject_yellow_dropped():
    decoded = dict(__run_engine("constraint_yellow_dropped.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_GUESS)

def test_reject_absent_letter_in_black_slot():
    decoded = dict(__run_engine("constraint_absent_black_slot.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_GUESS)

def test_reject_absent_letter_in_yellow_slot():
    decoded = dict(__run_engine("constraint_absent_yellow_slot.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_GUESS)

def test_accept_empty_absent_letters():
    decoded = dict(__run_engine("constraint_empty_absent.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.SUCCESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == "ggggg"

def test_reject_duplicate_yellow_underused():
    decoded = dict(__run_engine("constraint_dup_yellow_reject.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_GUESS)

def test_accept_duplicate_yellow_used():
    decoded = dict(__run_engine("constraint_dup_yellow_accept.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.SUCCESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == "byggg"

def test_reject_constraint_missing_known_positions():
    decoded = dict(__run_engine("constraint_missing_positions.json"))
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_JSON)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == []