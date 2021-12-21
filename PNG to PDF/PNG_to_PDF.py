import os
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader


mergedObject = PdfFileMerger()
items = os.listdir(r'D:/PNG/')

#PNG to PDF's

for item in items:
    imagel = Image.open(r'D:/PNG/' + item)
    iml = imagel.convert('RGB')
    print(item)
    print(item.split('.')[0])
    iml.save(r'D:/Done/' + item.split('.')[0] + '.pdf')

#PDF's to one PDF

items_pfd = os.listdir(r'D:/Done/')

for pdfitem in items_pfd:
    print(pdfitem)
    if pdfitem.split('.')[1] == 'pdf':
        mergedObject.append(PdfFileReader(r'D:/Done/' + pdfitem, 'rb'))
print('Done')
mergedObject.write(r'D:/WORK/Done_File.pdf')