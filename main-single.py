import urllib.request
import pathlib
from multiprocessing.dummy import Pool as ThreadPool
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pdftotext import convert_pdf_to_txt
from data_extract import extractor
import os
import sys

i = 45

def convert_file(source,destination):
    # convert pdf in desc path to txt file and store in source path
    raw_text = convert_pdf_to_txt(source)
    text_file = open(destination,"w")
    text_file.write(raw_text)
    text_file.close()

    
convert_file("./pdf/{}.pdf".format(i),"./text/{}.txt".format(i))
# os.remove("./pdf/{}.pdf".format(i))
extractor("./text/{}.txt".format(i))
# os.remove("./text/{}.txt".format(i))
print("Converted {}-".format(i))