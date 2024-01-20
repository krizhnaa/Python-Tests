from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
html_file = response.text

soup = BeautifulSoup(html_file, "html.parser")

movie_titles = soup.find_all("h3", class_="title")

movie_titles = [ movie.get_text() for movie in movie_titles ]

final_list = movie_titles[::-1]
print(final_list)
with open("movies.txt", 'w', encoding="utf8") as file:
    for movie in final_list:
        file.write(movie + "\n")

# anchor_tag = soup.find_all("span", class_="titleline")
# anchor_texts = [ anchor.get_text() for anchor in anchor_tag]
# print(anchor_texts)
#
# anchor_upvote = [ int(score.get_text().split()[0]) for score in soup.find_all("span", class_="score")]
# max_upvotes = min(anchor_upvote)
# max_index = anchor_upvote.index(min(anchor_upvote))
# print(f"The lowest upvote is {max_upvotes}, for the article '{anchor_texts[max_index]} {max_index}'")




























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

