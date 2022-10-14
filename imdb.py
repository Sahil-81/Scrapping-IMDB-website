from bs4 import BeautifulSoup
import requests


max_time=0
movie=""

for num in range(1001,7951,50):
    print(num)
    url = "https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start="+str(num)+"&ref_=adv_nxt"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    paras = soup.find_all('div',class_="lister-item-content")
    for i in paras:
        name=i.find('h3',class_="lister-item-header")
        # print(name.text)
        try:
            time=i.find('span',class_="runtime").text
            time=int(time.split(' ')[0])
            if(time>max_time):
                print(time)
                max_time=time
                movie=name.text.split("\n")[2]
        except:
            continue

print(movie,max_time)

