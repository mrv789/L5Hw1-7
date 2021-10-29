with open('test_dir/test_text2') as file:
    file_lines = file.readlines()
    # print(file_lines)
    str_count = 0
    for num, line in enumerate(file_lines):
        str_count += 1
        words_count = len(line.split())
        print(f'{num + 1} - {words_count}')
    print(str_count)
