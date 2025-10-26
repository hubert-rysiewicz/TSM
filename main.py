from src.log_processor import LogProcessor
from src.add_log import AddLog

data_file_path = "data/data.txt"

log = LogProcessor(data_file_path)
log.parse()
