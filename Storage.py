import json


class Storage:

    # Read Data from JSON
    def read(self):
        with open('data.json') as f:
            temp = json.load(f)
            data = []
            data.append(temp)
        return data

    # Write Data to JSON
    def write(self, data):
        json_obj = json.dumps(data, indent=2)
        with open('data.json', "w") as f:
            f.write(json_obj)
