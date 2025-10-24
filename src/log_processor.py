from .parse_cases import ParseCases
from typing import Iterator

class LogProcessor(ParseCases):
    #Read file contents and returns list of lines
    @staticmethod
    def read_file(file_path: str) -> Iterator[str]: #Returns generator not list
        with open(file_path, "r") as file:
            # Line normalisation strips of unnecessary contents such
            # as spaces, blank elements and rich format new lines
            for line in file:
                line = line.strip()
                if line:
                    yield line

    def __init__(self, data_file_path: str) -> None:
        # List method is used because "read_file" is a generator (yield)
        self.text = list(LogProcessor.read_file(data_file_path))

    def separate(self):
        print(self.text)




