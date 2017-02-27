
#importing the csv module for using its api in the code
import csv


import re
import sys

file_name = sys.argv[0]
fp = open(file_name)
contents = fp.read()



#f = open('data.csv')

#f is instance of file being opened
#csv_f = csv.reader(f)

#  we are trying to loop over every row
# every row is a list of three elemets, if you see closely

for row in contents:
    print row[0]



f.close()