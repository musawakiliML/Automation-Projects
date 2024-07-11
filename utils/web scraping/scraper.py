# import requests

# try:
#     r = requests.get("http://ip.jsontest.com/")
#     print("response object", r)
#     print("response text", r.text)

#    #  payload = {"q": "python"}
#    #  r = requests.get("https://github.com/search", params=payload)
#    #  print("Response:", r.text)

#     payload = {"key1":"value1"}
#     r = requests.post("http://httpbin.org/post", data=payload)
#     print("Response:", r.text)
# except requests.exceptions.RequestException as e:
#     print("Error Message:", e)


# from lxml import html
# import requests

# page = requests.get('https://github.com/pricing/')
# html_tree = html.fromstring(page.content)

# plans = html_tree.xpath('//h2[@class="mb-2 h5-mktg"]/text()')
# pricing = html_tree.xpath('//span[@class="js-computed-value"]/text()')

# print(plans, pricing)


# import bs4

# myfile = open("utils/web scraping/python.html")
# soup = bs4.BeautifulSoup(myfile, "lxml")

# print(soup.find_all("a")[0]['href'])
# print(soup.find("div", {"id": "inventor"}).get_text())
# print(soup.select("#inventor"))
# print(soup.select('.wow'))
import re
import os
import urllib.request
from bs4 import BeautifulSoup

image_type = "Project"
movie = 'Demon%20Slayer%20Anime'

url = f"https://www.google.com/search?q={movie}&source=lnms&tbm=isch"
header = {"User-Agent": 'Mozilla/5.0'}
soup = BeautifulSoup(urllib.request.urlopen(url), features='lxml')

images = [a["src"] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})][:5]
for img in images:
   # print("Image Source:", img)
   raw_img = urllib.request.urlopen(img).read()
   counter = len([i for i in os.listdir(".") if image_type in i]) + 1
   f = open(image_type + "_" + str(counter) + ".jpg", "wb")
   f.write(raw_img)
   f.close()   