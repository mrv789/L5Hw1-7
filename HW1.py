with open('test_dir/test_text1.txt', 'w') as file:
    line = input('Введите ваш текст: \n')
    line2 = '\n'
    while line:
        file.write(line + line2)
        line = input('Введите ваш текст: \n')
        if not line:
            break
