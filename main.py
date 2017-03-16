import urllib3
import sys
from tqdm import tqdm
from bs4 import BeautifulSoup
sys.stdout = open('IMDB_Top_1000_Movies.txt', 'w')
i = 1
for x in tqdm(range(1, 21)):
    url = "http://www.imdb.com/search/title?groups=top_1000&sort=user_rating&view=simple&page="+str(x) + "&ref_=adv_prv"
    r = urllib3.PoolManager().request('GET', url).data
    soup = BeautifulSoup(r, "html.parser")  # Beautiful soup object
    listerList = soup.find('div', attrs={'class': 'lister-list'})
    itemList = listerList.findAll('div', attrs={'class': 'lister-item mode-simple'})
    for each in itemList:
        coltitle = each.find('div', attrs={'class': 'col-title'})
        ratingItem = each.find('div', attrs={'class': 'col-imdb-rating'})
        print(str(i) + ": " + coltitle.find('a').text.strip('\n\t ') + ' - ' +ratingItem.find('strong').text.strip('\n\t '))
        i += 1
