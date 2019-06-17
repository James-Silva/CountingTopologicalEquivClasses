import json
import os

def getJsonFile(name):
    with open(name) as f:
        data = json.load(f)
    return data

def writeToJson(name, graph):
    with open(name+'.json', 'w') as outfile:
        json.dump(graph, outfile, indent=4)

def writeToJsonWPath(path, name, graph):
    with open(os.path.join(str(path),name)+'.json', 'w') as outfile:
        json.dump(graph, outfile, indent=4)
