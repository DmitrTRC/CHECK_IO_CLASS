def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    delimiters = (' ', ',', '.')
    result_str = ''
    index = 0
    result_str = ''.join( char if char.isalpha() else ' ' for char in text ).split()[0]
    # while index < (text.__len__() - 1):
    #     if text[index] in delimiters:
    #         index += 1
    #         continue
    #     while text[index] not in delimiters:
    #         result_str += text[index]
    #         index += 1
    #     else:
    #         return result_str

    return result_str


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
