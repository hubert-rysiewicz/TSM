# Data Standardisation
This folder contains the text format of the data file(s).
For the data to be easily read by the system, it must be in the right format depending on the case.
The system looks at the last word of the line of data and decides whether extra information needs to be added.
Therefore, here is the format for the currently allowed use cases (you can add your own in src/parse_cases.py):
- Food (last word "ate"), format: calories (kcal), protein (g), price(£)
- Projects (last word "project"), format: project name

By the way, it checks if information is added by looking for brackets, extra information doesn't need to be added.