# A8-String methods - file path analyzer
path = input("Enter file path: ")
is_valid_windows_path = False
is_valid_linux_path = False
# check if it's a valid windows path
if len(path) >= 6 and \
        path[0].isalpha() and \
        path[0].isupper() and \
        path[1:3] == ':\\' and \
        path[-1] != '.' and \
        path.find('/') == -1 and \
        path.find(':') == 1 and \
        path.find('*') == -1 and \
        path.find('?') == -1 and \
        path.find('"') == -1 and \
        path.find('<') == -1 and \
        path.find('>') == -1 and \
        path.find('|') == -1 and \
        path.find('\\\\') == -1 and \
        path.find('.\\') == -1 and \
        path.find('\\.') == -1 and \
        path.find('.') > 0 and \
        path[::-1].find('.') < path[::-1].find('\\'):
    is_valid_windows_path = True
else:
    # check if it's a valid linux path
    if path[0] == '/' and \
            path[-1] != '.' and \
            path.find('\\') == -1 and \
            path.find(':') == -1 and \
            path.find('*') == -1 and \
            path.find('?') == -1 and \
            path.find('"') == -1 and \
            path.find('<') == -1 and \
            path.find('>') == -1 and \
            path.find('|') == -1 and \
            path.find('//') == -1 and \
            path.find('./') == -1 and \
            path.find('/.') == -1 and \
            path.find('.') > 0 and \
            path[::-1].find('.') < path[::-1].find('/'):
        is_valid_linux_path = True

is_valid_path = is_valid_linux_path or is_valid_windows_path
if is_valid_path:
    if is_valid_windows_path:
        num_of_slashes = len(path) - len(''.join(path.split('\\')))
        last_slash_index = path[::-1].find('\\')
        last_period_index = path[::-1].find('.')
        file_name = path[::-1][last_slash_index - 1:last_period_index:-1]
        file_extension = path[::-1][last_period_index::-1]

    else:
        num_of_slashes = len(path) - len(''.join(path.split('/')))
        last_slash_index = path[::-1].find('/')
        last_period_index = path[::-1].find('.')
        file_name = path[::-1][last_slash_index - 1:last_period_index:-1]
        file_extension = path[::-1][last_period_index::-1]

    print("The path is valid")
    print(f"The path depth: {num_of_slashes - 1}")
    print(f"File name: {file_name}")
    print(f"File extension: {file_extension}")
else:
    print("The path is invalid")
