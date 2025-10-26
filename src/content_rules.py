class ContentRules:
    @classmethod
    def parse_ate(cls, activity_parameters) -> bool:
        print(activity_parameters)

    @classmethod
    def parse_project(cls, activity_parameters: str) -> bool:
        print(activity_parameters)

RULES_MAP = {
    "eat" : ContentRules.parse_ate,
    "project" : ContentRules.parse_project,
}