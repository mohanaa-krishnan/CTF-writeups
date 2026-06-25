import argparse
import string


ALPHABET = string.ascii_lowercase[:16]
OFFSET = ord("a")
LIKELY_FLAG_MARKERS = ("picoctf{", "flag{", "ctf{")


def decode_b16(cipher: str) -> str:
    """
    Decode custom Base16 text back to plaintext.
    Every two alphabet characters represent one original byte.
    """
    if len(cipher) % 2 != 0:
        raise ValueError("Cipher length must be even for b16 decoding.")

    decoded = []

    for i in range(0, len(cipher), 2):
        first = cipher[i]
        second = cipher[i + 1]

        first_index = ALPHABET.index(first)
        second_index = ALPHABET.index(second)

        binary = f"{first_index:04b}" + f"{second_index:04b}"
        decoded.append(chr(int(binary, 2)))

    return "".join(decoded)


def unshift(cipher: str, key: str) -> str:
    """Reverse the Caesar shift used by the challenge."""
    key_index = ord(key) - OFFSET
    result = []

    for ch in cipher:
        ch_index = ord(ch) - OFFSET
        old_index = (ch_index - key_index) % len(ALPHABET)
        result.append(ALPHABET[old_index])

    return "".join(result)


def brute_force(cipher: str) -> list[tuple[str, str]]:
    """Try every possible key and return the decoded results."""
    validate_cipher(cipher)
    results = []

    for key in ALPHABET:
        unshifted = unshift(cipher, key)
        decoded = decode_b16(unshifted)
        results.append((key, decoded))

    return results


def validate_cipher(cipher: str) -> None:
    invalid_chars = sorted(set(cipher) - set(ALPHABET))

    if invalid_chars:
        joined = ", ".join(invalid_chars)
        raise ValueError(f"Cipher contains unsupported characters: {joined}")

    if len(cipher) % 2 != 0:
        raise ValueError("Cipher length must be even.")


def looks_interesting(text: str) -> bool:
    lowered = text.lower()
    has_flag_marker = any(marker in lowered for marker in LIKELY_FLAG_MARKERS)
    has_wrapped_value = "{" in text and "}" in text
    return has_flag_marker or has_wrapped_value


def printable_text(text: str) -> str:
    return text.encode("unicode_escape").decode("ascii")


def print_results(results: list[tuple[str, str]]) -> None:
    print("\n=== Brute Force Results ===\n")

    for key, decoded in results:
        marker = " <-- possible flag" if looks_interesting(decoded) else ""
        print(f"Key {key} -> {printable_text(decoded)}{marker}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Brute force picoCTF-style custom Base16 Caesar ciphers."
    )
    parser.add_argument(
        "cipher",
        nargs="?",
        help="Encrypted text using the custom alphabet abcdefghijklmnop.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cipher = args.cipher or input("Enter encrypted string: ").strip()

    try:
        results = brute_force(cipher)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print_results(results)


if __name__ == "__main__":
    main()
