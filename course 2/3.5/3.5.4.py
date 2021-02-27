import requests
import json


def token():
    with open('secr') as data:
        client_id = data.readline().strip()
        client_secret = data.readline().strip()

    # инициируем запрос на получение токена
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

    # разбираем ответ сервера
    j = json.loads(r.text)

    # достаем токен
    return j["token"]

def info(token, id):
    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token": token}
    # инициируем запрос с заголовком
    r = requests.get("https://api.artsy.net/api/artists/"+id, headers=headers)
    # разбираем ответ сервера
    j = json.loads(r.text)
    return j['birthday'] + ';' + j['sortable_name']


token = token()

result = []

with open('data.txt') as data:
    for line in data:
        result.append(info(token, line.strip()))

result.sort()

for x in result:
    print(x.split(';')[1])
