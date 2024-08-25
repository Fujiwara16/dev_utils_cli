import base64

from utils.formatter import TerminalFormatter


def encode_base64(string: str):
    try:
        str = base64.b64encode(string.encode("utf-8")).decode("utf-8")
        formatter = TerminalFormatter()
        formatter.print_title()
        formatter.format_table([["Encoded string", str]])
    except Exception as e:
        print(f"Error: {e}, check the input string.")


def decode_base64(string: str):
    try:
        str = base64.b64decode(string).decode("utf-8")
        formatter = TerminalFormatter()
        formatter.print_title()
        formatter.format_table([["Decoded string", str]])
    except Exception as e:
        print(f"Error: {e}, check the input string.")
