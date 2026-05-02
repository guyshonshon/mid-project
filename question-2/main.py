import os

def get_normalized_file_name(file_name):
    """
    Return the normalized file-path for a given file-name
    """
    return f'./{file_name}'


def GetFileSize(file_name):
    """
    Return the size of a given file_name
    """
    normalized_file_name = get_normalized_file_name(file_name)
    try:
        if os.path.exists(normalized_file_name):
            return os.path.getsize(normalized_file_name)
    except FileNotFoundError:
        print(f'{normalized_file_name} does not exist')
    except PermissionError:
        print(f'Permission denied for {normalized_file_name}')


if __name__ == '__main__':
    print(GetFileSize('test.txt'))


