import os
import json

def getJson(self, json_file):
    data = {}
    script_file = os.path.realpath(__file__)
    directory = os.path.dirname(script_file)
    jasonFile = os.path.join(directory, json_file)
    with open(jasonFile) as data_file:
        data = json.load(data_file)

    print(f"********** {data} **********")
    return data
