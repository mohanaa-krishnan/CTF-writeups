# B16 Caesar Brute Forcer

A simple Python tool for solving picoCTF-style cryptography challenges involving:

- Custom Base16 encoding
- Caesar cipher shifting
- Small keyspace brute force

## Features

- Supports the custom alphabet `abcdefghijklmnop`
- Brute forces all 16 possible keys
- Decodes encrypted strings automatically
- Highlights output that looks like a possible flag
- Works with an argument or interactive input

## Usage

Run with an argument:

```bash
python solver.py fegdeogdgecoeocgcgchcfcffccfca
```

Or run interactively:

```bash
python solver.py
```

Then paste the encrypted string when prompted.

## Example

```text
=== Brute Force Results ===

Key a -> random_output
Key b -> random_output
...
Key p -> et_tu?_77866c61
```

## How It Works

The challenge uses a custom Base16 alphabet containing only the letters `a` through `p`.
Each pair of characters represents one byte. Before decoding, the text is Caesar-shifted
inside that 16-character alphabet.

This tool reverses the Caesar shift for every possible key, decodes each result from the
custom Base16 format, and prints all candidate plaintexts.

## Future Improvements

- Save results to a file
- Add stronger automatic flag detection
- Support other custom alphabets
- Add tests with known challenge samples
