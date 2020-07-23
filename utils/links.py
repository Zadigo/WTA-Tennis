from bs4 import BeautifulSoup
import os

PAGE = 'C:\\Users\\Pende\\Documents\\myapps\\WTA-Tennis\\pages\\EugeniBouchard.html'

class Pages:
    def __init__(self, page_name=None):
        self.pages = os.walk()
        with open(PAGE, encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            links = soup.find_all('a', attrs={'class': 'btn-stats'})
            self.links = (link['href'] for link in links if link)

    def __call__(self, page_name):
        self.__init__(page_name=page_name)

    def __len__(self):
        return len(list(self.links))

    @property
    def first(self):
        return list(self.links)[:1]
    
    @property
    def last(self):
        return list(self.links)[1:]

paginator = Pages()
