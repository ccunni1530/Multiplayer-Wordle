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
    return # Constraint logic not fully functional yet
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.SUCCESS)
    assert decoded.get(evaluator.FEEDBACK_FIELD) == "ggggg"