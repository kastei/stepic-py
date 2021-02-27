import requests

api_url = 'http://numbersapi.com/'
params = {
    'json': True,
    'default': 'Boring'
}

def read_numbers(file_name):
    with open(file_name) as f:
        lines = f.readlines()
        print(lines)
        return list(map(lambda x: x.strip(), lines))


file = 'dataset_24476_3.txt'

numbers = read_numbers(file)

print(numbers)
url = api_url + ",".join(numbers) + "/math"

res = requests.get(url, params=params).json()
print(res)
for num in numbers:
    if res[num] == 'Boring':
        print('Boring')
    else:
        print('Interesting')