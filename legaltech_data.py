import os, json

path_to_json = 'C:/Users/rookie/Downloads/民事判決/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

result = []
for index, js in enumerate(json_files):
    f = {}
    with open(os.path.join(path_to_json, js), encoding='utf-8') as json_file:
        json_text = json.load(json_file)
        f['fileName'] = js
        f['relatedIssues'] = []
        for ri in json_text['relatedIssues']:
            f['relatedIssues'].append(ri['lawName'] + ' ' + ri['issueRef'])
        f['relatedIssues'] = list(dict.fromkeys(f['relatedIssues']))

    result.append(f)

result = sorted(result, key=lambda k: k['fileName']) 
for r in result:
    print(r['fileName'] + '\t' + str(r['relatedIssues']))