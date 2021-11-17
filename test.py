
import json
from tqdm import tqdm

# remove duplicated cities

# with open('city.list.json') as f:
#     CITY_DATA = json.load(f)

# dataSet = []
# data1 = []
# noStates = []
# hasStates = []
# print('running...')

# for d in tqdm(CITY_DATA):
#     if not d['state']:
#         x = (d['name'], d['country'])
#         if x not in noStates:
#             data1.append(d)
#             noStates.append(x)
#     else:
#         x = (d['name'], d['state'], d['country'])
#         if x not in hasStates:
#             data1.append(d)
#             hasStates.append(x)


# print('passed', len(data1))

# with open('/Users/kammy/Desktop/cs50project/project/updated_city.list.json', 'w') as f:
#     json.dump(data1, f)

# sort by US cities first

with open('updated_city.list.json') as f:
    CITY_DATA = json.load(f)

nonUScities = []
UScities =[]
for c in CITY_DATA:
    if c['country'] == 'US':
        UScities.append(c)
    else:
        nonUScities.append(c)

updated_list = UScities + nonUScities

with open('/Users/kammy/Desktop/cs50project/project/updated_city(1).list.json', 'w') as f:
    json.dump(updated_list, f)
