import requests
import re


def get_dom_names(text):
    res = set()
    pattern = r'<a.* href=["\']\w*://?(\w[\w\.-]*)'

    for key in re.findall(pattern, str(text)):
        res.add(key)
    return res


link = input()
text = requests.get(link).text
res = sorted(list(get_dom_names(text)))

print(*res, sep='\n')
