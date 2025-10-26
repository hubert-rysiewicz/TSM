class ContentRules:
    @classmethod
    def parse_ate(cls, activity_parameters) -> bool:

    @classmethod
    def parse_project(cls, activity_parameters: str) -> bool:

RULES_MAP = {
    "ate" : ContentRules.parse_ate,
    "project" : ContentRules.parse_project,
}