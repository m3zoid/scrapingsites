"""Scraping Bot logic
"""

import os
import time
import requests
import traceback
import siteparser
import dataholder
import visualizer


class Scrapingbot:
    def __init__(self, period, source):
        self.period = period
        self.source = source
        self.parser = siteparser.Siteparser()
        self.holder = dataholder.Dataholder()
        self.visualizer = visualizer.Visualizer()

    def sleep_exactly(self, secs):
        end_tm = time.time() + secs
        while True:
            cur_tm = time.time()
            cur_dt = end_tm - cur_tm
            cur_sl = 0
            if cur_dt <= 0:
                return cur_dt
            elif cur_dt <= 0.1:
                cur_sl = cur_dt
            else:
                cur_sl = cur_dt / 10
            time.sleep(cur_sl)

    def get_data(self):
        rawdata_all = {}
        for src_name, settings in self.source.iteritems():
            getdata_site = ''
            try:
                getdata_site = requests.get(settings['URL'], headers=settings['HEAD'], proxies=settings['PROXY'], timeout=10)
            except:
                with open('errorlog', 'a') as output_file:
                    output_file.write("Unexpected error: " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) +\
                                         '\n' + traceback.format_exc() + '\n\n')

            if getdata_site is not '':
                rawdata_all[src_name] = getdata_site.text.encode('utf-8')

        return rawdata_all

    def launch(self):
        correction = 0
        while True:
            time_start = time.time()
            time_local = time.localtime(time_start)

            getdat_all = self.get_data()
            self.holder.clean()
            for sname, data in getdat_all.iteritems():
                self.holder.add_data(self.parser.parsing(data, sname))

            self.visualizer.set_data(self.holder.get_prepared(), time_local)
            self.visualizer.output_file()
            self.visualizer.output_console()

            time_dur = time.time() - time_start
            correction = self.sleep_exactly(self.period + correction - time_dur)
