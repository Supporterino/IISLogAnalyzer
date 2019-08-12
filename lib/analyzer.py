import collections
import os
from lib import ua_parser


class Analyzer:
    def __init__(self, helpers):
        self.inputpath = os.getcwd() + "/output/output.log"
        self.data = collections.defaultdict()
        self.helpers = helpers
        self.path = os.getcwd() + "/reports/"

    def load_logfile(self):
        self.data = self.helpers.read_file(self.inputpath)

    def run(self):
        self.helpers.clean_up()
        self.helpers.load_files()
        self.load_logfile()
        self.get_users_per_month()
        self.http_206_per_month()
        self.get_hits_hour()
        self.get_hits_month()
        self.get_by_os()
        self.get_hits_per_weekday()
        self.get_statuscode_frequency()
        self.get_ip_hits()
        self.get_hits_per_endpoint()

    def get_ip_hits(self):
        print(":: Analysing Hits per IP Address")
        ip_hits = {}
        fileoutput = "Hits by IP-Address \n\n"
        for entry in self.data:
            if entry.c_ip in ip_hits:
                ip_hits[entry.c_ip] += 1
            else:
                ip_hits[entry.c_ip] = 1
        ip_hits = collections.OrderedDict(sorted(ip_hits.items(), key=lambda kv: kv[1], reverse=True))
        for x in ip_hits:
            fileoutput += "{0}\t{1}\n".format(str(x), str(ip_hits[x]))
        self.helpers.write_file(self.path + "IpHits.txt", fileoutput)

    def get_statuscode_frequency(self):
        print(":: Analysing Statuscode Frequency")
        statuscodes = {}
        fileoutput = "Hits per HTTP Statuscode \n\n"
        for entry in self.data:
            if entry.sc_status in statuscodes:
                statuscodes[entry.sc_status] += 1
            else:
                statuscodes[entry.sc_status] = 1
            statuscodes = collections.OrderedDict(sorted(statuscodes.items(), key=lambda kv: kv[1], reverse=True))
        for x in statuscodes:
            fileoutput += "{0}\t{1}\n".format(self.helpers.http_code_description(x), str(statuscodes[x]))
        self.helpers.write_file(self.path + "HttpCodeHits.txt", fileoutput)

    def get_hits_per_weekday(self):
        print(":: Analysing Hits per Weekday")
        days = [0, 0, 0, 0, 0, 0, 0]
        fileoutput = "Hits per Weekday \n\n"
        for entry in self.data:
            days[self.helpers.convert_date_into_weekday(entry.date)] += 1
        for x in range(7):
            fileoutput += "{0}\t{1}\n".format(self.helpers.convert_day_to_string(x), str(days[x]))
        self.helpers.write_file(self.path + "HitsPerDay.txt", fileoutput)

    def get_users_per_month(self):
        print(":: Analysing Users per Month")
        users = {}
        fileoutput = "Users per Month \n\n"
        # for i in range(len(data) - 1):
        i = 0
        while i < len(self.data) - 1:
            month = self.data[i].date[0:7]
            for j in range(len(self.data) - i):
                # print("Len: {0}, i: {1}, j: {2}".format(len(data), i, j))
                # print("data[i]: {0}, data[j+i]: {1}".format(data[i].c_ip, data[i + j].c_ip))
                if self.data[i].c_ip == self.data[i + j].c_ip and i + j < len(self.data) - 1:
                    continue
                else:
                    i += j
                    if month in users:
                        users[month] += 1
                    else:
                        users[month] = 1
                    break
        users = collections.OrderedDict(sorted(users.items(), key=lambda kv: kv[0]))
        for x in users:
            fileoutput += "{0}\t{1}\n".format(x, users[x])
        self.helpers.write_file(self.path + "UsersPerMonth.txt", fileoutput)

    def get_hits_per_endpoint(self):
        print(":: Analysing Endpoint hits")
        endpoints = {}
        fileoutput = "Hits per Endpoint \n\n"
        for entry in self.data:
            if entry.cs_uri_stem in endpoints:
                endpoints[entry.cs_uri_stem] += 1
            else:
                endpoints[entry.cs_uri_stem] = 1
        endpoints = collections.OrderedDict(sorted(endpoints.items(), key=lambda kv: kv[1], reverse=True))
        for x in endpoints:
            fileoutput += "{0}\t{1}\n".format(x, str(endpoints[x]))
        self.helpers.write_file(self.path + "HitsPerEndpoint.txt", fileoutput)

    def get_by_os(self):
        print(":: Analysing Useragents")
        agents = {}
        browser = {}
        unknowns = {}
        fileoutput_a = "Hits per Useragent \n\n"
        fileoutput_b = "Hits per Browser \n\n"
        for entry in self.data:
            agent = ua_parser.simple_detect(entry.user_agent)
            if agent[0] in agents:
                agents[agent[0]] += 1
            else:
                agents[agent[0]] = 1
            if agent[1] in browser:
                browser[agent[1]] += 1
            else:
                browser[agent[1]] = 1

            if agent[0] == "Unknown OS":
                if entry.user_agent in unknowns:
                    unknowns[entry.user_agent] += 1
                else:
                    unknowns[entry.user_agent] = 1
        agents = collections.OrderedDict(sorted(agents.items(), key=lambda kv: kv[1], reverse=True))
        browser = collections.OrderedDict(sorted(browser.items(), key=lambda kv: kv[1], reverse=True))
        unknowns = collections.OrderedDict(sorted(unknowns.items(), key=lambda kv: kv[1], reverse=True))
        for x in agents:
            fileoutput_a += "{0}\t{1}\n".format(x, str(agents[x]))
            if x == "Unknown OS":
                for i in unknowns:
                    fileoutput_a += "\t{0}\t{1}\n".format(i, str(unknowns[i]))
        for y in browser:
            fileoutput_b += "{0}\t{1}\n".format(y, str(browser[y]))
        self.helpers.write_file(self.path + "OS.txt", fileoutput_a)
        self.helpers.write_file(self.path + "Browser.txt", fileoutput_b)

    def get_hits_month(self):
        print(":: Analysing Hits per month")
        months = {}
        fileoutput = "Hits per Month \n\n"
        for entry in self.data:
            if entry.date[0:7] in months:
                months[entry.date[0:7]] += 1
            else:
                months[entry.date[0:7]] = 1
        months = collections.OrderedDict(sorted(months.items(), key=lambda kv: kv[0]))
        for x in months:
            fileoutput += "{0}\t{1}\n".format(x, str(months[x]))
        self.helpers.write_file(self.path + "HitsPerMonth.txt", fileoutput)

    def get_hits_hour(self):
        print(":: Analysing Hits per Dayhour")
        hours = {}
        fileoutput = "Hits per Hour \n\n"
        for entry in self.data:
            if entry.time[0:2] in hours:
                hours[entry.time[0:2]] += 1
            else:
                hours[entry.time[0:2]] = 1
        hours = collections.OrderedDict(sorted(hours.items(), key=lambda kv: kv[0]))
        for x in hours:
            fileoutput += "{0}\t{1}\n".format(x, str(hours[x]))
        self.helpers.write_file(self.path + "HitsPerHour.txt", fileoutput)

    def http_206_per_month(self):
        print(":: Analysing HTTP Code 206 per month")
        months = {}
        files = {}
        fileoutput = "Hits per Month of http code 206 devided into files \n\n"
        for entry in self.data:
            if entry.sc_status == "206":
                if entry.date[0:7] in months:
                    months[entry.date[0:7]] += 1
                else:
                    months[entry.date[0:7]] = 1
                    files[entry.date[0:7]] = {}
                if entry.cs_uri_stem in files[entry.date[0:7]]:
                    files[entry.date[0:7]][entry.cs_uri_stem] += 1
                else:
                    files[entry.date[0:7]][entry.cs_uri_stem] = 1
        months = collections.OrderedDict(sorted(months.items(), key=lambda kv: kv[0]))
        files = collections.OrderedDict(sorted(files.items(), key=lambda kv: kv[0]))
        for x in files:
            files[x] = collections.OrderedDict(sorted(files[x].items(), key=lambda kv: kv[1], reverse=True))
        for x in months:
            fileoutput += "{0}\t{1}\n".format(x, str(months[x]))
            for y in files[x]:
                fileoutput += "\t{0}\t{1}\n".format(y, str(files[x][y]))
        self.helpers.write_file(self.path + "HTTPCode206.txt", fileoutput)
