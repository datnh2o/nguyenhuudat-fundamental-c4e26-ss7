#1
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

print("Chỉ số chất lượng về không khí (AQI)")
city = input("Nhập tên Thành phố: ")
url = "https://wind.waqi.info/nsearch/full/{}?n=4".format(city)
conn = urlopen(url)
#2
raw_data= conn.read() 
html_content = raw_data
dict_content = json.loads(html_content)   
time = dict_content["results"][0]["s"]["t"][0]
location = dict_content["results"][0]["s"]["n"][0]
aqi = dict_content["results"][0]["s"]["a"]

print("Date - Time: ", time)
print("Location: ", location)
print("AQI: ", aqi)
