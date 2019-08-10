#Xractz
#IndoSec

from requests import Session
import re, sys, json
s = Session()

print("Save File by Xractz - IndoSec\nThis tool is useful for saving your files.\n")
file = input("File  :  ")

url = "https://anonfile.com/api/upload"
headers = {
	'x-requested-with':'XMLHttpRequest',
	
}
try:
	files = open(file,'r')
except:
	print("\n\t* File Not Found! *")
	sys.exit()

f = {
	'file':(file, files)
}
cek = s.post(url, headers=headers, files=f).text
hasil = json.loads(cek)
url1 = str(hasil['data']['file']['url']['full'])
short = str(hasil['data']['file']['url']['short'])
size = str(hasil['data']['file']['metadata']['size']['readable'])

if 'true' in cek:
	print("\nSize  : ",size)
	print("Short : ",short)
	print("Url   : ",url1)
	print("Saved in result.txt")
	s = open("result.txt","a+")
	s.write(f"File  : {file}\nSize  : {size}\nShort : {short}\nUrl   : {url1}\n\n")
	s.close()
else:
	print("\n\t* Failed *")