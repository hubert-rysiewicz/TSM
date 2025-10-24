from src.log_entry import LogEntry
from src.parse_cases import ParseCases

data_file_path = "data/data.txt"

#Reading the contents inside var "data_file_path"
def read_file(file_path):
    with open(file_path, "r") as file:
        #Line normalisation strips of unnecessary contents such
        #as spaces, blank elements and rich format new lines
        for line in file:
            line = line.strip()
            if line:
                yield line

#Sending extracted and normalised text data to "src/log_entry" module
#List method is used because "read_file" is a generator (yield)
log = LogEntry(list(read_file(data_file_path)))
