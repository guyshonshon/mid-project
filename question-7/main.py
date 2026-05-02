def get_normalized_file_name(file_name):
    """
    Return the normalized file-path for a given file-name
    """
    return f'./{file_name}'


def WriteReverse(input_file, output_file):
    """
    Open input and output file with corresponding modes,
    Then read input's content, reverse it and write to output.
    """
    normalized_input_name = get_normalized_file_name(input_file)
    normalized_output_name = get_normalized_file_name(output_file)

    try:
        with open(normalized_input_name, 'r') as input, open(normalized_output_name, 'w') as output:
            output.write(input.read().strip()[::-1])
    except FileNotFoundError:
        print(f'{input_file} does not exist')
    except PermissionError:
        print(f'Permission denied for {normalized_input_name} or {normalized_output_name}')


if __name__ == '__main__':
    WriteReverse('input.txt', 'output.txt')


