def check_count():
    counter = 0

    def add_one(word):
        nonlocal counter
        if word.isalpha():
            counter += 1
        else:
            counter = 0
        if counter == 3:
            counter = -1
        return counter
    return add_one


def checkio(words: str) -> bool:
    for word in words.split():
        get_counter = check_count()
        answer = get_counter(word)
        if answer == -1:
            return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
