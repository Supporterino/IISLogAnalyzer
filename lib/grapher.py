# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt

class Grapher:
    def __init__(self, encoding, helpers):
        self.helpers = helpers
        self.encoding = encoding
        self.path = os.getcwd() + "/graphs/"
        self.report_path = os.getcwd() + "/reports/"

    def removeOldGraphs(self):
        print("\t:: Removing old graphs")
        for file in os.listdir(self.path):
            os.remove(self.path + "/" + file)

    def run(self):
        print(":: Plotting Graphs")
        self.removeOldGraphs()
        self.plotWeekdays()
        self.plotHours()
        self.plotBrowsers()
        self.plotWeeks()
        self.plotEndpoints()
        self.plotHTTPCodes()
        self.plotOS()

    def printPieChart(self, inLabels, inValues, graphTitle, limit, size):
        labels = []
        values = []
        legendText = []

        for i in range(len(inLabels)):
            if i < limit:
                labels.append(inLabels[i])
                values.append(inValues[i])

        fig, ax = plt.subplots(figsize=size)
        patches, texts, autotexts = ax.pie(values, autopct='%1.1f%%', shadow=True, startangle=90)
        for i in range(len(labels)):
            legendText.append(labels[i] + " " + autotexts[i].get_text())
        ax.legend(patches, legendText, loc="best")
        ax.axis('equal')
        ax.set_title(graphTitle)
        fig.set_tight_layout(True)
        fig.savefig(self.path + graphTitle)

    def printBarChart(self, xVals, yVals, graphTitle, xAxis, yAxis, limit, size):
        xvals = []
        xlabels = []
        yvals = []
        for i in range(len(xVals)):
            if i < limit:
                xlabels.append(xVals[i])
                xvals.append(i)
                yvals.append(yVals[i])

        fig, ax = plt.subplots(figsize=size)
        ax.bar(xvals, yvals, align="center", alpha=0.5)
        ax.set(title=graphTitle, ylabel=yAxis, xlabel=xAxis)
        ax.set_xticks(xvals)
        ax.set_xticklabels(xlabels)
        fig.set_tight_layout(True)
        fig.savefig(self.path + graphTitle)

    def plotWeekdays(self):
        X = []
        Y = []
        print("\t:: Plotting graph for daily use")
        with open(self.report_path + "HitsPerDay.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            X.append(parts[0])
            Y.append(int(parts[1].replace('\n', '')))
        self.printBarChart(X, Y, "Hits per Weekday", "Weekday", "Hits", len(X), None)

    def plotHours(self):
        X = [ str(i) for i in range(24)]
        Y = [ 0 for i in range(24)]
        print("\t:: Plotting graph for usage by hour")
        with open(self.report_path + "HitsPerHour.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            Y[int(parts[0])] = int(parts[1].replace('\n', ''))
        self.printBarChart(X, Y, "Hits per Hour", "Hour", "Hits", len(X), None)

    def plotBrowsers(self):
        X = []
        Y = []
        print("\t:: Plotting graph for browser usage")
        with open(self.report_path + "Browser.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            X.append(parts[0])
            Y.append(int(parts[1].replace('\n', '')))
        self.printPieChart(X, Y, "Used Browsers", len(X), (12, 7.5))

    def plotWeeks(self):
        X = []
        Y = []
        print("\t:: Plotting graph for hits per month")
        with open(self.report_path + "HitsPerMonth.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            X.append(self.helpers.beatufiyMonth(parts[0]))
            Y.append(int(parts[1].replace('\n', '')))
        self.printBarChart(X, Y, "Hits per Month", "Month", "Hits", len(X), (20, 10))

    def plotEndpoints(self):
        X = []
        Y = []
        print("\t:: Plotting graph for endpoint usage")
        with open(self.report_path + "HitsPerEndpoint.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            X.append(parts[0])
            Y.append(int(parts[1].replace('\n', '')))
        self.printPieChart(X, Y, "Used Endpoints (Top 10)", 10, (12, 7.5))

    def plotHTTPCodes(self):
        X = []
        Y = []
        print("\t:: Plotting graph for HTTP statuscodes")
        with open(self.report_path + "HttpCodeHits.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            parts = entry.split('\t')
            X.append(parts[0])
            Y.append(int(parts[1].replace('\n', '')))
        self.printPieChart(X, Y, "HTTP Statuscodes", len(X), (12, 7.5))

    def plotOS(self):
        X = []
        Y = []
        print("\t:: Plotting graph for OS usage")
        with open(self.report_path + "OS.txt", "r", encoding=self.encoding) as input_file:
            data = input_file.readlines()[2:]
        for entry in data:
            if not entry.startswith('\t'):
                parts = entry.split('\t')
                X.append(parts[0])
                Y.append(int(parts[1].replace('\n', '')))
        self.printPieChart(X, Y, "Operatingsystems", len(X), (12, 7.5))