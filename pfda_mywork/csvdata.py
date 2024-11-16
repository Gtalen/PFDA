import csv

dtpath = "../../PFDA-courseware/code/Topic01-getting started/datafiles/data.csv"
with open (dtpath, "r") as data:
      dt = csv.reader(data, delimiter=',',quoting = csv.QUOTE_NONE)
      for line in data:
        print (line)
        dt = csv.reader(data, delimiter=',',quoting = csv.QUOTE_ALL)
        for line in data:
            print (line)