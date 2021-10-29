import json

companies = {}
count = 0
sum = 0
with open('test_dir/test_text7') as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        companies.update({data[0]: profit})
        if profit > 0:
            count += 1
            sum += profit
average_profit = sum / count
result = [companies, {'average_profit': average_profit}]

with open ('test_dir/result.json', 'w') as file:
    json.dump(result, file)