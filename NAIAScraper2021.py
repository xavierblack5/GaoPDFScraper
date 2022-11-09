from ast import arg
from base64 import encode
import sys
import tabula as tb
import tabulate as tbl
import pandas as pd
import re
import PyPDF2 
import csv
import argparse

# Setup argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--Append", help = "Append data to existing file")
parser.add_argument("-c", "--Count", help = "Integer number of data inputs to read from the input pdf")
# parser.add_argument("-n", "--New", help = "Make a new file to write the data to")
parser.add_argument("i", help = 'Input pdf file name')
parser.add_argument("y", help = 'Input year')
args = parser.parse_args()

inFileName = args.i
if not ".pdf" in inFileName:
    print("Input must be a pdf")
    sys.exit()


df = tb.read_pdf(inFileName, pages="1", multiple_tables=False)

text = str(df[0])
read1 = re.findall("(\d{1,3}) \w+( |-)*\w*, \w* *\w{2} \d{1,3} (\S+( |-)){1,5}\s*(\d{1,3}|-)\s*(\d{2}:\d{2}\.\d)", text)
read2 = re.search("Men|Women", text)
if 'Men' == read2[0]:
    gender = 1
    distance = 8
else:
    gender = 2
    distance = 5
count = 10
if args.Count:
    count = int(args.Count)
table = []
for i in range(0,len(read1)):
    if int(read1[i][0]) < count + 1:
        table.append(read1[i])  

for i in range(0,count-8):
    place = table.pop(0)      
    table.append(place)


# Open csv file
if args.Append:
    outName = args.Append
    f = open(outName, 'a', newline='')
    writer = csv.writer(f)
else:
    outName = inFileName.replace(".pdf", ".csv")
    header = ['Place', 'Gender', 'Time', 'Distance', 'Level', 'Year']
    f = open(outName, 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(header)

year = args.y
if int(year) < 2021:
    print("year must be past 2021")
    sys.exit()

for i in range(0,len(table)):
    readTime = re.search("(\d{2}):(\d{2}\.\d)", table[i][5])
    time = int(readTime.group(1))*60 + float(readTime.group(2))
    data = [table[i][0], gender, time, distance, 4, year]
    writer.writerow(data)
    

# hash tables for ditance and levels
distances = {'Men': '8', 'Women': '5'}
level = {'I': '1', 'II': '2','III': '3'}




# closing the file objects
# pdfFileObj.close() 

