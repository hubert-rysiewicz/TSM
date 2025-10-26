from src.log_processor import LogProcessor

data_file_path = "data/data.txt"

log = LogProcessor(data_file_path)
log.parse()
