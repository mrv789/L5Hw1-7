with open('test_dir/test_text3', 'r') as file:
    file_new = file.readlines()
    workers = {}
    total_sum = 0
    for line in file_new:
        info_w = line.split()
        workers.update({info_w[0]: float(info_w[1])})
        total_sum += float(info_w[1])
aver_sum = total_sum / len(workers)
print(f'средняя зарплата = {aver_sum}')

for a, b in workers.items():
    if b < 20000:
        print(f'{a}: {b}')