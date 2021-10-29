dic_tr = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре",
}

with open('test_dir/test_text4') as file:
    file_new = file.readlines()
    print(file_new)

with open('test_dir/test_text4new.txt', 'w') as file:
    for line in file_new:
        info = line.split()
        dic_rus = dic_tr.get(info[0])
        file.write(f'{line.replace(info[0], dic_rus)}')

