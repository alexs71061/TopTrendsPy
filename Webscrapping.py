import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://trends24.in/united-states/'
my_url

###open connection, get page, close client
uclient = uReq(my_url)
page_rawtwitter = uclient.read()
uclient.close()
page_twitter = soup(page_rawtwitter, "html.parser")
#grab trend card from site
twiter_trendcard = page_twitter.findAll('div', {'class':"trend-card"})
twit_top = twiter_trendcard[0]
alltop = twit_top.findAll('li',{'title':""})

filename = "TopTwitter.csv"
f = open(filename, "w")
headers = "Top Twitter Hashtags\n"
f.write(headers)

for eachline in alltop:

    numbers = eachline.a.text

    print(numbers)

    f.write(numbers + '\n')
f.close()