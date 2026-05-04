import os


def GetSumSize(files):
    """
    Return the sum of files in bytes.

    This function accepts a list of file names, which are iterated
    and searched on current-dir, uses `os.path.getsize()` to grab file's
    size and count towards sum.


    If file exists, add it's size to sum var,
    If file not found, print error
    If permission denied print error
    """
    sum = 0
    for file in files:
        try: 
            sum += os.path.getsize(file)
        except FileNotFoundError:
            print(f'{file} does not exist')
        except PermissionError:
            print(f'Permission denied for {file}')
    return sum


if __name__ == '__main__':
    print(GetSumSize(['test.txt', 'test2.txt', 'test3.txt']))
