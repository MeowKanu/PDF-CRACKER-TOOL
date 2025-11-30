import pikepdf
import itertools
import string
import argparse
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm


# Load passwords from a wordlist file
def load_passwords(wordlist_file):
    with open(wordlist_file, "r") as file:
        for line in file:
            yield line.strip()


# Generate passwords using itertools (brute-force)
def generate_passwords(charset, max_length):
    for length in range(1, max_length + 1):
        for combo in itertools.product(charset, repeat=length):
            yield ''.join(combo)


# Try a single password
def try_password(pdf_file, password):
    try:
        with pikepdf.open(pdf_file, password=password):
            return password   # SUCCESS
    except pikepdf._core.PasswordError:
        return None          # WRONG PASSWORD
    except Exception as e:
        return None          # Other errors ignored


# Decrypt using threads
def decrypt_pdf(pdf_file, passwords, threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []

        for password in passwords:
            futures.append(executor.submit(try_password, pdf_file, password))

        for future in tqdm(futures, desc="Cracking", unit="password"):
            result = future.result()
            if result is not None:
                return result  # Found correct password

    return None  # Nothing worked


# Main function
def main():
    parser = argparse.ArgumentParser(description="PDF Password Cracker Tool")

    parser.add_argument("pdf_file", help="Protected PDF file path")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--wordlist", help="Path to wordlist file")
    group.add_argument("--generate", action="store_true",
                       help="Use brute-force password generation")

    parser.add_argument("--max_length", type=int, default=3,
                        help="Max length for brute-force (default: 3)")
    parser.add_argument("--threads", type=int, default=10,
                        help="Number of threads (default: 10)")

    args = parser.parse_args()

    if args.wordlist:
        passwords = load_passwords(args.wordlist)

    elif args.generate:
        charset = string.ascii_lowercase + string.digits
        passwords = generate_passwords(charset, args.max_length)

    print("Starting PDF password cracking...")

    found = decrypt_pdf(args.pdf_file, passwords, args.threads)

    if found:
        print(f"\nSUCCESS! Password found: {found}")
    else:
        print("\nFAILED: Password not found.")


if __name__ == "__main__":
    main()
