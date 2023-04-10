from ast import arg
from base64 import encode
import PyPDF2
import re
import csv
import glob

# hash tables for ditance and levels
distances = {'Men': '8', 'Women': '5'}
level = {'I': '1', 'II': '2','III': '3'}

# Open csv file
outName = "NAIA_Results.csv"
header = ['Place', 'Gender', 'Time', 'Distance', 'Level', 'Year']
f = open(outName, 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)
year = 0
gender = 1
distance = 8

file_list = glob.glob("*.pdf")
for j in file_list:
    pdfReader = PyPDF2.PdfReader(j) 
    num_of_pages = len(pdfReader.pages)
    for i in range(num_of_pages):
        pageObj = pdfReader.pages[i]
        text = str(pageObj.extract_text())
        if i == 0:
            read0 = re.search("\d{2}/\d{2}/(\d{4})",text)
            year = read0.group(1)
        read1 = re.search("Men's|Women's", text)
        if(read1.group(0) == "Men's"):
            gender = 1
            distance = 8
        else:
            gender = 2
            distance = 5
        read2 = re.findall("(\d{1,3})\S+ *\S* *\S*(,| ) *\S* *\S* *\w{2}\d{1,3}(\S+( |-)){1,5}\(*(\d{1,3}|-)\)*\s*(\d{2}:\d{2}\.\d)",text)
        for i in range(len(read2)):
            readTime = re.search("(\d{2}):(\d{2}\.\d)", read2[i][5])
            time = int(readTime.group(1))*60 + float(readTime.group(2))
            data = [read2[i][0], gender, time, distance, 4, year]
            writer.writerow(data)

    # creating a page object for page

    

    # read3 = re.findall("(\d{1,3})\.* [^,\n]*\s*,\s*[^,]*\s*,\s*[^,]*\s*,*\s+(\d+:\d+\.\d)",text3)
    # for i in range(len(read3)):
    #     readTime = re.search("(\d{2}):(\d{2}\.\d)", read3[i][1])
    #     time = int(readTime.group(1))*60 + float(readTime.group(2))
    #     data = [read3[i][0], gender, time, distance, level[l], year]
    #     writer.writerow(data)
    






# closing the file objects
# pdfFileObj.close() 

