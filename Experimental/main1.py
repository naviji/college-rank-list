import urllib.request
import pathlib
from multiprocessing.dummy import Pool as ThreadPool
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
	# #download binary files like pdf (not text)
	# response = urlopen(download_url)
	# with open (save_path, 'wb+') as f:
	# 	f.write(response.read())
	# 	f.seek(0)
	try:
		urllib.request.urlretrieve(download_url, save_path)
	except:
		pass



def convert_file(src,des):
	# convert pdf in desc path to txt file and store in src path
	raw_text = convert_pdf_to_txt(src)
	text_file = open(des,"w")
	text_file.write(raw_text)
	text_file.close()


def makedirectory(filename):
	pathlib.Path(filename).mkdir(parents=True, exist_ok=True)


#result_url = input("Enter the url of result page: ")
# format should be https://www.example.com

#result_url = """https://www.ktu.edu.in/eu/res/viewExamResults.htm?examDefIdEnr=s1f1Yz9Ez3mTh8FehlN0IbecTuk%2FmUaexaZvdnucfuQ%3D&type=XCaROGlc62E6b4hab1%2BeaPK63kmhAF3qL%2FVAa1ccNuk%3D&publishId=VJLLijUz7ldOzCMNC5TsTFlIwYh%2BPpX%2FyAhNMPjLm%2FI%3D"""

#reevaluation
#result_url = """https://www.ktu.edu.in/eu/res/viewExamResults.htm?examDefIdEnr=PXWICZ57B6PcSF7NA%2FqyDlx%2FBbieI99UDGm0PtoFocg%3D&type=3IcV3MhL9p%2FDdB%2FcWAiPRLKlmX8r0%2B%2FsZFCVI%2Fx8bjI%3D&publishId=%2Bjvpw5b2g4cWkUV8essjUJZMB8vvszOylAB%2FPDL6%2BGs%3D"""
#supply
#result_url = """https://www.ktu.edu.in/eu/res/viewExamResults.htm?examDefIdEnr=ilmUvhZYmVvMXSiX2buWscMIhg8OfZJikOsUhhZ2ULk%3D&type=cDk%2BT1gsF8ZclRnxnujvZr94kxf%2FEXg0wbSuoV0dN6k%3D&publishId=l9ePEsb6%2FlHkSLvJtsuKn%2FLl%2Bok7jVe6iR8n6XcyHhw%3D"""



with open("./url_file.txt") as f:
	url_list = f.readlines()
url_list = [x.strip() for x in url_list]

result_count = 0
for result_url in url_list:
	if(result_url):
		print(result_url)
		result_count = result_count + 1

		print(":Processing link {}:".format(result_count))
		download_links = [] # list to store the download urls
		count = 0 # initialize number of colleges to zero

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

		save_loc =  "/home/navi/Desktop/environments/data/{}".format(str(result_count))
		makedirectory(save_loc)
		makedirectory(save_loc+"/pdf")
		makedirectory(save_loc+"/text")
		makedirectory(save_loc+"/info")
		print("Started downloading files...")
		print("Please wait!")
		destination = ["{}/pdf/{}.pdf".format(save_loc,i) for i in range(0,len(download_links))]
		pool = ThreadPool(100)
		results = pool.starmap(download_file, zip(download_links, destination))
		print("\nDownloaded--")
		for count in range(0,len(download_links)):
			print("")
			print("Downloaded\t{}-".format(count))
			convert_file("{}/pdf/{}.pdf".format(save_loc,count),"{}/text/{}.txt".format(save_loc,count))
			print("Converted\t{}-".format(count))
			extractor("{}/text/{}.txt".format(save_loc,count),save_loc+"/info")
			print("Extracted\t{}-".format(count))
			print("")
		print("Completed!")

print(":Finished!:")
