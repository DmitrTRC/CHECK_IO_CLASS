'''
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.
'''


class Marker:
    def __init__(self, symbol: str, position: int = 0):
        self._position = position
        self.symbol = symbol

    def seek(self, source: str):
        self.position = source.find(self.symbol)

    def set(self, value):
        self.position = value


class Boundary:
    def __init__(self, text: str, begin: str, end: str):

        assert begin != end, f'Begin must be different from end'
        self._source = text
        self._end_position = text.__len__()
        self.initial_marker = Marker(begin).seek(self._source)
        self.final_marker = Marker(end).seek(self._source)

    def _logic_check(self):
        if not self.initial_marker:
            self.initial_marker.set(0)

        if not self.final_marker:
            self.final_marker.set(self._end_position)
        
        if self.initial_marker > self.final_marker:
            self.initial_marker.set(0)
            self.final_marker.set(0)


        

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    return text[text.index(begin)+1:text.index(end)]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers(
        'No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
