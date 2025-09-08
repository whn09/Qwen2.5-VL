import json

filename = 'llava_next_raw_format/llava_next_raw_format_processed.json'
prefix = 'sharegpt4v'

data = json.load(open(filename, 'r'))
new_data = []
for i in range(len(data)):
    # print(data[i].keys(), data[i]['data_source'], data[i]['image'])
    if 'sharegpt4v' in data[i]['image']:
        # print(data[i])
        new_data.append(data[i])
        # break

json.dump(new_data, open(filename[:-5]+'_'+prefix+'.json', 'w'), ensure_ascii=False)