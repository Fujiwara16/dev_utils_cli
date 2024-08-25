import argparse

from utils.base64_util import encode_base64, decode_base64
from utils.epoch_utils import curr_time, date_time_to_epoch, epoch_to_datetime
from utils.formatter import TerminalFormatter
from utils.jwt_decode import decode_jwt


def main():
    parser = argparse.ArgumentParser(description="A CLI tool for common developer utils")
    subparsers = parser.add_subparsers(dest="command")

    # Command: epochToDatetime
    parser_epoch = subparsers.add_parser("epochToDatetime", help="Convert epoch time to datetime.")
    parser_epoch.add_argument("epoch", help="Epoch time to convert.")
    parser_epoch.add_argument("--timezone", help="Timezone (optional).", required=False)

    # Command: jwtDecode
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

    # Command base64Encode
    parser_base64_ec = subparsers.add_parser("base64Encode", help="Encode the given string to base64.")
    parser_base64_ec.add_argument("string", help="String to encode.")

    # Command base64Decode
    parser_base64_dc = subparsers.add_parser("base64Decode", help="Decode the given base64 string.")
    parser_base64_dc.add_argument("string", help="String to decode.")

    # Command jsonFormat
    parser_json = subparsers.add_parser("jsonFormat", help="Format the given JSON string.")
    parser_json.add_argument("string", help="JSON string to format.")
    parser_json.add_argument("--grid", help="Enable grid view.", required=False)

    args = parser.parse_args()

    if args.command == "epochToDatetime":
        epoch_to_datetime(args.epoch, args.timezone)
    elif args.command == "jwtDecode":
        decode_jwt(args.jwt, args.key, args.algorithm)
    elif args.command == "currentTime":
        curr_time(args.timezone)
    elif args.command == "dateToEpoch":
        date_time_to_epoch(args.datetime, args.timezone)
    elif args.command == "base64Encode":
        encode_base64(args.string)
    elif args.command == "base64Decode":
        decode_base64(args.string)
    elif args.command == "jsonFormat":
        formatter = TerminalFormatter()
        formatter.format_json_string(args.string, args.grid)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
