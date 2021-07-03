def backward_string_by_word(text: str) -> str:
    accumulator = ''
    result_array = ['']
    for char in text:
        if char != ' ':
            # If not a space
            accumulator += char
        else: # Cant find end of the string !
            if accumulator:
                # if word in accumulator and next is space
                result_array.append(accumulator[::-1] + ' ')
                accumulator = ''
            else:
                result_array.append(char)

    if accumulator: result_array.append(accumulator[::-1] )

    print(f'Answer : ', ''.join(result_array))
    return ''.join(result_array)
    


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
