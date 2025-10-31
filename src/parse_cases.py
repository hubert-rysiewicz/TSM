from datetime import datetime, timedelta
from .content_rules import ContentRules, RULES_MAP

class ParseCases:
    def __init__(self):
        self.current_date = None
        self.activities = {}

    #If parameter (line) is a date, runs date handler
    def date(self, line: str) -> bool:
        try:
            parsed_date = datetime.strptime(line, "%d/%m/%y")
        except ValueError:
            return False

        #Date handler checks if found date is the next date to previous
        #date, if not, runs warning, else, changes date to found date
        if self.current_date and not parsed_date - self.current_date == timedelta(days = 1):
            print(f"[WARN][parse_cases.py] Previous date: {self.current_date}. "
                  f"Received date: {parsed_date}. There may be missed days.")
        self.current_date = parsed_date
        return True

    @staticmethod
    def clean(*args) -> list[str]:
        return [arg.strip() for arg in args]

    @staticmethod
    def activity_parameter_checker(parsed_activity: str) -> tuple[str, str]:
        parsed_parameters: str = ""
        if "|" in parsed_activity:
            parsed_activity, parsed_parameters = parsed_activity.split("|")
        return parsed_activity, parsed_parameters


    def content(self, line: str) -> bool:
        try:
            line.split("-")
        except TypeError:
            return False

        parsed_time, parsed_activity = line.split("-")
        parsed_activity, parsed_parameters = self.activity_parameter_checker(parsed_activity)
        parsed_time, parsed_activity, parsed_parameters = self.clean(parsed_time, parsed_activity, parsed_parameters)
        last_word = parsed_activity.split()[-1].lower()
        function = RULES_MAP.get(last_word)
        if function:
            function(parsed_parameters)
        return True