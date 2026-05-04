def WriteReverse(input_file, output_file):
    """
    Open input and output file with corresponding modes,
    Then read input's content, reverse it and write to output.
    """
    try:
        with open(input_file, 'r') as input, open(output_file, 'w') as output:
            output.write(input.read().strip()[::-1])
    except FileNotFoundError:
        print(f'{input_file} does not exist')
    except PermissionError:
        print(f'Permission denied for {input_file} or {output_file}')


if __name__ == '__main__':
    WriteReverse('input.txt', 'output.txt')


