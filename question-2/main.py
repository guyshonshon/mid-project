import os

def GetFileSize(file_name):
    """
    Return the size of a given file_name
    """
    try:
        return os.path.getsize(file_name)
    except FileNotFoundError:
        print(f'{file_name} does not exist')
    except PermissionError:
        print(f'Permission denied for {file_name}')


if __name__ == '__main__':
    print(GetFileSize('test.txt'))


