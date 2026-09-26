import json
class TestDataReader:
    @staticmethod
    def read_json(file_path):
        with open(file_path, "r") as file:
           return json.load(file)

