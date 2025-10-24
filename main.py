from src.log_entry import LogEntry
from src.parse_cases import ParseCases

data_file_path = "data/data.txt"

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

log = LogEntry(read_file(data_file_path))
