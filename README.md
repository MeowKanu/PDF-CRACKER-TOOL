PDF Cracker Tool

This project is a Python-based tool used to crack the password of a protected PDF file. It can perform a wordlist attack or a brute-force attack, and uses multithreading to speed up password attempts.

Features

Crack password-protected PDF files

Supports wordlist-based password attacks

Supports brute-force password generation

Uses ThreadPoolExecutor for faster parallel password testing

Shows progress using tqdm progress bar

Clean error handling

Project Structure
pdf-cracker-tool/
│── pdf_cracker.py        # Main script
│── wordlist.txt          # Password list (optional)
│── README.md             # Documentation
└── protected.pdf         # Test PDF (optional)

Installation

Install the required Python libraries:

pip install pikepdf tqdm

Usage
1. Wordlist Attack

Use a text file that contains passwords (one per line):

python pdf_cracker.py protected.pdf --wordlist wordlist.txt

2. Brute-Force Attack

Automatically generate passwords using letters and digits:

python pdf_cracker.py protected.pdf --generate --max_length 3

3. Adjust Speed (Threads)

Increase the number of threads for faster cracking:

python pdf_cracker.py protected.pdf --wordlist wordlist.txt --threads 20

Wordlist Format

A wordlist is a simple .txt file where each password is on a new line:

1234
password
mypdf
kanak
test123


Save this as:

wordlist.txt

How It Works

Loads passwords from a wordlist OR generates them using itertools

Tests each password using pikepdf.open()

Uses multithreading to speed up attempts

Displays progress using tqdm

Stops and returns the correct password once found

Requirements

Python 3.8 or higher

pikepdf

tqdm

Notes

Use small wordlists for testing

Create protected PDFs using a PDF protection tool

Brute-force is slow for long passwords

Thread count can be adjusted based on system performance

License

This project is licensed under the MIT License.
