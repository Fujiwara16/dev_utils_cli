import argparse
from datetime import datetime


def epoch_to_datetime(epoch):
    try:
        # Convert epoch to datetime
        dt = datetime.fromtimestamp(int(epoch))
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return "Invalid epoch value."


def main():
    parser = argparse.ArgumentParser(description="Convert epoch time to human-readable datetime.")
    parser.add_argument("command", help="Command to run (epochToDatetime)")
    parser.add_argument("epoch", help="Epoch time to convert")
    args = parser.parse_args()

    if args.command == "epochToDatetime":
        print(epoch_to_datetime(args.epoch))
    else:
        print(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()

