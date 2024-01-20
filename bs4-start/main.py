from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
html_file = response.text

soup = BeautifulSoup(html_file, "html.parser")

anchor_tag = soup.find_all("span", class_="titleline")
anchor_texts = [ anchor.get_text() for anchor in anchor_tag]
print(anchor_texts)

anchor_upvote = [ int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")]
max_upvotes = min(anchor_upvote)
max_index = anchor_upvote.index(min(anchor_upvote))
print(f"The lowest upvote is {max_upvotes}, for the article '{anchor_texts[max_index]} {max_index}'")




























# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.p)
#
# allanchor = soup.find_all("a")
#
# # for anchor in allanchor:
# #     print(anchor.get("href"))
#
# lol = soup.select(selector=".heading")
#
# for _ in lol:
#     print(_.string)

