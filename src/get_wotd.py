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

        for match in soup.findAll('span'):
            match.unwrap()
        return wotd_string

    def get_wotd_definition(self):
        soup = self.soup
        def_headword_def_divs = soup.find_all("div",{"class":"otd-item-headword__pos"})[0]
        #print(def_headword_def_divs)
        def_headword_def_p = def_headword_def_divs.find_all('p')
        #print(def_headword_def_p)

        #print("Get text")
        #print(def_headword_def_p.get_text())
        def_type_string = list(filter(('\n').__ne__, def_headword_def_p[0].contents))[0]
        def_string = list(filter(('\n').__ne__, def_headword_def_p[1].contents))[0]

        return def_type_string, def_string

    def wotd_msg(self):
        output = f':flag_gb: ENGLISH:\n> **{self.wotd_string}**\n> *{self.wotd_type}*\n> __Definition:__ {self.wotd_definition}'
        #print(output)
        return output

class WOTD_Italian:
    def __init__(self, soup):
        self.soup = soup
        self.wotd_string = self.get_wotd()
        self.wotd_type, self.wotd_definition = self.get_wotd_definition()

    def get_wotd(self):
        soup = self.soup
        wotd_headword_divs = soup.find_all('div',{'r101-wotd-widget__word'})[0]
        wotd_string = wotd_headword_divs.contents[0]
        #print(wotd_string)

        for match in soup.findAll('span'):
            match.unwrap()
        return wotd_string

    def get_wotd_definition(self):
        soup = self.soup
        def_div = soup.find_all("div",{"class":"r101-wotd-widget__english"})[0]
        def_string = def_div.contents[0]

        def_type_div = soup.find_all("div",{"class":"r101-wotd-widget__class"})[0]
        def_type_string = def_type_div.contents[0].strip()

        return def_type_string, def_string

    def wotd_msg(self):
        output = f':flag_it: ITALIAN:\n> **{self.wotd_string}**\n> *{self.wotd_type}*\n> __Definition:__  {self.wotd_definition}'
        #print(output)
        return output

class WOTD_German:
    def __init__(self, soup):
        self.soup = soup
        self.wotd_string = self.get_wotd()
        self.wotd_type, self.wotd_definition = self.get_wotd_definition()

    def get_wotd(self):
        soup = self.soup
        wotd_headword_divs = soup.find_all('div',{'r101-wotd-widget__word'})[0]
        wotd_string = wotd_headword_divs.contents[0]
        #print(wotd_string)

        for match in soup.findAll('span'):
            match.unwrap()
        return wotd_string

    def get_wotd_definition(self):
        soup = self.soup
        def_div = soup.find_all("div",{"class":"r101-wotd-widget__english"})[0]
        def_string = def_div.contents[0]

        def_type_div = soup.find_all("div",{"class":"r101-wotd-widget__class"})[0]
        def_type_string = def_type_div.contents[0].strip()

        return def_type_string, def_string

    def wotd_msg(self):
        output = f':flag_de: GERMAN:\n> **{self.wotd_string.lower()}**\n> *{self.wotd_type}*\n> __Definition:__  {self.wotd_definition}'
        #print(output)
        return output

class WOTD_French:
    def __init__(self, soup):
        self.soup = soup
        self.wotd_string = self.get_wotd()
        self.wotd_type, self.wotd_definition = self.get_wotd_definition()

    def get_wotd(self):
        soup = self.soup
        wotd_headword_divs = soup.find_all('div',{'r101-wotd-widget__word'})[0]
        wotd_string = wotd_headword_divs.contents[0]
        #print(wotd_string)

        for match in soup.findAll('span'):
            match.unwrap()
        return wotd_string

    def get_wotd_definition(self):
        soup = self.soup
        def_div = soup.find_all("div",{"class":"r101-wotd-widget__english"})[0]
        def_string = def_div.contents[0]

        def_type_div = soup.find_all("div",{"class":"r101-wotd-widget__class"})[0]
        def_type_string = def_type_div.contents[0].strip()

        return def_type_string, def_string

    def wotd_msg(self):
        output = f':flag_fr: FRENCH:\n> **{self.wotd_string}**\n> *{self.wotd_type}*\n> __Definition:__  {self.wotd_definition}'
        #print(output)
        return output


class WOTD_Russian:
    def __init__(self, soup):
        self.soup = soup
        self.wotd_string = self.get_wotd()
        self.wotd_type, self.wotd_definition, self.word_roman = self.get_wotd_definition()

    def get_wotd(self):
        soup = self.soup
        wotd_headword_divs = soup.find_all('div',{'r101-wotd-widget__word'})[0]
        wotd_string = wotd_headword_divs.contents[0]
        #print(wotd_string)

        for match in soup.findAll('span'):
            match.unwrap()
        return wotd_string

    def get_wotd_definition(self):
        soup = self.soup
        def_div = soup.find_all("div",{"class":"r101-wotd-widget__english"})[0]
        def_string = def_div.contents[0]

        def_roman_div = soup.find_all("div",{"class":"r101-wotd-widget__additional-field romanization"})[0]
        def_roman_string = def_roman_div.contents[0]

        def_type_div = soup.find_all("div",{"class":"r101-wotd-widget__class"})[0]
        def_type_string = def_type_div.contents[0].strip()

        return def_type_string, def_string, def_roman_string

    def wotd_msg(self):
        output = f':flag_ru: RUSSIAN:\n> **{self.wotd_string}** | _*Romanization:*_ {self.word_roman}\n> *{self.wotd_type}*\n> __Definition:__  {self.wotd_definition}'
        #print(output)
        return output


if __name__ == "__main__":
    #url = 'https://www.dictionary.com/e/word-of-the-day/'
    url = 'https://www.italianpod101.com/italian-phrases/'
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    soup = BeautifulSoup(html,features="html.parser")
    #wotd = WOTD_English(soup)
    wotd = WOTD_Italian(soup)
    wotd_msg = wotd.wotd_msg()

    print(wotd_msg)
