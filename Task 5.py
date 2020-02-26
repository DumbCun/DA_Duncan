#Task 5i
import requests
#Set target Website
URL = 'http://172.17.50.43/algenius'
r = requests.get(URL)
print(r.text)
#Task 5 Part 2:
print('Status_Code')
print('\t OK:', r.status_code)
#Website Header
h = requests.head(URL)
print('Header:')
#To print line by line
for x in h.headers:
    print('\t -/headers.php', x, ':', h.headers[x])
#Modify the Header's user-agent
headers = {
    'User-Agent' : 'Mobile'
}
rh = requests.get(URL, headers = headers)
print(rh.text)