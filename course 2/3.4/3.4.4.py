import json

# json_str = input()
json_str = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
json_str = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'

classes = {x['name']: x['parents'] for x in json.loads(json_str)}


def search(name):
    nodes = [name]
    for parent in classes[name]:
        new_nodes = search(parent)
        for new_node in new_nodes:
            if new_node not in nodes:
                nodes.append(new_node)
    return nodes


keys = sorted(classes.keys())
result = dict()
for key in keys:
    result[key] = search(key)

result2 = dict()
for key in keys:
    for ch in result.values():
        result2[key] = result2.get(key, 0) + ch.count(key)

for key in keys:
    print(key, result2[key])


