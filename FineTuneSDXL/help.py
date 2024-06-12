import json

with open('metadata.jsonl', 'r') as json_file:
    data = [json.loads(line) for line in json_file]

new = []
c=0
for i in data:
    if int(i['file_name'][:len(i['file_name'])-4])<=5000:
        c+=1
        print(c)
        new.append(i)

with open('cut.jsonl', 'w') as json_file:
    for i in new:
        json.dump(i, json_file)
        json_file.write('\n')
