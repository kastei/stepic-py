import requests
import re

url_in = input()
url_out = input()

def get_urls(url):
    res = requests.get(url)
    if res.status_code == 200:
        pattern = '<a href="(.*?.html)">'
        return re.findall(pattern, str(res.text))
    else:
        return []


def we_can(url1, url2):
    for i in get_urls(url1):
        if url2 in get_urls(i):
            return True
    return False


if we_can(url_in, url_out):
    print("Yes")
else:
    print("No")
