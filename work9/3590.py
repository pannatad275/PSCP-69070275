'''flatten'''
import json

def flatten(lst):
    '''flat'''
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

data = json.loads(input().strip())

flat_list = flatten(data)
flat_list.sort(reverse=True)
print(flat_list)
