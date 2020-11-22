lastnumber = 399
from bs4 import BeautifulSoup
import sys
which = '2 months ago'
with open('url.html', 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, features="html.parser")
i = 0
fout = open('new.txt', 'w') # fout = sys.stdout
for item in soup.find_all("li", {"class": "mdc-list-item"}):
    date = item.find("span", {"class": "iNPTzy"})
    if date and date.text.split(' • ')[1] == which:
        i += 1
        kind = date.text.split(' • ')[0]
        team = date.text.split(' • ')[-1].replace(' Teams','')
        team = "{:,}".format(int(team))
        link = "https://www.kaggle.com" + item.find("a")["href"]
        image = item.find("img")["src"].split("?t=")[0]
        year = '2020'
        isHot = 'false'
        done = 'false'
        title = item.find("div", {"class": "AVXQL"}).text
        desc = item.find("span", {"class": "jrEmlo"}).text
        desc = desc.replace(":", ";").replace("'","")
        prize = item.find("div", {"class": "hscaIv"}).text
        print(f"  - number: '{lastnumber+i}'", file=fout)
        print(f"    title: '{title}'", file=fout)
        print(f"    desc: '{desc}'", file=fout)
        print(f"    kind: '{kind}'", file=fout)
        print(f"    prize: '{prize}'", file=fout)
        print(f"    team: '{team}'", file=fout)
        print(f"    link: '{link}'", file=fout)
        print(f"    image: '{image}'", file=fout)
        print(f"    year: '{year}'", file=fout)
        print(f"    isHot: '{isHot}'", file=fout)
        print(f"    done: '{done}'", file=fout)
        print(f"    solutions: ", file=fout)
fout.close()