#opening different file formats in python

filename = "data.txt"

#  ../../ is used to move 2 directory upwards

filepath = "../../PFDA-courseware/code/Topic01-getting started/datafiles/data.txt"
#"../PFDA-courseware/code/Topic01-getting started/datafiles/"
print (filepath + filename)
with open (filepath, "rt") as dt:
    for line in dt:
        print (line)

