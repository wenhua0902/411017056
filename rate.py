import requests
from bs4 import BeautifulSoup
url = "http://www.atmovies.com.tw/movie/next"
Data = requests.get(url)
Data.encoding = "utf-8"
sp = BeautifulSoup(Data.text, "html.parser")
films = sp.select(".filmListAllX li")
for t in films:
  title = t.find("img").get("alt")
  print("片名:" + title)

  images = t.select("img")
  if len(images) == 1:
    rate = "目前尚無分級資訊"
  else:
    rate = images[1].get("src")
  print("電影分級:" + rate + "\n")