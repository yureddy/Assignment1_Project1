import csv


print ("word1", "word2", "word3")
f = open('data.txt')

#f is instance of file being opened
f.close()

csv_f = csv.reader(f)

print(f)