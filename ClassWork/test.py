import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

response.encoding = "utf-8"
html = response.text

soup = BeautifulSoup(html, "html.parser")
movie_list = soup.find("ol", class_="grid_view").find_all("li")

for movie in movie_list:
    name = movie.find("span", class_="title").text
    info = movie.find("div", class_="bd").find("p").text
    rating = movie.find("span", class_="rating_num").text
    comment_num = movie.find("div", class_="star").find_all("span")[-1].text[:-3]
    print(f"电影名称：{name}")
    print(f"电影信息：{info}")
    print(f"评分：{rating}")
    print(f"评论数：{comment_num}")
    print("-" * 50)
