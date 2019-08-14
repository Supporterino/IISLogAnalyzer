import csv
import os


class Writer:
    def __init__(self, encoding, helpers):
        """
        This function initializes the csv writer with the given parameters.
        :param encoding: Encoding of logfiles.
        :param helpers: Reference to a initialized helper class.
        """
        self.encoding = encoding
        self.helpers = helpers
        self.report_path = os.getcwd() + "/reports/"
        self.csv_path = os.getcwd() + "/csvs/"

    def write_ip(self):
        """
        This function converts the ip report to a csv file.
        """
        print("\t:: Writing csv for ip statistics")
        with open(self.report_path + "IpHits.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['IP', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'IP': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(self.csv_path + "HitsPerIP.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_browser(self):
        """
        This function converts the browser report to a csv file.
        """
        print("\t:: Writing csv for browser statistics")
        with open(self.report_path + "Browser.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Browser', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Browser': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(self.csv_path + "HitsPerBrowser.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_days(self):
        """
        This function converts the hits per day report to a csv file.
        """
        print("\t:: Writing csv for daily use")
        with open(self.report_path + "HitsPerDay.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Day', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Day': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(self.csv_path + "HitsPerDay.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_endpoint(self):
        """
        This function converts the hits per endpoint report to a csv file.
        """
        print("\t:: Writing csv for endpoint analyses")
        with open(self.report_path + "HitsPerEndpoint.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Endpunkt', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Endpunkt': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(self.csv_path + "HitsPerEndpoint.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_hour(self):
        """
        This function converts the hits per hour report to a csv file.
        """
        print("\t:: Writing csv for per hour report")
        with open(self.report_path + "HitsPerHour.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Stunde', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Stunde': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(self.csv_path + "HitsPerHour.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_month(self):
        """
        This function converts the hits per month report to a csv file.
        """
        print("\t:: Writing csv for monthly results")
        with open(self.report_path + "HitsPerMonth.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Monat', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'Monat': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(self.csv_path + "HitsPerMonth.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_http_codes(self):
        """
        This function converts the http statuscode report to a csv file.
        """
        print("\t:: Writing csv for http codes")
        with open(self.report_path + "HttpCodeHits.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['HTTP Code', 'Anzahl']
        for entry in data:
            parts = entry.split('\t')
            csv_out.append({'HTTP Code': parts[0], 'Anzahl': parts[1].replace('\n', '')})
        with open(self.csv_path + "HitsPerHTTPCode.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_os(self):
        """
        This function converts the hits per OS report to a csv file. And adds the "Unknown OS" as a sub table.
        """
        print("\t:: Writing csv for OS hits")
        with open(self.report_path + "OS.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_out_unknown = []
        csv_columns = ['OS', 'Hits']
        csv_columns_unknown = ['Unknown OS', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            if not entry.startswith('\t'):
                csv_out.append({'OS': parts[0], 'Hits': parts[1].replace('\n', '')})
            else:
                csv_out_unknown.append({'Unknown OS': parts[1], 'Hits': parts[2].replace('\n', '')})
        with open(self.csv_path + "HitsPerOS.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns_unknown)
            writer.writeheader()
            writer.writerows(csv_out_unknown)

    def write_http_206(self):
        """
        This function converts the hits for HTTP statuscode 206 report to a csv file.
        """
        print("\t:: Writing csv for http codes")
        with open(self.report_path + "HTTPCode206.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Monat', 'Hits']
        for entry in data:
            parts = entry.split('\t')
            if not entry.startswith('\t'):
                csv_out.append({'Monat': parts[0], 'Hits': parts[1].replace('\n', '')})
        with open(self.csv_path + "HTTP206HitsPerMonth.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def write_usage_month(self):
        """
        This function converts the usages per month report to a csv file.
        """
        print("\t:: Writing csv for usage per month")
        with open(self.report_path + "UsersPerMonth.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        csv_out = []
        csv_columns = ['Monat', 'Benutzungen']
        for entry in data:
            parts = entry.split('\t')
            if not entry.startswith('\t'):
                csv_out.append({'Monat': parts[0], 'Benutzungen': parts[1].replace('\n', '')})
        with open(self.csv_path + "UsagesPerMonth.csv", "w+", newline='', encoding=self.encoding) as csv_file:
            writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=csv_columns)
            writer.writeheader()
            writer.writerows(csv_out)

    def run_all(self):
        """
        This function deletes the old csv files and then starts the creation of all reports.
        """
        self.helpers.clean_up_csv()
        print(":: Converting reports to CSV files")
        self.write_ip()
        self.write_browser()
        self.write_days()
        self.write_endpoint()
        self.write_hour()
        self.write_month()
        self.write_http_codes()
        self.write_os()
        self.write_http_206()
        self.write_usage_month()
