
#importing the csv module for using its api in the code
import csv


print ("word1", "word2", "word3")
f = open('data.csv')

#f is instance of file being opened
csv_f = csv.reader(f)

#  we are trying to loop over every row
# every row is a list of three elemets, if you see closely

for row in csv_f:
    print row[0]



f.close()