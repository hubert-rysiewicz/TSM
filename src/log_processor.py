from .parse_cases import ParseCases
from typing import Iterator

class LogProcessor:
    #Read file contents and returns list of lines
    @staticmethod
    def read_file(file_path: str) -> Iterator[str]:
        with open(file_path, "r") as file:
            # Line normalisation strips of unnecessary contents such
            # as spaces, blank elements and rich format new lines (/n)
            for line in file:
                line = line.strip()
                if line:
                    yield line #Returns generator

    def __init__(self, data_file_path: str) -> None:
        # List method is used because "read_file" is a generator (yield)
        self.text = list(LogProcessor.read_file(data_file_path))
        self.parser = ParseCases()

    #Parse each line of text by mapping to each type
    def parse(self) -> None:
        for line in self.text:
            if self.parser.date(line):
                continue
            self.parser.content(line)





