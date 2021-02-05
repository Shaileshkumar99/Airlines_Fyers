import json

data = {}
data['info'] = []
data['info'].append({
    'name': 'anuj',
    'course': 'btech',
    'branch': 'IT'
})
data['info'].append({
    'name': 'ayush',
    'course': 'btech4',
    'branch': 'ME'
})
data['info'].append({
    'name': 'shailesh',
    'course': 'btech2',
    'branch': 'CS'
})
with open('new2.json', 'w') as file:
    json.dump(data, file)

with open('new2.json') as file:
    data = json.load(file)
    for p in data['info']:
        print('Name ' + p['name'])
        print('course ' + p['course'])
        print('branch ' + p['branch'])
