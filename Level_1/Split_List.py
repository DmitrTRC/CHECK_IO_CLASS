import math


def split_list(items: list) -> list:
    if items.__len__() == 0: return [[],[]]
    elif items.__len__() == 1: return [[items[0]], []]

    return  [
        items[i : i + math.ceil(items.__len__() / 2)]
        for i in range(0, items.__len__(), math.ceil(items.__len__() / 2))
    ]
    
   


if __name__ == "__main__":
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))
    print ('Example 2: ')
    print (split_list([1]))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []] 
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
