subj = {}
with open('test_dir/test_text6') as file:
    file_lines = file.readlines()
    for line in file_lines:
        info = line.split()
        hours = 0
        for elem in info[1:]:
            if elem != '-':
                num = '0'
                for i in elem:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hours += int (num)
        subj.update({info[0].strip(':'): hours})
    print(subj)