PATTERN = "1234"


def get_pattern_occurrences_with_slicing(content, pattern):
    """
    The pythonic way of finding occurrences of a pattern in content.
    We iterate through content's with indexing, and check for each index
    if the next sequence of {pattern_len} equals to pattern, for instance:
    content = "123abc1234def"
    pattern = "1234"
    pattern_len = len(pattern) # 4
    so, for each char in content, we take slice a sequence of index + pattern_len and if it
    is equal to pattern then we record that index in the occurrences list.

    index = 6
    slice = content[index:index+pattern_len] # equals to content[6:10]
    slice = "1234"
    pattern = "1234"
    assert slice == pattern
    occurences.append(index)

    """
    index = 0
    pattern_len = len(pattern)
    occurrences = []
    for index in range(len(content)):
        if content[index] == pattern[0]:
            if content[index:index+pattern_len] == pattern:
                 occurrences.append(index)
    return occurrences


def get_pattern_occurrences_with_indexing_nested_loop(content, pattern):
    """
    This function provides a hardcoded pattern occurences search,
    We grab the lengths of pattern and content, then we loop through content's length
    and capture "start_index" which is used for occurrences list, then, for each character
    we start a nested loop of pattern matching, we safely ensure that we can not escape content's
    length, and check if the char at content_index equals the pattern's index. for instance:

    content = 123abc1234def
    pattern = 1234

    On each iteration, we would take the first char of the pattern ('1') and match it against
    the current index of content, then continue comparing among the rest of the pattern's indexes,
    incase both sides match, we have a match that is captured and added to the list,
    otherwise, matching fails and we continue onto the next char in the content string, performing
    the same iteration again.
    """
    pattern_len = len(pattern)
    content_len = len(content)
    occurrences = []
    for start_index in range(content_len):
        matched = True
        for pattern_index in range(pattern_len):
            content_index = start_index + pattern_index

            # Prevent going past the end of content
            if content_index >= content_len:
                matched = False
                break

            if content[content_index] != pattern[pattern_index]:
                matched = False
                break

        if matched:
            occurrences.append(start_index)
    return occurrences


def FindPatternWithoutBuiltins(file_name):
    """
    Open input and output file with corresponding modes,
    Then read input's content, reverse it and write to output.
    """
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            occurrences = get_pattern_occurrences_with_slicing(content, PATTERN)
            hardcoded_occurrences = get_pattern_occurrences_with_indexing_nested_loop(content, PATTERN)

            assert occurrences == hardcoded_occurrences, "Algo sucks"

            print(occurrences)
            print(hardcoded_occurrences)

    except FileNotFoundError:
        print(f'{file_name} does not exist')
    except PermissionError:
        print(f'Permission denied for {file_name}')


if __name__ == '__main__':
    FindPatternWithoutBuiltins('test.txt')


