from utils.formatter import TerminalFormatter
import json
import csv


def csv_formatter(file_path, grid):
    data = []
    formatter = TerminalFormatter()
    formatter.print_title()
    with open(file_path, newline="") as csvfile:
        if grid:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)  # Extract headers
            data = [row for row in csv_reader]
            # Format data as a table
            formatter.format_table(data, headers)
        else:
            reader = csv.DictReader(csvfile)
            # Read the CSV for grid view
            for row in reader:
                data.append(row)
            print(json.dumps(data, indent=4))
