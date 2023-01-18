import json
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Read JSON file
with open('Data/data.json', 'r', encoding='utf-8') as json_file:
    json_array = json.load(json_file)

# Index documents in Elasticsearch
for doc in json_array:
    res = es.index(index='sample3', document=doc)
    print(res)
