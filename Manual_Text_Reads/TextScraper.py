from ast import arg
from base64 import encode
import sys
import tabula as tb
import pandas as pd
import csv
import re


# print(df)
inFile="NAW2002.txt"
# creating a pdf file object 
tf= open(inFile) 
    
# creating a pdf reader object 
text1 = tf.read()
# print(text1)
    
outName = inFile.replace(".txt", "_Results.csv")
header = ['Place', 'Gender', 'Time', 'Distance', 'Level', 'Year']
f = open(outName, 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)
gender = 2
distance =5
year=2002


read2 = re.findall("(\d{1,3})( \d{1,3}){2}( \S+){4,8} (\d{2}:\d{2})", text1)
# print(read2)
for i in range(len(read2)):
    readTime = re.search("(\d{2}):(\d{2})", read2[i][3])
    time = int(readTime.group(1))*60 + int(readTime.group(2))
    # print(time)
    data = [read2[i][0], gender, time, distance, 4, year]
    writer.writerow(data)
# creating a page object for page 1 and 2
 
# 2017 regex (\d{1,3}) +(\d{1,3})* +(\d{1,3})( \S+){2,3} *([A-Z]{2})*( \S+){1,5} +(\d{2}:\d{2})
# 2015 regex (\d{1,3})( \S+){2} *([A-Z]{2})*( \S+){1,5} *(\d{2}:\d{2}\.\d)
# 2011 regex (\d{1,3})\t(\d{1,3})*\s(\d{1,3})(\s\S+){2,3}\s([A-Z]{2})(\s\S+){1,6}\s(\d{2}:\d{2})
# 2010 regex (\d{1,3})\S* \S*\s*(\d{1,3})( \S+){3,9} \S*(\d{2}:\d{2})
# 2004 regex 
# 2003 regex (\d{1,3}) (\d{1,3})( \S+){6,10} (\d{2}:\d{2}\.\d)


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
tf.close() 
f.close()