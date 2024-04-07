class File:

    def __init__(self, path: str):
        try:
            self.file = open(path, "r")
        except IOError:
            self.file = open(path, "wr+")
        self.type = path.split(".")[-1]

    def read_file(self):
        return self.file.read()

    def close_file(self):
        self.file.close()