#https://stepik.org/lesson/3380/step/5?unit=963

data = dict()
for i in range(12):
    data[str(i+1)] = []

input_file = 'dataset_3380_5.txt'
with open(input_file) as f:
    for line in f:
        class_num, name, height = line.split('\t')
        data[class_num].append(int(height))

for i in range(11):
    key = str(i+1)
    if len(data[key]) == 0:
        print(f'{key} -')
    else:
        print(f'{key} ' + str(round(sum(data[key])/len(data[key]), 5)))


