"""Here is a class for construct correct link from home link
"""

import requests


class Pathconstructor:
    def __init__(self):
        self.sites = {  'Williamhill'   : 'http://sports.williamhill.com',
                        'Skybet'        : 'https://www.skybet.com',
                        'Paddypower'    : 'http://www.paddypower.com',
                        'Mobilebet'     : 'https://mobile.bet365.com'}

    def get_links(self):
        # TODO: implement site navigation from home link to correct link; fill data structure
        return {'Williamhill'   : { 'URL'   : 'http://sports.williamhill.com/bet/en-gb/betting/e/1644903/World+Cup+2018+-+Outright.html',
                                    'HEAD'  : {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'},
                                    'PROXY' : None},
                'Skybet'        : { 'URL'   : 'https://www.skybet.com/football/world-cup-2018/event/16742642',
                                    'HEAD'  : {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'},
                                    # 'PROXY' : {'https' : 'https://35.177.13.63',
                                    #            'https' : 'https://35.176.85.99',
                                    #            'https' : 'https://35.176.122.84'}},
                                    'PROXY' : None},
                'Paddypower'    : { 'URL'   : 'http://www.paddypower.com/football/international-football/world-cup-2018?ev_oc_grp_ids=1828129',
                                    'HEAD'  : {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'},
                                    'PROXY' : None},
                'Mobilebet'     : { 'URL'   : 'https://mobile.bet365.com/#type=Coupon;key=1-172-1-26326924-2-0-0-0-2-0-0-0-0-0-1-0-0-0-0-0-0;ip=0;lng=1;anim=1',
                                    'HEAD'  : {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'},
                                    'PROXY' : None}}
