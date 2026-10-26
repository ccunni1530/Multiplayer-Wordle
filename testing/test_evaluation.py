import json
from engine.evaluation.evaluator import Evaluation, ResponseCode, Feedback

evaluator = Evaluation()
def test_reject_null():
    response = evaluator.evaluate_raw(b"{}")
    decoded = dict(json.loads(response))
    print(decoded)
    assert decoded.get(evaluator.RESPONSE_CODE_FIELD) == int(ResponseCode.INVALID_JSON)