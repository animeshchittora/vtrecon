import requests
import json 
import pyfiglet

ascii_banner=pyfiglet.figlet_format("VT-RECON!")
print(ascii_banner)

print("\n")

url = 'https://www.virustotal.com/vtapi/v2/domain/report'

print("url exampple---------> site.com")
data=input("Enter URl : ")
print("\n")

params = {'apikey':'<apikey>','domain':data}

print("[1] for whois info")
print("[2] for subdomains")
pref=int(input("Enter Number : "))


try:
	response = requests.get(url, params=params)
	jdata=response.json()
	sub_domains=jdata['subdomains']
	more_domains=jdata['last_https_certificate']['extensions']['subject_alternative_name']
	


	if(pref==1):
		print("--------------------------------------whois info------------------------------")
		print("\n")
		whois=jdata['whois']
		print(whois)
		print("\n")

	elif(pref==2):
		print("---------------------------------------subdomains----------------------------")
		print("\n")
		for sub in sub_domains:
			print(sub)
		for domain in more_domains:
			print(domain)

	else:
		print("Enter correct choice")
		
except(KeyError):
	print("No sub-domains found")
	exit(0)
