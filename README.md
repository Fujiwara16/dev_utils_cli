
# Dev Utils CLI

`Dev Utils CLI` is a Python package that provides a set of common utilities for developers, including converting epoch time to datetime and decoding JWT tokens. This CLI tool is designed to be flexible and easy to use, making it a handy addition to your developer toolkit.

## Features

- **Epoch to Datetime Conversion**: Convert epoch time to a human-readable datetime, with optional timezone support.
- **JWT Decode**: Decode and optionally verify a JWT using a provided key and algorithm.

## Installation

You can install the package directly from the GitHub repository using `pip`:

```bash
pip install git+https://github.com/Fujiwara16/dev_utils_cli.git
```

This command will install the package and make the `dev_utils_cli` commands available globally.

## Usage

### General Command Structure

After installation, you can use the CLI tool via the `dev_utils_cli` command:

```bash
dev_utils_cli [command] [arguments]
```

### Command: `epochToDatetime`

Convert epoch time to a human-readable datetime.

**Usage:**

```bash
dev_utils_cli epochToDatetime [epoch] [--timezone <timezone>]
```

**Example:**

```bash
dev_utils_cli epochToDatetime 1609459200 --timezone "UTC"
```

This will output:

```
2021-01-01 00:00:00
```

### Command: `jwtDecode`

Decode a JWT and optionally verify it using a key and algorithm.

**Usage:**

```bash
dev_utils_cli jwtDecode [jwt] [--key <key>] [--algorithm <algorithm>]
```

**Example:**

```bash
dev_utils_cli jwtDecode eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... --key "your_256_bit_key" --algorithm HS256
```

This will decode the JWT and print out the header, payload, and signature.

## Example Outputs

### Epoch to Datetime

```bash
dev_utils_cli epochToDatetime 1609459200
```

Output:

```
2021-01-01 00:00:00
```

### JWT Decode

```bash
dev_utils_cli jwtDecode eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Output:

```
Header:
+--------+------------+
| Field  | Value      |
+--------+------------+
| alg    | HS256      |
| typ    | JWT        |
+--------+------------+

Payload:
+--------+------------+
| Claim  | Value      |
+--------+------------+
| sub    | 1234567890 |
| name   | John Doe   |
+--------+------------+

Signature:
+----------+--------------------------------------------------+
| Signature| SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c     |
+----------+--------------------------------------------------+
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features.

## License

This project is licensed under the MIT License.
