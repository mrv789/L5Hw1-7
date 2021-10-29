with open('test_dir/test_text5') as file:
    num_file = file.read().split()
    sum = 0
    for num in  num_file:
        sum += int(num)

print(sum)