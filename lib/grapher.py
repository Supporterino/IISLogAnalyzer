# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt

class Grapher:
    def __init__(self, encoding, helpers):
        """
        This function initializes the grapher with the right encoding and sets the paths.
        :param encoding: The encoding of the reports
        :param helpers: A reference to an helpers object
        """
        self.helpers = helpers
        self.encoding = encoding
        self.path = os.getcwd() + "/graphs/"
        self.report_path = os.getcwd() + "/reports/"

    def remove_old_graphs(self):
        """
        This function removes the old graphics from the graphs directory.
        """
        print("\t:: Removing old graphs")
        for file in os.listdir(self.path):
            os.remove(self.path + "/" + file)

    def run(self):
        """
        This function runs the creation of all graphics.
        """
        print(":: Plotting Graphs")
        self.remove_old_graphs()
        self.plot_weekdays()
        self.plot_hours()
        self.plot_browsers()
        self.plot_month()
        self.plot_endpoints()
        self.plot_http_codes()
        self.plot_os()

    def print_pie_chart(self, in_labels, in_values, graph_title, limit, size):
        """
        This function takes the given parameters and creats a pie chart.
        :param in_labels: An array of labels for the pie chart
        :param in_values: An array of values for the pie chart
        :param graph_title: A string with the name of the chart
        :param limit: An number how much fields should show up in the chart
        :param size: Tuple with lenght and width of the graphic in inch
        """
        labels = []
        values = []
        legend_text = []

        for i in range(len(in_labels)):
            if i < limit:
                labels.append(in_labels[i])
                values.append(in_values[i])

        fig, ax = plt.subplots(figsize=size)
        patches, texts, autotexts = ax.pie(values, autopct='%1.1f%%', shadow=True, startangle=90)
        for i in range(len(labels)):
            legend_text.append(labels[i] + " " + autotexts[i].get_text())
        ax.legend(patches, legend_text, loc="best")
        ax.axis('equal')
        ax.set_title(graph_title)
        fig.set_tight_layout(True)
        fig.savefig(self.path + graph_title)

    def print_bar_chart(self, x_vals, y_vals, graph_title, x_axis, y_axis, limit, size):
        """
        This function takes the given parameters and creats a bar chart.
        :param x_vals: An array of values for the x axis of the bar chart
        :param y_vals: An array of values for the y axis of the bar chart
        :param graph_title: A string with the name of the chart
        :param x_axis: A string with the name of x Axis
        :param y_axis: A string with the name of y Axis
        :param limit: An number how much fields should show up in the chart
        :param size: Tuple with lenght and width of the graphic in inch
        """
        xvals = []
        xlabels = []
        yvals = []
        for i in range(len(x_vals)):
            if i < limit:
                xlabels.append(x_vals[i])
                xvals.append(i)
                yvals.append(y_vals[i])

        fig, ax = plt.subplots(figsize=size)
        ax.bar(xvals, yvals, align="center", alpha=0.5, width=0.5)
        ax.set(title=graph_title, ylabel=y_axis, xlabel=x_axis)
        ax.set_xticks(xvals)
        ax.set_xticklabels(xlabels)
        fig.set_tight_layout(True)
        fig.savefig(self.path + graph_title)

    def plot_weekdays(self):
        """
        This function reads the HitsPerDay report and creats the arrrays to generate a chart
        """
        x = []
        y = []
        print("\t:: Plotting graph for daily use")
        with open(self.report_path + "HitsPerDay.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            x.append(parts[0])
            y.append(int(parts[1].replace('\n', '')))
        self.print_bar_chart(x, y, "Hits per Weekday", "Weekday", "Hits", len(x), None)

    def plot_hours(self):
        """
        This function reads the HitsPerHour report and creats the arrrays to generate a chart
        """
        x = [str(i) for i in range(24)]
        y = [0 for i in range(24)]
        print("\t:: Plotting graph for usage by hour")
        with open(self.report_path + "HitsPerHour.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            y[int(parts[0])] = int(parts[1].replace('\n', ''))
        self.print_bar_chart(x, y, "Hits per Hour", "Hour", "Hits", len(x), None)

    def plot_browsers(self):
        """
        This function reads the Browser report and creats the arrrays to generate a chart
        """
        x = []
        y = []
        print("\t:: Plotting graph for browser usage")
        with open(self.report_path + "Browser.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            x.append(parts[0])
            y.append(int(parts[1].replace('\n', '')))
        self.print_pie_chart(x, y, "Used Browsers", len(x), (12, 7.5))

    def plot_month(self):
        """
        This function reads the HitsPerMonth report and creats the arrrays to generate a chart
        """
        x = []
        y = []
        print("\t:: Plotting graph for hits per month")
        with open(self.report_path + "HitsPerMonth.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            x.append(self.helpers.beatufiy_month(parts[0]))
            y.append(int(parts[1].replace('\n', '')))
        self.print_bar_chart(x, y, "Hits per Month", "Month", "Hits", len(x), (12, 7.5))

    def plot_endpoints(self):
        """
        This function reads the HitsPerEndpoint report and creats the arrrays to generate a chart
        """
        x = []
        y = []
        print("\t:: Plotting graph for endpoint usage")
        with open(self.report_path + "HitsPerEndpoint.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            x.append(parts[0])
            y.append(int(parts[1].replace('\n', '')))
        self.print_pie_chart(x, y, "Used Endpoints (Top 10)", 10, (12, 7.5))

    def plot_http_codes(self):
        """
        This function reads the HttpCodeHits report and creats the arrrays to generate a chart
        """
        x = []
        y = []
        print("\t:: Plotting graph for HTTP statuscodes")
        with open(self.report_path + "HttpCodeHits.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            x.append(parts[0])
            y.append(int(parts[1].replace('\n', '')))
        self.print_pie_chart(x, y, "HTTP Statuscodes", len(x), (12, 7.5))

    def plot_os(self):
        """
        This function reads the OS report and creats the arrrays to generate a chart
        """
        x = []
        y = []
        print("\t:: Plotting graph for OS usage")
        with open(self.report_path + "OS.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            if not entry.startswith('\t'):
                parts = entry.split('\t')
                x.append(parts[0])
                y.append(int(parts[1].replace('\n', '')))
        self.print_pie_chart(x, y, "Operatingsystems", len(x), (12, 7.5))
