from tabulate import tabulate
from pyfiglet import figlet_format
import json


class TerminalFormatter:
    def __init__(self, title=None):
        self.title = title

    def print_title(self):
        # print author Name Fujiwara
        print(figlet_format("Fujiwara's utils"))
        # Print the title in ASCII art
        if self.title:
            print(figlet_format(self.title, font="slant"))

    def format_table(self, data, headers=None, tablefmt="grid"):
        # Format data as a table
        if headers:
            table = [headers] + data
        else:
            table = data
        print(tabulate(table, tablefmt=tablefmt))

    def format_json(self, data, grid=True):
        # Format data as pretty-printed JSON
        if grid:
            table = []
            for key, value in data.items():
                table.append([key, value])
            self.format_table(table)
        else:
            print(json.dumps(data, indent=4))

    def format_text(self, text):
        # Print plain text
        print(text)
