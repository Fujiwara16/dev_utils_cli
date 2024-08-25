
# Dev Utils CLI

`Dev Utils CLI` is a Python package that provides a set of common utilities for developers, including converting epoch time to datetime and decoding JWT tokens. This CLI tool is designed to be flexible and easy to use, making it a handy addition to your developer toolkit.

## Features

- **Epoch to Datetime Conversion**: Convert epoch time to a human-readable datetime, with optional timezone support.
- **JWT Decode**: Decode and optionally verify a JWT using a provided key and algorithm.
- **Current Time**: Get the current time in both epoch and human-readable datetime format, with optional timezone support.
- **Datetime to Epoch Conversion**: Convert a datetime string to epoch time, with optional timezone support.

## Installation

You can install the package directly from the GitHub repository using `pip`:

```bash
pip install git+https://github.com/Fujiwara16/dev_utils_cli.git
```

This command will install the package and make the `dev_util` commands available globally.

## Usage

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

### Command: `currentTime`

Get the current time in both epoch and human-readable datetime format.

**Usage:**

```bash
dev_utils_cli currentTime [--timezone <timezone>]
```

**Example:**

```bash
dev_utils_cli currentTime --timezone "Asia/Kolkata"
```

This will output something like:

```
Current Epoch: 1627489200
Current Datetime: 2024-08-25 10:00:00
```

### Command: `dateToEpoch`

Convert a datetime string to epoch time.

**Usage:**

```bash
dev_utils_cli dateToEpoch [datetime] [--timezone <timezone>]
```

**Example:**

```bash
dev_utils_cli dateToEpoch "2024-08-25 10:00:00" --timezone "Asia/Kolkata"
```

This will output:

```
Epoch: 1627489200
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


## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features.

## License

This project is licensed under the MIT License.
