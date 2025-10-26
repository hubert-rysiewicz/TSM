from datetime import datetime, timedelta

class ParseCases:
    def __init__(self):
        self.current_date = 0
        self.activities = []

    def date(self, line: str) -> bool:
        try:
            parsed_date = datetime.strptime(line, "%d/%m/%y")
        except ValueError:
            return False

        if self.current_date and not parsed_date - self.current_date == timedelta(days = 1):
            print(f"[WARN][parse_cases.py] Previous date: {self.current_date}. "
                  f"Received date: {parsed_date}. There may be missed days.")
        self.current_date = parsed_date
        return True
