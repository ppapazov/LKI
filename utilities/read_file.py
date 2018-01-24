import csv


def getCSVdata(fileName):

    data = []

    file = open(fileName, "r")
    reader = csv.reader(file)
    next(reader)

    for line in reader:
        data.append(line)

    return data
