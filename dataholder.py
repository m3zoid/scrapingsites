"""Here is a class for data holding
"""

class Dataholder:
    def __init__(self):
        self.datapool = dict()
        self.dataprep = dict()

    def clean(self):
        self.datapool = dict()
        self.dataprep = dict()

    def add_data(self, newdata):
        self.datapool.update(newdata)

    def prepare_data(self):
        servers = []
        countries = []
        for server, data in self.datapool.iteritems():
            servers.append(server)
            for country, odds in data.iteritems():
                countries.append(country)

        servers = set(servers)
        countries = set(countries)

        for country in countries:
            self.dataprep[country] = {}
            for server in servers:
                self.dataprep[country][server] = self.datapool[server][country] if country in self.datapool[server] else '-'

    def get_prepared(self):
        self.prepare_data()
        return self.dataprep
