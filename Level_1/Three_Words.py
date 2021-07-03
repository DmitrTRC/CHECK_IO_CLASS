def check_counter() -> bool:
    counter = 0

    def count_word(word):  # Better to pass argument word
        nonlocal counter
        if word.isalpha():
            counter += 1
        else:
            counter = 0
        if counter == 3:
            counter = -1

        return counter
    return count_word


def checkio(words: str) -> bool:
    get_cur_count = check_counter()
    for word in words.split():
        cur_count = get_cur_count(word)
        print ( f'Checking word : {word} with {cur_count=}')

        if cur_count == -1:
            return True
        else:
            continue

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, 'Result is : ' + \
        str(checkio("Hello World hello"))
    assert checkio("He is 123 man") == False, 'Result is : ' + \
        str(checkio("He is 123 man"))
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
