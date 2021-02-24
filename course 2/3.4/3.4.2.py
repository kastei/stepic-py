import csv
import datetime


with open("Crimes.csv") as f:
    reader = csv.reader(f)
    res = dict()

    for line in reader:
        # print(line)
        break

    for line in reader:

        if line[2][6:10] != '2015':
            continue
        res[line[5]] = res.get(line[5], 0) + 1

    print(sorted(res.items(), key=lambda x: -x[1])[0][0])
