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
    parser_jwt_decode.add_argument("--key", help="Key to verify the jwt", required=False)
    parser_jwt_decode.add_argument("--algorithm", help="Algorithm to verify the jwt", required=False)
    args = parser.parse_args()

    if args.command == "epochToDatetime":
        epoch_to_datetime(args.epoch, args.timezone)
    elif args.command == "jwtDecode":
        decode_jwt(args.jwt, args.key, args.algorithm)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
