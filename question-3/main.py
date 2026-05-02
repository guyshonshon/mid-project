def ValidateStringFormat(string):
    """
    A Validator function that guarantees those rules combined:
    - Length must be 9 exactly
    - First 3 characters are uppercased
    - Followed by 4 digits
    - Followed by 2 lowercased characters
    """
    return (
        len(string) == 9 and
        string[:3].isalpha() and string[:3].isupper() and
        string[3:7].isdigit() and
        string[7:9].isalpha() and string[7:9].islower()
    )

if __name__ == '__main__':
    """
    A few test-cases proving the function's validance.
    """
    true_case = 'ABC1234de'
    false_cases = ['Abc1234de',
                   'ABC12s4de',
                   'ABC12334de',
                   '1234',
                   'ABC',
                   'de',
                   'ABC1234De']
    
    assert ValidateStringFormat(true_case), 'Oh no!!!'

    for false_case in false_cases:
        if ValidateStringFormat(false_case):

            print(false_case)
        assert ValidateStringFormat(false_case) == False
    
    print('Shit works')