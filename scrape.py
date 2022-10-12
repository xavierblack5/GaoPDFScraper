import tabula as tb
import pandas as pd
import re
import PyPDF2 

# creating a pdf file object 
pdfFileObj = open('D12019.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 
pageObj1 = pdfReader.getPage(0) 
pageObj2 = pdfReader.getPage(2) 
    

with open('D1_2019.txt', 'w') as f:
    f.write(pageObj1.extractText())
    f.write(pageObj2.extractText())
    
# closing the pdf file object 
pdfFileObj.close() 