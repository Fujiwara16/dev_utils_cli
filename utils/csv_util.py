from utils.formatter import TerminalFormatter
import json
import csv


def csv_formatter(file_path, grid):
    data = []
    formatter = TerminalFormatter()
    formatter.print_title()
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
        if grid:
            formatter.format_table(data)
        else:
            print(json.dumps(data, indent=4))
