from bs4 import BeautifulSoup
import urllib.request


class AppURLopener(urllib.request.FancyURLopener):
    version = "Chrome/46.0"
    pass


def scrape(rawtext):
    rawtext = rawtext .split(" ")
    text = ""
    for _ in rawtext:
        text += _+"+"
    text = text[:-1]

    #print(text)

    query = "https://www.google.co.in/search?q="+text

    opener = AppURLopener()

    html = opener.open(query).read()
#    html = urllib.request.urlopen(query).read()
    bs_html = BeautifulSoup(html, "html.parser")

    for div in bs_html.findAll('div', attrs={'class':'g'}):
        link = div.find('a')
        try:
            link = link['href']
        except:
            continue
        if not (link.find("/url?q=") == -1):
            ind = link.find("&sa=U")
            link = link [7:ind]
            print(link)



if __name__ == "__main__":
    _ = str(input("Enter query:"))
    scrape(_)