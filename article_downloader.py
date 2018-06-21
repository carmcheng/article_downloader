import requests
from bs4 import BeautifulSoup

def nyt():
    h = soup.find("h1").get_text()
    a = soup.find("p", {"itemprop": "author creator"}).get_text()
    d = soup.find("time").get_text()
    story = soup.findAll("div", {"class": "StoryBodyCompanionColumn"})
    b = []
    for div in story:
        paras = div.findAll("p")
        for p in paras:
            b.append(p.get_text())
    return h, a, b, d

def cnn():
    h = soup.find("h1").get_text()
    a = soup.find("p", {"class": "metadata__byline"}).get_text()
    d = soup.find("p", {"class": "update-time"}).get_text()
    story = soup.findAll("div", {"class": "zn-body__paragraph"})
    b = [p.get_text() for p in story]
    return h, a, b, d

if __name__ == "__main__":
    url = input("Article URL: ")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    if "nytimes.com" in url:
        h, a, b, d = nyt()
    elif "cnn.com" in url:
        h, a, b, d = cnn()

    filename = h.replace(" ", "_").replace(",", "") + ".txt"
    output = open(filename, "w")
    output.write(url + "\n")
    output.write(h + "\n" + a + "\n" + d + "\n\n")
    for p in b:
        output.write(p + "\n\n")
    output.close()

    print("Done!")
