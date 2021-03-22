from urllib.request import urlopen
from bs4 import BeautifulSoup

class WOTD_English:
    def __init__(self, soup):
        self.soup = soup
        self.wotd_string = self.get_wotd()
        self.wotd_type, self.wotd_definition = self.get_wotd_definition()

    def get_wotd(self):
        soup = self.soup
        wotd_headword_divs = soup.find_all("div",{"class":"otd-item-headword__word"})[0]
        wotd_string = wotd_headword_divs.find('h1').contents[0]
        return wotd_string

    def get_wotd_definition(self):
        soup = self.soup
        def_headword_def_divs = soup.find_all("div",{"class":"otd-item-headword__pos"})[0]
        def_headword_def_p = def_headword_def_divs.find_all('p')
        def_type_string = def_headword_def_p[0].contents[1].contents[1].contents[0]
        def_string = def_headword_def_p[1].contents[0]
        return def_type_string, def_string

    def wotd_msg(self):
        output = f'> **{self.wotd_string}**\n> *{self.wotd_type}*\n> {self.wotd_definition}'
        #print(output)
        return output
