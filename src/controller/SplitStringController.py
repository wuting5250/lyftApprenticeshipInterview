from flask_api import status
import json

def splitStringRequestIsValid(requestJson):
    if not requestJson or requestJson.get("string_to_cut") is None or \
        not isinstance(requestJson.get("string_to_cut"), str):
        return False
    return True


def splitString(request):
    splitRequest = request.get_json()
    if not splitStringRequestIsValid(splitRequest):
        return "bad request", status.HTTP_400_BAD_REQUEST
    stringToSplit = splitRequest.get("string_to_cut")
    thirdChars = ""
    if len(stringToSplit) >= 3:
        for i in range(0, len(stringToSplit) + 1, 3):
            if i != 0:
                thirdChars += stringToSplit[i - 1]
    return {"return_string": thirdChars}
