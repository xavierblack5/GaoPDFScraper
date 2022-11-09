from ast import arg
from base64 import encode
import sys
import tabula as tb
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
args = parser.parse_args()

inFileName = args.i
if not ".pdf" in inFileName:
    print("Input must be a pdf")
    sys.exit()

# creating a pdf file object 
pdfFileObj = open(inFileName, 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
    
# creating a page object for page 1 and 2
pageObj1 = pdfReader.getPage(0) 
pageObj2 = pdfReader.getPage(2) 

# hash tables for ditance and levels
distances = {'MEN': '10', 'WOMEN': '6','NAIAM': '8', 'NAIAW': '5'}
level = {'I': '1', 'II': '2','III': '3'}

# grab text from first page
text1 = str(pageObj1.extract_text())

# # Scrape year from the pdf
read0 = re.search("(\d{4}) Championships",text1)
year = read0.group(1)

# Scrape Division number and gender from the pdf store in variables
read1 = re.search("DIVISION\s(I{1,3})\s(\w{3,5})",text1)
if 'MEN' == read1.group(2):
    gender = 1
    distance = 10
    if 'III' == read1.group(1):
        distance = 8
else:
    gender = 2
    distance = 6
l = read1.group(1)

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


# # grab text data page
text2 = str(pageObj2.extract_text())

# # Scrape top 10 times and convert to seconds and write to csv
read2 = re.findall("(\d{1,3}) [^,\n]*\s*,\s*[^,]*\s*,\s*[^,]*\s*,\s*(\d+:\d+\.\d)",text2)
count = 10
if args.Count:
    count = int(args.Count)
for i in range(0,count):
    readTime = re.search("(\d{2}):(\d{2}\.\d)", read2[i][1])
    time = int(readTime.group(1))*60 + float(readTime.group(2))
    data = [read2[i][0], gender, time, distance, level[l], year]
    writer.writerow(data)
    
# closing the file objects
pdfFileObj.close() 
f.close()