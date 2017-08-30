"""Site parser logic
"""

from bs4 import BeautifulSoup
import unicodedata
import string


class Siteparser:
    def __init__(self):
        pass

    def data_process(self, dataraw_country, dataraw_odds):
        dataclean_country = []
        dataclean_odds = []
        for country in dataraw_country:
            txt = string.join(country.text.split())
            dataclean_country.append(unicodedata.normalize('NFKD', txt).encode('ascii','ignore'))

        for odds in dataraw_odds:
            txt = string.join(odds.text.split())
            dataclean_odds.append(unicodedata.normalize('NFKD', txt).encode('ascii','ignore'))

        procesed_data = dict(zip(dataclean_country, dataclean_odds))
        return procesed_data

    # TODO: fix for 2 sites (first - proxy cause, second - navigation)
    def pars_Williamhill(self, soup):
        dataraw_country = soup.find_all('div', {'class': 'eventselection'})
        dataraw_odds = soup.find_all('div', {'class': 'eventprice'})
        return self.data_process(dataraw_country, dataraw_odds)

    def pars_Skybet(self, soup):
        dataraw_country = soup.find_all('span', {'class': 'oc-desc'})
        dataraw_odds = soup.find_all('b', {'class': 'odds'})
        return self.data_process(dataraw_country, dataraw_odds)

    def pars_Paddypower(self, soup):
        dataraw_country = soup.find_all('span', {'class': 'odds-label'})
        dataraw_odds = soup.find_all('span', {'class': 'odds-value'})
        return self.data_process(dataraw_country, dataraw_odds)

    def pars_Mobilebet(self, soup):
        dataraw_country = soup.find_all('span', {'class': 'opp'})
        dataraw_odds = soup.find_all('span', {'class': 'odds'})
        return self.data_process(dataraw_country, dataraw_odds)

    def parsing(self, data, source_name):
        soup = BeautifulSoup(data, 'html.parser')
        if source_name == 'Williamhill':
            return {source_name : self.pars_Williamhill(soup)}
        elif source_name == 'Skybet':
            return {source_name : self.pars_Skybet(soup)}
        elif source_name == 'Paddypower':
            return {source_name : self.pars_Paddypower(soup)}
        elif source_name == 'Mobilebet':
            return {source_name : self.pars_Mobilebet(soup)}
        else:
            return dict()
