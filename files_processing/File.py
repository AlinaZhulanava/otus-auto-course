import os.path

FILES_DIR = os.path.dirname(__file__)
class File:

    def __init__(self, path: str):
        try:
            self.file = open(path, "r")
        except IOError:
            self.file = open(path, "a")
        self.type = path.split(".")[-1]

    def read_file(self):
        return self.file.read()

    def close_file(self):
        self.file.close()

    def write_file(self, text):
        path=os.path.join(FILES_DIR, "result.json")
        self.file = open(path, "a")
        self.file.write(text)
        self.file.close()