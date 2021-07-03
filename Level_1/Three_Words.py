def check_counter(word):
    counter = 0
    def add_and_check(): # Better to pass argument word
        nonlocal counter
        counter += 1 if word.isalpha() else 0
        return counter
    return True if counter == 3 else False

def checkio(words: str) -> bool:
    for word in words.split():
        if not check_counter(word): continue 
        else: return True
    return False    
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")