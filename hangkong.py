import requests
proxies = {
  "https": "http://58.251.76.29"
}
r=requests.get('http://www.variflight.com/schedule/CTU-TSN-GS7888.html?AE71649A58c77=&fdate=201707',proxies=proxies)
r.encoding=r.apparent_encoding
print(r.text)
