import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pdftotext import convert_pdf_to_txt
from data_extract import extractor



def get_html(url):
	# returns html of the webpage from url
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	return mystr

def download_file(download_url,save_path):
	#download binary files like pdf
	response = urlopen(download_url)
	file = open(save_path, 'wb+')
	file.write(response.read())
	file.close()



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



# result_url = """https://www.ktu.edu.in/eu/res/viewExamResults.htm?examDefIdEnr=PXWICZ57B6PcSF7NA%2FqyDlx%2FBbieI99UDGm0PtoFocg%3D&type=3IcV3MhL9p%2FDdB%2FcWAiPRLKlmX8r0%2B%2FsZFCVI%2Fx8bjI%3D&publishId=%2Bjvpw5b2g4cWkUV8essjUJZMB8vvszOylAB%2FPDL6%2BGs%3D"""

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
for url in download_links:
	no_of_colleges = no_of_colleges + 1
	download_file(url,"./pdf/{}.pdf".format(no_of_colleges))
	print("Downloaded {}-".format(no_of_colleges))
print("Download completed")


print("Started conversion of files...")
print("Please wait!")
for i in range(1,no_of_colleges+1):
	convert_file("./pdf/{}.pdf".format(i),"./text/{}.txt".format(i))
	extractor("./text/{}.txt".format(i),"./extracted_data")
	print("Converted {}-".format(i))
print("Conversion completed and data extracted")
