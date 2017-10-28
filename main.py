import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pdftotext import convert_pdf_to_txt
from data_extract import extractor



def get_html( str ):
	# returns html string from url
	fp = urllib.request.urlopen(str)
	mybytes = fp.read()
	mystr = mybytes.decode("utf8")
	fp.close()
	return mystr

def download_file(download_url,save_path):
	#download binary files like pdf (not text)
	response = urlopen(download_url)
	file = open(save_path, 'wb+')
	file.write(response.read())
	file.close()



def convert_file(src,des):
	# convert pdf in desc path to txt file and store in src path
	raw_text = convert_pdf_to_txt(src)
	text_file = open(des,"w")
	text_file.write(raw_text)
	text_file.close()



download_links = [] # list to store the download urls
count = 0 # initialize number of colleges to zero

#result_url = input("Enter the url of result page: ")
# format should be https://www.example.com

#result_url = """https://www.ktu.edu.in/eu/res/viewExamResults.htm?examDefIdEnr=s1f1Yz9Ez3mTh8FehlN0IbecTuk%2FmUaexaZvdnucfuQ%3D&type=XCaROGlc62E6b4hab1%2BeaPK63kmhAF3qL%2FVAa1ccNuk%3D&publishId=VJLLijUz7ldOzCMNC5TsTFlIwYh%2BPpX%2FyAhNMPjLm%2FI%3D"""

#reevaluation
result_url = """https://www.ktu.edu.in/eu/res/viewExamResults.htm?examDefIdEnr=PXWICZ57B6PcSF7NA%2FqyDlx%2FBbieI99UDGm0PtoFocg%3D&type=3IcV3MhL9p%2FDdB%2FcWAiPRLKlmX8r0%2B%2FsZFCVI%2Fx8bjI%3D&publishId=%2Bjvpw5b2g4cWkUV8essjUJZMB8vvszOylAB%2FPDL6%2BGs%3D"""
#supply
#result_url = """https://www.ktu.edu.in/eu/res/viewExamResults.htm?examDefIdEnr=ilmUvhZYmVvMXSiX2buWscMIhg8OfZJikOsUhhZ2ULk%3D&type=cDk%2BT1gsF8ZclRnxnujvZr94kxf%2FEXg0wbSuoV0dN6k%3D&publishId=l9ePEsb6%2FlHkSLvJtsuKn%2FLl%2Bok7jVe6iR8n6XcyHhw%3D"""
html_doc = get_html(result_url)

# creates a ordered grouping from raw html string
soup = BeautifulSoup(html_doc, 'html.parser')


for link in soup.find_all('a'):
	temp = link.get('href')
	if("attachment" in temp):
		if("https://www.ktu.edu.in" not in temp):
			download_links.append("https://www.ktu.edu.in"+temp)
		else:
			download_links.append(temp)


print("Started downloading files...")
print("Please wait!")
for url in download_links:
	count = count + 1
	download_file(url,"./pdf/{}.pdf".format(count))
	print("Downloaded {}-".format(count))
print("Download completed")


num_college = count # Set number of colleges to count

print("Started conversion of files...")
print("Please wait!")
for i in range(1,num_college+1):
	convert_file("./pdf/{}.pdf".format(i),"./text/{}.txt".format(i))
	extractor("./text/{}.txt".format(i),"./extracted_data")
	print("Converted {}-".format(i))
print("Conversion completed and data extracted")
