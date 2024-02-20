import requests
import bs4
import pandas as pd

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

res = requests.get(URL)

data = []

try:
    # it ensures that the page has been downloaded
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.content, "html.parser")

    # finding the movie elements
    elements = soup.find_all("div", class_="article-title-description__text")

    # exploring the movies
    for element in elements:
        pos_title = element.find(
            "h3", class_="title").text.replace(":", ")").split(")")
        year = element.find("strong")
        description = element.find("p", class_="description")

        position = int(pos_title[0].strip())
        title = pos_title[1].strip()

        if year:
            year = year.text
            description = description.text[4:]
        else:
            description = description.text

        dict = {
            "position": position,
            "title": title,
            "year": year,
            "description": description
        }

        data.append(dict)

    df = pd.DataFrame(data)
    df.set_index('position', inplace=True)
    print(df.tail())
    
    df.to_csv('data_100GreatestMovies.csv')

except Exception as exc:
    print(f"There was a problem open the page: {URL}, the problem was: {exc}")
