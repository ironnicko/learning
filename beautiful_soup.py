from bs4 import BeautifulSoup
import requests, csv

source = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')

csvf = open('none.csv','w')

csvw = csv.DictWriter(csvf,fieldnames=headline)

headlines = ['headline','summary','video_link']

csvw.(headlines)

for article in soup.find_all('article'):

    headline = article.h2.a.text

    summary = article.find('div', class_='entry-content').p.text

    try:
        vid = article.find('iframe',class_='youtube-player')['src']

        vid_id = vid.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://www.youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    # print(vid_id)

    print(yt_link)

    print()

csvf.close()
# with open('nothin.html','r') as html:
#     soup = BeautifulSoup(html,'lxml')

# print(soup.title)#the title object
# print(soup.title.text)#just the text
# print(soup.prettify())#with the indentation
#print(soup.find('div',class_='footer'))
# for article in soup.find_all('div',class_='article'):
#
#     headline = article.h2.a.text
#     print(headline)
#
#     summary = article.p.text
#     print(summary)
#
#     print()
# print(soup.prettify())

#print(summary)

# print(article)

# print(headline)

# print(vid)