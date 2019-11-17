def add_to_file(path, data):
    with open(path, 'a') as f:
        print(data, file=f)


def add_set_to_file(path, data):
    with open(path, 'a') as f:
        for datapoint in data:
            print(datapoint.username, file=f)


def write_to_file(dataSet, PATH):
    with open(PATH, 'w') as f:
        for item in dataSet:
            print(item, file=f)


def get_set_from_file(path):
    dataSet = set()
    with open(path, 'r') as f:
        fileLines = f.readlines()
        for line in fileLines:
            # Remove linebreak character
            line = line[:-1]
            # Add item to list
            dataSet.add(line)
    return dataSet
