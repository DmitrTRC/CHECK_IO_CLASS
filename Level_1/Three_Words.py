def check_counter(word) -> bool:
    counter = 0

    def count_word():  # Better to pass argument word
        nonlocal counter
        print(f'Counter before : {counter}')
        if word.isalpha():
            counter += 1
        elif counter == 3:
            counter = -1
        else:
            counter = 0
        print(f'Counter after : {counter}')

        return counter
    return count_word


def checkio(words: str) -> bool:
    for word in words.split():
        if check_counter(word) == -1:
            return True
        else:
            continue

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, 'Result is : ' + \
        str(checkio("He is 123 man"))
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
