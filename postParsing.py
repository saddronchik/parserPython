from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

work = Session()

work.get("https://quotes.toscrape.com/", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

token  = soup.find("form").find("input").get("value")

data = {"csrf_token":token,"username":"andrew","password":"123andrew"}
result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)
def array_ite():
    for count in range(1, 11):
        url = f"https://quotes.toscrape.com/page/{count}"
        response = work.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="quote")

        for i in data:   
            if len(data) != 0:
                res_text = i.find("span", class_="text").text
                res_author = i.find("small", class_="author").text
                print(res_text + "\n" + res_author + "\n\n")
                yield res_text, res_author,
            else:
                break
    # print(text + "\n" + author + "\n\n")