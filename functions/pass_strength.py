def pass_strength(password: str) -> int:

    # Check if empty password
    if len(password) == 0 or password.isspace():
        return 0

    points = 0

    # Strings
    symbols = "!\"#$%&\\'()*+,-./:;<=>?@[\\]^_`{|}~"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    higher_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    start = 0
    has_lower = False
    has_higher = False
    has_number = False
    has_symbol = False
    unique_characters = []

    while (points != 35 and start < len(password)):

        letter = password[start]

        if not has_lower and letter in lower_alphabet:
            points += 5
            has_lower = True
        
        if not has_higher and letter in higher_alphabet:
            points += 5
            has_higher = True

        if not has_number and letter in numbers:
            points += 5
            has_number = True

        if not has_symbol and letter in symbols:
            points += 10
            has_symbol = True

        if len(unique_characters) != 5 and letter not in unique_characters:
            unique_characters.append(letter)

            if len(unique_characters) == 5:
                points +=  10
        
        start += 1

    if len(password) >= 13:
        points += 15
    elif len(password) >= 8:
        points += 5

    return points
