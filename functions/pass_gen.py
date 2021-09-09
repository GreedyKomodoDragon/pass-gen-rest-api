import random


def pass_gen(length: int, has_symbols: bool) -> str:
    """
    A function for generating a password

    Args:
        length: int, denotes length of string returned
        has_symbols: bool, determines if symbols are included in the password

    Returns:
        A string of length: {length} with symbols include if {has_symbols}

    Raises:
        ValueError: If length is less than 8.
    """

    if length < 8:
        raise ValueError("Not enough letters for an effective password")

    # Get percentage of attributes
    number_of_numbers = int(length * 0.2)
    number_of_uppercase = int(length * 0.3)

    if has_symbols:
        number_of_symbols = int(length * 0.2)
    else:
        number_of_symbols = 0

    number_of_lowercase = length - number_of_symbols - \
        number_of_numbers - number_of_uppercase

    # List to place all random letters in
    letters = []

    numbers = "0123456789"
    for _ in range(0, number_of_numbers):
        letters.append(random.choice(numbers))

    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(0, number_of_uppercase):
        letters.append(random.choice(uppercase_alphabet))

    symbols = "!\"#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~"
    for _ in range(0, number_of_symbols):
        letters.append(random.choice(symbols))

    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(0, number_of_lowercase):
        letters.append(random.choice(lower_alphabet))

    # Shuffle letters
    random.shuffle(letters)

    return "".join(letters)
