import csv
import glob
import os

MAX_NUMBER_OF_FILES = 5

def read_data():
    path = os.getcwd() + '\data\dataToRead'
    listOfFiles = []
    filesName = []
    numberOfFiles = 0
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    for f in csv_files:

        if numberOfFiles + 1 > MAX_NUMBER_OF_FILES:
            break
        print("wczytano: " + str(f.title()))
        filesName.append((f.title()))
        csvreader = csv.reader(open(f))
        points = []
        i = 0
        for point in csvreader:
            try:
                float(point[0])
                points.append((float(point[0]), float(point[1])))
                i += 1
            except ValueError:
                pass

        listOfFiles.append(points)

        numberOfFiles += 1

    return listOfFiles, filesName
