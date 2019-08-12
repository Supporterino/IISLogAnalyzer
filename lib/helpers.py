import os
import datetime
from lib.models import Logentry


class Helpers:
    def __init__(self, encoding):
        self.encoding = encoding

    @staticmethod
    def http_code_description(sc_status):
        result = "HTTP Code " + str(sc_status) + " ("

        # dictionary of HTTP status codes
        codes = {
            '200': "OK",
            '206': "Partial content",
            '301': "Moved permanently",
            '302': "Found",
            '304': "Not modified",
            '400': "Bad request",
            '401': "Unauthorized",
            '403': "Forbidden",
            '404': "Not found",
            '405': "Method not allowed",
            '406': "Not acceptable",
            '416': "Requested range not satisfiable",
            '500': "Internal server error",
            '501': "Not implemented",
            '502': "Bad gateway",
            '503': "Service unavailable",
            '505': "HTTP version not supported"
        }

        if sc_status in codes:
            result += codes[sc_status] + ")"
        else:
            result += "NO HTTP STATUS CODE DESCRIPTION - check the code meaning on the Internet)"

        return result

    def write_file(self, filepath, data):
        with open(filepath, "w+", encoding=self.encoding) as output:
            output.writelines(data)
        print(":: Written File {}".format(filepath))

    @staticmethod
    def clean_up():
        print(":: Removing old files")
        files = [
            os.getcwd() + "/reports/HttpCodeHits.txt",
            os.getcwd() + "/reports/IpHits.txt",
            os.getcwd() + "/output/output.log",  # see main.py for comment-out rules
            os.getcwd() + "/reports/HitsPerDay.txt",
            os.getcwd() + "/reports/HitsPerEndpoint.txt",
            os.getcwd() + "/reports/Browser.txt",
            os.getcwd() + "/reports/OS.txt",
            os.getcwd() + "/reports/HitsPerMonth.txt",
            os.getcwd() + "/reports/HitsPerHour.txt",
            os.getcwd() + "/reports/HTTPCode206.txt",
            os.getcwd() + "/reports/UsersPerMonth.txt",
                 ]

        for file in files:
            if os.path.exists(file):
                os.remove(file)

    @staticmethod
    def clean_up_csv():
        print(":: Removing old csv files")
        files = [
            os.getcwd() + "/csvs/HitsPerIP.csv",
            os.getcwd() + "/csvs/HitsPerBrowser.csv",
            os.getcwd() + "/csvs/HitsPerDay.csv",
            os.getcwd() + "/csvs/HitsPerEndpoint.csv",
            os.getcwd() + "/csvs/HitsPerHour.csv",
            os.getcwd() + "/csvs/HitsPerMonth.csv",
            os.getcwd() + "/csvs/HitsPerHTTPCode.csv",
            os.getcwd() + "/csvs/HitsPerOS.csv",
            os.getcwd() + "/csvs/HTTP206HitsPerMonth.csv",
            os.getcwd() + "/csvs/UsagesPerMonth.csv",
                 ]

        for file in files:
            if os.path.exists(file):
                os.remove(file)

    def load_files(self):
        print(":: Loading Logfiles to combine")
        lines = []
        if len(os.listdir(os.getcwd() + "/input/")) == 0:
            raise Exception("No Logfiles in input directory")
        for file_name in os.listdir(os.getcwd() + "/input/"):
            if ".log" in file_name:
                file_path = os.getcwd() + "/input/" + file_name
                print("\t :: Reading: {0}".format(file_path))
                with open(file_path, "r", encoding=self.encoding) as log_file:
                    for line in log_file:
                        if not line.startswith("#"):
                            lines.append(line)
        self.write_file(os.getcwd() + "/output/output.log", lines)

    @staticmethod
    def convert_date_into_weekday(input):
        return datetime.date(int(input[0:4]), int(input[5:7]), int(input[8:10])).weekday()

    @staticmethod
    def convert_day_to_string(input):
        weekdays = {
            '0': 'Montag',
            '1': 'Dienstag',
            '2': 'Mittwoch',
            '3': 'Donnerstag',
            '4': 'Freitag',
            '5': 'Samstag',
            '6': 'Sonntag'
        }
        return weekdays.get(str(input))

    def read_file(self, filepath):
        print(":: Loading File {}".format(filepath))
        entries = []
        with open(filepath, "r", encoding=self.encoding) as log_file:
            for line in log_file:
                data = line.split(" ")
                # if data[8] == "192.168.1.20":
                if len(data) == 16:
                    entries.append(
                        Logentry(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9],
                                 data[10], data[11], data[12], data[13], data[14], data[15]))
                elif len(data) == 15:
                    entries.append(
                        Logentry(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9],
                                 data[10], data[11], data[12], data[13], 0, data[14]))
                elif len(data) == 14:
                    entries.append(
                        Logentry(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9],
                                 0, data[10], data[11], data[12], 0, data[13]))

        return entries

    @staticmethod
    def create_directorys():
        print(":: Check if all directorys are present")
        if not os.path.exists("input"):
            os.makedirs("input")
            print("\t:: Created input directory")
        if not os.path.exists("output"):
            os.makedirs("output")
            print("\t:: Created output directory")
        if not os.path.exists("reports"):
            os.makedirs("reports")
            print("\t:: Created reports directory")
        if not os.path.exists("csvs"):
            os.makedirs("csvs")
            print("\t:: Created csvs directory")