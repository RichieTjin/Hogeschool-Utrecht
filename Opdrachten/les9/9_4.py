import csv

with open('artikelen.csv', 'r') as f:
  reader = csv.reader(f)
  regels = list(reader)

  print(regels)

infile = open('example.txt')
