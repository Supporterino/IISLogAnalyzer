import os
import datetime
from lib.models import Logentry


class Helpers:
    def __init__(self, encoding, fileending):
        """
        This function initializes the helpers class with the needed parameters.
        :param encoding: Encoding of the logfiles.
        :param fileending: The fileformat of the logfiles.
        """
        self.encoding = encoding
        self.ending = fileending

    @staticmethod
    def http_code_description(sc_status):
        """
        This function takes an HTTP statuscode and adds its description.
        :param sc_status: HTTP statuscode as integer
        :return: A string with the HTTP statuscode and its description
        """
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
        """
        This function takes a path and data und writes a file at the location with the data.
        :param filepath: path to file, that should be saved
        :param data: data to write to file
        """
        with open(filepath, "w+", encoding=self.encoding) as output:
            output.writelines(data)
        print(":: Written File {}".format(filepath))

    @staticmethod
    def clean_up():
        """
        This function deletes the old text reports and the combined file.
        """
        print(":: Removing old files")
        report_path = os.getcwd() + "/reports/"
        files = [
            report_path + "HttpCodeHits.txt",
            report_path + "IpHits.txt",
            os.getcwd() + "/output/output.log",  # see main.py for comment-out rules
            report_path + "HitsPerDay.txt",
            report_path + "HitsPerEndpoint.txt",
            report_path + "Browser.txt",
            report_path + "OS.txt",
            report_path + "HitsPerMonth.txt",
            report_path + "HitsPerHour.txt",
            report_path + "HTTPCode206.txt",
            report_path + "UsersPerMonth.txt",
        ]

        for file in files:
            if os.path.exists(file):
                os.remove(file)

    @staticmethod
    def clean_up_csv():
        """
        This function deletes the old csv files.
        """
        print(":: Removing old csv files")
        csv_path = os.getcwd() + "/csvs/"
        files = [
            csv_path + "HitsPerIP.csv",
            csv_path + "HitsPerBrowser.csv",
            csv_path + "HitsPerDay.csv",
            csv_path + "HitsPerEndpoint.csv",
            csv_path + "HitsPerHour.csv",
            csv_path + "HitsPerMonth.csv",
            csv_path + "HitsPerHTTPCode.csv",
            csv_path + "HitsPerOS.csv",
            csv_path + "HTTP206HitsPerMonth.csv",
            csv_path + "UsagesPerMonth.csv",
        ]

        for file in files:
            if os.path.exists(file):
                os.remove(file)

    def load_files(self):
        """
        This function combines all logfiles inside the input directory into one file and removes the headers.
        """
        print(":: Loading Logfiles to combine")
        lines = []
        if len(os.listdir(os.getcwd() + "/input/")) == 0:
            raise Exception("No Logfiles in input directory")
        for file_name in os.listdir(os.getcwd() + "/input/"):
            if self.ending in file_name:
                file_path = os.getcwd() + "/input/" + file_name
                print("\t :: Reading: {0}".format(file_path))
                with open(file_path, "r", encoding=self.encoding) as log_file:
                    for line in log_file:
                        if not line.startswith("#"):
                            lines.append(line)
        self.write_file(os.getcwd() + "/output/output.log", lines)

    @staticmethod
    def convert_date_into_weekday(input_string):
        """
        This function takes a date as a string and returns a number representing the weekday
        :param input_string: string with date in following format YYYY-MM-DD
        :return: a number, which represents the weekday (0-6)
        """
        return datetime.date(int(input_string[0:4]), int(input_string[5:7]), int(input_string[8:10])).weekday()

    @staticmethod
    def convert_day_to_string(input_string):
        """
        This functions converts a number of a weekday into its string.
        :param input_string: number 0-6
        :return: String with weekday
        """
        weekdays = {
            '0': 'Montag',
            '1': 'Dienstag',
            '2': 'Mittwoch',
            '3': 'Donnerstag',
            '4': 'Freitag',
            '5': 'Samstag',
            '6': 'Sonntag'
        }
        return weekdays.get(str(input_string))

    def read_file(self, filepath):
        """
        This function takes the filepath of the combined logfile and reads each entry into an array of objects.
        :param filepath: path to combine logfile
        :return: array of all logentrys as Logentry objects
        """
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
    def beatufiy_month(input_string):
        """
        This function takes a string with a year and month and beautifys it.
        :param input_string: string with month and year in the format 'YYYY-MM'
        :return: String with apprevation of month and year
        """
        months = {
            '01': 'Jan',
            '02': 'Feb',
            '03': 'März',
            '04': 'Apr',
            '05': 'Mai',
            '06': 'Jun',
            '07': 'Jul',
            '08': 'Aug',
            '09': 'Sept',
            '10': 'Okt',
            '11': 'Nov',
            '12': 'Dez'
        }

        return str(months.get(input_string[-2:])) + " " + str(input_string[0:4])
    @staticmethod
    def create_directorys():
        """
        This function generates the needed directorys, if they are missing.
        """
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
        if not os.path.exists("graphs"):
            os.makedirs("graphs")
            print("\t:: Created graphs directory")
        if not os.path.exists("html_report"):
            os.makedirs("html_report")
            print("\t:: Created html_report directory")
