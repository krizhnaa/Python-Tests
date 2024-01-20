from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.p)

allanchor = soup.find_all("a")

# for anchor in allanchor:
#     print(anchor.get("href"))

lol = soup.select(selector=".heading")

for _ in lol:
    print(_.string)