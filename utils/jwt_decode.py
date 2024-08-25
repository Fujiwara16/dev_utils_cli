import jwt


def decode_jwt(token, key, algorithm):
    try:
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

        return {
            "header": header,
            "payload": payload,
            "signature": signature,
        }
    except jwt.DecodeError as e:
        return f"Failed to decode JWT: {e}"
