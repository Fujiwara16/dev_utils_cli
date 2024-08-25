import argparse

from utils.epoch_utils import curr_time, date_time_to_epoch, epoch_to_datetime
from utils.jwt_decode import decode_jwt


def main():
    parser = argparse.ArgumentParser(description="A CLI tool for common developer utils")
    subparsers = parser.add_subparsers(dest="command")

    # Command: epochToDatetime
    parser_epoch = subparsers.add_parser("epochToDatetime", help="Convert epoch time to datetime.")
    parser_epoch.add_argument("epoch", help="Epoch time to convert.")
    parser_epoch.add_argument("--timezone", help="Timezone (optional).", required=False)

    # Command: jsonToYaml
    parser_jwt_decode = subparsers.add_parser("jwtDecode", help="Decode the given jwt")
    parser_jwt_decode.add_argument("jwt", help="jwt to decode")
    parser_jwt_decode.add_argument("--key", help="Key to verify the jwt", required=False)
    parser_jwt_decode.add_argument("--algorithm", help="Algorithm to verify the jwt", required=False)

    # Command: currentEpoch
    parser_curr_epoch = subparsers.add_parser("currentTime", help="Get current time. The output will be the epoch and datetime, you can also pass the timezone.")
    parser_curr_epoch.add_argument("--timezone", help="Timezone (optional).", required=False)

    # Command dateToEpoch
    parser_date = subparsers.add_parser("dateToEpoch", help="Convert datetime to epoch. Pass the datetime and timezone (optional).")
    parser_date.add_argument("datetime", help="Datetime to convert in format (YYYY-MM-DD HH:MM:SS).")
    parser_date.add_argument("--timezone", help="Timezone (optional).", required=False)
    args = parser.parse_args()

    if args.command == "epochToDatetime":
        epoch_to_datetime(args.epoch, args.timezone)
    elif args.command == "jwtDecode":
        decode_jwt(args.jwt, args.key, args.algorithm)
    elif args.command == "currentTime":
        curr_time(args.timezone)
    elif args.command == "dateToEpoch":
        date_time_to_epoch(args.datetime, args.timezone)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
