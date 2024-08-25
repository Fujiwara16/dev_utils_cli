import argparse

from utils.epoch_utils import epoch_to_datetime
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
    args = parser.parse_args()

    if args.command == "epochToDatetime":
        result = epoch_to_datetime(args.epoch, args.timezone)
        print(result)
    elif args.command == "jwtDecode":
        result = decode_jwt(args.jwt)
        print(result)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
