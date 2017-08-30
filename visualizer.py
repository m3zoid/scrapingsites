"""Here is a class for data visualization
"""

import os
import time
import string


class Visualizer:
    def __init__(self):
        self.file_name = 'output'
        self.data_src = None
        self.data_str = None
        self.time_loc = None
        self.time_str = None

    def clean(self):
        self.data_src = None
        self.data_str = None
        self.time_loc = None
        self.time_str = None

    def set_data(self, data, ltime):
        self.clean()
        self.data_src = data
        self.time_loc = ltime
        self.time_str = "Get data in: " + time.strftime("%a, %d %b %Y %H:%M:%S", self.time_loc)
        self.prepare_data()

    def prepare_data(self):
        country_maxlen = 0
        site_maxlen = 0
        countries = []
        sites = []
        for country, data in self.data_src.iteritems():
            countries.append(country)
            country_maxlen = len(country) if (len(country) > country_maxlen) else country_maxlen
            if site_maxlen == 0:
                for site, odds in data.iteritems():
                    sites.append(site)
                    site_maxlen = len(site) if (len(site) > site_maxlen) else site_maxlen

        countries.sort()
        sites.sort()
        country_maxlen += 2
        site_maxlen += 2

        # making string
        self.data_str = self.time_str + '\n\n' + string.center('', country_maxlen) + '|'
        for site in sites:
            self.data_str += (string.center(site, site_maxlen) + '|')

        self.data_str += '\n'
        for country in countries:
            self.data_str += (string.center(country, country_maxlen) + '|')
            for site in sites:
                self.data_str += (string.center(self.data_src[country][site], site_maxlen) + '|')

            self.data_str += '\n'

    def output_file(self):
        with open(self.file_name, 'w') as output_file:
            output_file.write(self.data_str)

    def output_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print self.data_str
