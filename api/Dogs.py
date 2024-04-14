import json


class Dogs():
    def __init__(self):
        pass

    def get_status_from_body(self, response):
        dict_from_body = json.loads(response.text)
        return dict_from_body["status"]

    def get_message_from_body(self, response):
        dict_from_body = json.loads(response.text)
        return dict_from_body["message"]

    def get_expected_breeds(self, PATH_EXPECTED_BREEDS):
        with open(PATH_EXPECTED_BREEDS, "r") as file:
            breeds = [line.partition('\n')[0] for line in file]
        return breeds
