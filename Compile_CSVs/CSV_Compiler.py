from ast import arg
from base64 import encode
import glob
import tabula as tb
import tabulate as tbl
import pandas as pd
import csv



header = ['Place', 'Gender', 'Time', 'Distance', 'Level', 'Year']
f = open("XC_Results.csv", 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)

file_list = glob.glob("*.csv")
for j in file_list:
    # creating a pdf reader object 
    if j != "XC_Results.csv":
        r=open(j, 'r')
        reader = csv.reader(r)
        for data in reader:
            writer.writerow(data)
        print("Finished " + j)
        r.close()
   
    

# with open("demo_csv.csv", mode="r") as old_file:
#     reader_obj = csv.reader(old_file) #read the current csv file

#     with open("new_demo_csv.csv", mode="w") as new_file:
#         writer_obj = csv.writer(new_file, delimiter="-") # Writes to the new CSV file 

#         for data in reader_obj:
#             #loop through the read data and write each row in new_demo_csv.csv
#             writer_obj.writerow(data)





# closing the file objects
f.close() 

