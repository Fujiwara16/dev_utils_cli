import jwt


def decode_jwt(token):
    try:
        # Decode the token without verifying the signature
        decoded_payload = jwt.decode(token, options={"verify_signature": False})
        return decoded_payload
    except jwt.DecodeError as e:
        return f"Failed to decode JWT: {e}"
