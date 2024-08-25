import jwt

from utils.formatter import TerminalFormatter


def decode_jwt(token, key=None, algorithm=None):
    try:
        formatter = TerminalFormatter()

        if key:
            if not algorithm:
                algorithm = "HS256"
            # Decode the JWT and verify the signature
            decoded_payload = jwt.decode(token, key=key, algorithms=[algorithm])
        else:
            # Decode the JWT without verifying the signature
            decoded_payload = jwt.decode(token, options={"verify_signature": False})

        # Extract header, payload, and signature
        header = jwt.get_unverified_header(token)
        payload = decoded_payload
        # The signature is part of the original token, after the second '.'
        signature = token.split('.')[2] if '.' in token else None

        # format header and paload in this format - [['key', 'value'], ['key', 'value'], ...]
        formatted_header = []
        for key, value in header.items():
            formatted_header.append([key, value])
        formatted_payload = []
        for key, value in payload.items():
            formatted_payload.append([key, value])

        # Print formatted output
        formatter.print_title()
        formatter.format_text("\nHeader:")
        formatter.format_table(formatted_header)

        formatter.format_text("\nPayload:")
        formatter.format_table(formatted_payload)

        formatter.format_text("\nSignature:")
        formatter.format_table([["Signature", signature]])
    except jwt.DecodeError as e:
        print(f"Failed to decode JWT: {e}")
