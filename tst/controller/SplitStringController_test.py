from src.controller.SplitStringController import splitStringRequestIsValid, splitString

class FakeRequest:
    def __init__(self, jsonRequest):
        self.jsonRequest = jsonRequest

    def get_json(self):
        return self.jsonRequest

def testSplitValidString():
    request = FakeRequest({"string_to_split": "12a34b56cno"})
    response = splitString(request)
    assert(isinstance(response, dict))
    assert(response.get("return_string") is not None)
    assert(response.get("return_string") == "abc")

def testSplitValidShortString():
    request = FakeRequest({"string_to_split": "ab"})
    response = splitString(request)
    assert(isinstance(response, dict))
    assert(response.get("return_string") is not None)
    assert(response.get("return_string") == "")

def testSplitEmptyString():
    request = FakeRequest({"string_to_split": ""})
    response = splitString(request)
    assert(isinstance(response, dict))
    assert(response.get("return_string") is not None)
    assert(response.get("return_string") == "")

def testSplitBadRequest():
    request = FakeRequest({"string_to_split": 1})
    response = splitString(request)
    assert(not isinstance(response, dict))
    assert(response[0] == "bad request")
