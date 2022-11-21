from ast import arg
from base64 import encode
import sys
import tabula as tb
import pandas as pd
import re
import PyPDF2 
import csv
import argparse


# df = tb.read_pdf("NAIAW2_2020.pdf", pages="3", multiple_tables=False)
# print(df)
inFile="NAM2013.pdf"
# creating a pdf file object 
pdfFileObj = open(inFile, 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
outName = inFile.replace(".pdf", "_Results.csv")
header = ['Place', 'Gender', 'Time', 'Distance', 'Level', 'Year']
f = open(outName, 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)
gender = 1
distance =8
year=2013

for i in range(0,6):
    pageObj1 = pdfReader.getPage(i)
    text1 = str(pageObj1.extract_text())
    # print(text1)
    read2 = re.findall("(\d{1,3}) \S+ {0,1}\w*\s\w+\s{0,1}\S*\s{0,1}\S*\s*([A-Z]{2})*( \S+){1,4} +(\d{1,2}:\d{2}\.\d) +(\d{2}:\d{2}\.\d{2})", text1)
    # print(read2)
    for i in range(len(read2)):
        readTime = re.search("(\d{2}):(\d{2}\.\d{2})", read2[i][4])
        time = int(readTime.group(1))*60 + float(readTime.group(2))
        # print(time)
        data = [read2[i][0], gender, time, distance, 4, year]
        writer.writerow(data)
# creating a page object for page 1 and 2
 

# 2019 regex (\d{1,3})\S+ *\S* *\S*,( \S+){1,2} (\w{2}\d{1,3})( *\S+){1,5} \(*(\d{1,3}|-)\)* *(\d{2}:\d{2}\.\d)
# 2018 W regex (\d{1,3})\s*\d{1,3} *\S+ \S* {0,1}\S* *(\w{2}) *( \S+){1,5} *(\d{2}:\d{2}) *\d: \d{2}
# 2018 M regex (\d{1,3})\s*\d{1,3} *\S+ \S* {0,1}\S* {0,1}\S* *([A-Z]{2}) *( \S+){1,5} *(\d{1}:\d{2}){0,1} *\d{1,2}:\d{2} *(\d{2}:\d{2}){0,1} *(\d{2} :\d{2}){0,1} *(\d{2}:\d{2}) *\d{1}:\d{2}
# 2016 M Refex (\d{1,3})\s\S+\s{0,1}\w+,\s\w+\s{0,1}\S*\s{0,1}\S*\s*([A-Z]{2})(\s\S+){1,4}\s+(\d{2}:\d{2}\.\d{2})
# 2014 M Regex (\d{1,3}) \S+ {0,1}\w*,\s\w+\s{0,1}\S*\s{0,1}\S*\s*([A-Z]{2})*( \S+){1,4} +(\d{1,2}:\d{2}\.\d) +(\d{2}:\d{2}\.\d{2})
# 2013 M regex (\d{1,3}) \S+ {0,1}\w*\s\w+\s{0,1}\S*\s{0,1}\S*\s*([A-Z]{2})*( \S+){1,4} +(\d{1,2}:\d{2}\.\d) +(\d{2}:\d{2}\.\d{2})
# 2012 W regex (\d{1,3})( *\d{1,3}){1,2} +\S+( \S+){1,2} +([A-Z] *[A-Z])( {1,2}\S+){1,6} +(\d *\d *: *\d *\d) +\d *: *\d *\d
# 2012 (\d) *(\d) *: *(\d) *(\d) int(readTime.group(1))*600 + int(readTime.group(2))*60 + int(readTime.group(3))*10 + int(readTime.group(4))

# hash tables for ditance and levels
distances = {'MEN': '10', 'WOMEN': '6','NAIAM': '8', 'NAIAW': '5'}
level = {'I': '1', 'II': '2','III': '3'}

# grab text from first page



# # # Scrape year from the pdf
# read0 = re.search("(\d{4}) Championships",text1)
# year = read0.group(1)

# # Scrape Division number and gender from the pdf store in variables
# read1 = re.search("DIVISION\s(I{1,3})\s(\w{3,5})",text1)
# if 'MEN' == read1.group(2):
#     gender = 1
#     distance = 10
#     if 'III' == read1.group(1):
#         distance = 8
# else:
#     gender = 2
#     distance = 6
# l = read1.group(1)

# # Open csv file
# # f = open(outName, 'a', newline='')
# # writer = csv.writer(f)




# # # grab text data page
# text2 = str(pageObj2.extract_text())

# # Scrape top 10 times and convert to seconds and write to csv

    
# closing the file objects
pdfFileObj.close() 
f.close()