from ast import arg
from base64 import encode
import sys
import re
import PyPDF2 
import csv
import glob

# hash tables for ditance and levels
distances = {'MEN': '10', 'WOMEN': '6','NAIAM': '8', 'NAIAW': '5'}
level = {'I': '1', 'II': '2','III': '3'}

outName = "NCAA_Results.csv"
header = ['Place', 'Gender', 'Time', 'Distance', 'Level', 'Year']
f = open(outName, 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)



file_list = glob.glob("*.pdf")
for j in file_list:
    # creating a pdf reader object 
    pdfReader = PyPDF2.PdfReader(j) 
    # creating a page object for page
    pageObj1 = pdfReader.pages[0] 
    pageObj2 = pdfReader.pages[2]
    pageObj3 = pdfReader.pages[3]
    # grab text from first page
    text1 = str(pageObj1.extract_text())
    # Scrape year from the pdf
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
    # grab text data pages
    text2 = str(pageObj2.extract_text())
    text3 = str(pageObj3.extract_text())
    # Scrape first data page, convert to seconds and write to csv
    read2 = re.findall("(\d{1,3})\.* [^,\n]*\s*,\s*[^,]*\s*,\s*[^,]*\s*,*\s+(\d+:\d+\.\d)",text2)
    for i in range(len(read2)):
        readTime = re.search("(\d{2}):(\d{2}\.\d)", read2[i][1])
        time = int(readTime.group(1))*60 + float(readTime.group(2))
        data = [read2[i][0], gender, time, distance, level[l], year]
        writer.writerow(data)

    read3 = re.findall("(\d{1,3})\.* [^,\n]*\s*,\s*[^,]*\s*,\s*[^,]*\s*,*\s+(\d+:\d+\.\d)",text3)
    for i in range(len(read3)):
        readTime = re.search("(\d{2}):(\d{2}\.\d)", read3[i][1])
        time = int(readTime.group(1))*60 + float(readTime.group(2))
        data = [read3[i][0], gender, time, distance, level[l], year]
        writer.writerow(data)
    
f.close()