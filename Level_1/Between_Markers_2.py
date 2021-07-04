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

    def position(self): return self._position

    def seek(self, source: str):
        self._position = source.find(self.symbol)

    def set(self, value):
        self._position = value

    def __eq__(self, other):
        return self._position == other._position

    def __gt__(self, other):
        return self._position > other._position


class Boundary:
    def __init__(self, text: str, begin: str, end: str):

        assert begin != end, f'Begin must be different from end'
        self._source = text
        self._end_position = text.__len__()
        self.initial_marker = Marker(begin)
        self.initial_marker.seek(self._source)
        if self.initial_marker.position() != -1 :
            self.initial_marker.set(self.initial_marker.position() + begin.__len__())

        self.final_marker = Marker(end)
        self.final_marker.seek(self._source)

    def _logic_check(self):
        if self.initial_marker.position() == -1:
            self.initial_marker.set(0)

        if self.final_marker.position() == -1:
            self.final_marker.set(self._end_position)

        if self.initial_marker > self.final_marker:
            self.initial_marker.set(0)
            self.final_marker.set(0)

    def run(self) -> str:
        self._logic_check()
        return self._source[self.initial_marker.position():self.final_marker.position()]


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """

    boundary = Boundary(text, begin, end)
    return boundary.run()


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers(
        'What is >apple<', '>', '<') == "apple", f" Got : { between_markers('What is >apple<', '>', '<')}"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site",  between_markers("<head><title>My new site</title></head>",
                                                                                     "<title>", "</title>")
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers(
        'No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
