import urllib.request
import pathlib
from multiprocessing.dummy import Pool as ThreadPool
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pdftotext import convert_pdf_to_txt
from data_extract import extractor
import os
import sys


def get_html(url):
	# returns html of the webpage from url
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	return mystr

def download_file(download_url,save_path):

	#download binary files like pdf (not text)
	try:
		urllib.request.urlretrieve(download_url, save_path)
	except:
		pass



def convert_file(source,destination):
	# convert pdf in desc path to txt file and store in source path
	raw_text = convert_pdf_to_txt(source)
	text_file = open(destination,"w")
	text_file.write(raw_text)
	text_file.close()



download_links = [] # list to store the download urls
no_of_colleges = 0 # initialize number of colleges to zero


result_url = input("Enter the url of result page: ")
# format should be https://www.example.com




html_doc = get_html(result_url)

# arrange html string using html parser
soup = BeautifulSoup(html_doc, 'html.parser')


for link in soup.find_all('a'):
	link_url = link.get('href')
	if("attachment" in link_url):
		if("https://www.ktu.edu.in" not in link_url):
			download_links.append("https://www.ktu.edu.in"+link_url)
		else:
			download_links.append(link_url)


print("Started downloading files...")
print("Please wait!")


print("Download links is {}".format(len(download_links)))

destination = ["{}/pdf/{}.pdf".format(".",i) for i in range(1,len(download_links)+1)]
pool = ThreadPool(100)
results = pool.starmap(download_file, zip(download_links, destination))




print("Started conversion of files...")
print("Please wait!")
for i in range(1,len(download_links)+1):
	convert_file("./pdf/{}.pdf".format(i),"./text/{}.txt".format(i))
	os.remove("./pdf/{}.pdf".format(i))
	extractor("./text/{}.txt".format(i))
	os.remove("./text/{}.txt".format(i))
	print("Converted {}-".format(i))
print("Conversion completed and data extracted")


