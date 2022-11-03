def print_upper_words(words):
    """Print each word uppercase"""

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print words uppercase, that start with 'E'"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word on sepseperate line, uppercased, if starts with one of given letter"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break