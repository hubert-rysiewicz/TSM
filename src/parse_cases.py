from datetime import datetime, timedelta
from .content_rules import ContentRules, RULES_MAP

class ParseCases:
    def __init__(self):
        self.current_date = None
        self.activities = {}

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

    def content(self, line: str) -> bool:
        try:
            line.split("-")
        except Exception:
            return False

        parsed_time, parsed_activity = line.split("-")
        if "(" in parsed_activity:

        function = RULES_MAP.get(last_word)
        if function:
            function(activity_parameters)
        return True