"""
This Python script demonstrates a simple text encryption and decryption process using prime numbers and random padding.

The encryption process:
1. Selects two prime numbers based on the given day of the month.
2. Multiplies the ASCII value of each character in the input text by the two prime numbers.
3. Converts the resulting product to a zero-padded 10-digit string.
4. Appends the zero-padded day of the month (2 digits) to the encrypted character string.
5. Adds random padding between each digit of the encrypted character string.
6. Stores the 20-character encrypted string for each character in the input text in a list.

The decryption process:
1. Removes the random padding between the digits of the encrypted character string.
2. Extracts the day of the month from the encrypted string (last two characters).
3. Extracts the encrypted character string without the day of the month.
4. Retrieves the prime numbers corresponding to the extracted day of the month.
5. Divides the integer value of the encrypted string by the product of the two prime numbers used for encryption.
6. Converts the result back to the original character.
7. Reconstructs the original text by combining the decrypted characters.

This encryption method is more of an obfuscation technique than a secure encryption method. It should not be used for protecting sensitive data, as it does not provide strong cryptographic security. To improve the security of this encryption method, consider using established cryptographic algorithms such as AES, RSA, or other modern cryptography libraries.
"""

import random


def prime_list():
    primes = [
        131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
        239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
        293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
        359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
        479, 487, 491, 499, 503, 509, 521, 523, 541, 547,
        557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
        613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
        673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
        821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
        881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
        953, 967, 971, 977, 983, 991, 997
    ]
    return primes


def encrypt_char(char, prime1, prime2, secret_key):
    encrypted_value = (ord(char) * prime1 * prime2) ^ secret_key
    return str(encrypted_value).zfill(10)


def add_random_padding(encrypted_char):
    padded_char = ""
    for i in range(len(encrypted_char)):
        padded_char += encrypted_char[i]
        if i < len(encrypted_char) - 1:
            padded_char += str(random.randint(0, 9))
    return padded_char


def encrypt_text(text, day_in_month, secret_key):
    if not isinstance(text, str) or not text:
        raise ValueError("Input text must be a non-empty string.")
    if not isinstance(day_in_month, int) or not (1 <= day_in_month <= 31):
        raise ValueError(
            "Day of the month must be an integer between 1 and 31.")
    if not isinstance(secret_key, int) or len(str(secret_key)) < 30:
        raise ValueError(
            "Secret key must be an integer with at least 30 digits.")

    prime_numbers = prime_list()
    prime1 = prime_numbers[day_in_month - 1]
    prime2 = prime_numbers[-day_in_month]
    encrypted_list = []

    for char in text:
        encrypted_char = encrypt_char(char, prime1, prime2, secret_key)

        # Add the day of the month after the encrypted string
        encrypted_char += str(day_in_month).zfill(2)

        # Add random padding between digits
        encrypted_char = add_random_padding(encrypted_char)

        encrypted_list.append(encrypted_char)

    return encrypted_list


def remove_random_padding(padded_char):
    original_char = ""
    for i in range(0, len(padded_char), 2):
        original_char += padded_char[i]
    return original_char


def decrypt_char(encrypted_char, prime1, prime2, secret_key):
    decrypted_value = (int(encrypted_char) ^ secret_key) // (prime1 * prime2)
    return chr(decrypted_value)


def decrypt_list(encrypted_list, secret_key):
    decrypted_text = ""

    for encrypted_char in encrypted_list:
        # Remove random padding between digits
        encrypted_char = remove_random_padding(encrypted_char)

        # Extract the day of the month from the encrypted string
        day_in_month = int(encrypted_char[-2:])

        # Extract the encrypted character (excluding the day of the month)
        encrypted_char = encrypted_char[:-2]

        # Get the prime numbers corresponding to the day of the month
        prime_numbers = prime_list()
        prime1 = prime_numbers[day_in_month - 1]
        prime2 = prime_numbers[-day_in_month]

        # Decrypt the character
        decrypted_char = decrypt_char(
            encrypted_char, prime1, prime2, secret_key)

        decrypted_text += decrypted_char

    return decrypted_text


text = "Hello, world!"
day_in_month = 18
secret_key = 1111111111111111111111111111111

print("\ninput:\ntext: " + text + ", day in month: " +
      str(day_in_month) + ", secret key: " + str(secret_key))

encrypted_list = encrypt_text(text, day_in_month, secret_key)
print("\nencrypted_list: ")
print(encrypted_list)

print("\ndecrypted_text: ")
decrypted_text = decrypt_list(encrypted_list, secret_key)
print(decrypted_text)
