# IISLogAnalyzer

## Note

The branch development holds the new version with a database implementation

## Introduction

This analyzer uses IIS Logs, to create statistics as raw text files and as CSV files. besides the mentioned text reports the analyzer also creates a directory called `graphs`, which stores a collection of charts created with `matplotlib`.

## Requirements

+ Python > 3.5 (Not tested with python 2.X)
+ matplotlib >= 3.1.1
+ Memory >= Logfiles size (A future version will probably migrate to a real db to remove this constrain)

## How to run

1. Execute the main.py once, to create the necessary directorys
2. Copy your logfiles inside the input folder
3. Execute main.py again
4. The raw text statistics are now inside the `reports` directory, the csvs inside `csvs` and inside the `output` directory is a file, which is the combination of all your logfiles

## Documentation

+ [Grapher](https://supporterino.github.io/IISLogAnalyzer/grapher.html)
+ [Analyzer](https://supporterino.github.io/IISLogAnalyzer/analyzer.html)
+ [Helpers](https://supporterino.github.io/IISLogAnalyzer/helpers.html)
+ [Writer](https://supporterino.github.io/IISLogAnalyzer/writer.html)
+ [Models](https://supporterino.github.io/IISLogAnalyzer/models.html)
+ [Reporter](https://supporterino.github.io/IISLogAnalyzer/reporter.html)

## Reports

The following statistics are created by the analyzer in raw text and csv:

|report name|information|csv names|chart|
|-----------|-----------|---------|---|
|Browser|A list of all browser communicating with the IIS and the amount of http request each browser has made|HitsPerBrowser| Yes
|HitsPerDay|A list with all weekdays and the http request made at this day (whole period)|HitsPerDay| Yes 
|HitsPerEndpoint|A list of all endpoints targeted by clients and the request amount|HitsPerEndpoint| Yes (Top 10)
|HitsPerHour|All hours and their http request amounts (whole period)|HitsPerHour| Yes
|HitsPerMonth|A list with all months of the period and their http request during that time|HitsPerMonth| Yes
|HTTPCode206|A list with months where HTTP 206 Codes happend. The amount of that code and which endpoint caused it|HTTP206HitsPerMonth| No
|HTTPCodeHits|A list with the hitten HTTP codes and their amount|HitsPerHTTPCode| Yes
|IpHits|Http requests per IP address|HitsPerIP| No
|OS|A list of all operating systems hitting the IIS with their hit amounts|HitsPerOS| Yes
|UsersPerMonth|A list of usages<sup>[1](#myfootnote1)</sup> per month|UsagesPerMonth| No

<a name="myfootnote1">1</a>: A usage is defined as the time an IP address communicates with IIS, once a new IP address communicates, another usage is counted.

## HTML Report

The directory `html_report` includes a `report.html` which includes most of the charts from the `graphs` directory with an basic explanation. The pictures are embedded as base64 strings inside the html file, which means the file can be moved without loosing content.


## Supported IIS formats

The script supports the following formats out of the box:

1. date, time, s_ip, cs_method, cs_uri_stem, cs_uri_query, s_port, cs_username, c_ip, user_agent, referer, sc_status, sc_substatus, sc_win32_status, cs_bytes, time_taken
2. date, time, s_ip, cs_method, cs_uri_stem, cs_uri_query, s_port, cs_username, c_ip, user_agent, referer, sc_status, sc_substatus, sc_win32_status, time_taken
3. date, time, s_ip, cs_method, cs_uri_stem, cs_uri_query, s_port, cs_username, c_ip, user_agent, sc_status, sc_substatus, sc_win32_status, time_taken

### Adding own formats

The analyzer uses a model to load a log entry. The model looks like this and is located in the `lib/models.py`:
```python
class Logentry:
    def __init__(self, date, time, s_ip, cs_method, cs_uri_stem, cs_uri_query, s_port, cs_username, c_ip, user_agent, referer, sc_status, sc_substatus, sc_win32_status, cs_bytes, time_taken):
        self.date = date
        self.time = time
        self.s_ip = s_ip
        self.cs_method = cs_method
        self.cs_uri_stem = cs_uri_stem
        self.cs_uri_query = cs_uri_query
        self.s_port = s_port
        self.cs_username = cs_username
        self.c_ip = c_ip
        self.user_agent = user_agent
        self.referer = referer
        self.sc_status = sc_status
        self.sc_substatus = sc_substatus
        self.sc_win32_status = sc_win32_status
        self.cs_bytes = cs_bytes
        self.time_taken = time_taken
```

The entrys are loaded with the following function in the `lib/helpers.py`:
```python
    def read_file(self, filepath):
        print(":: Loading File {}".format(filepath))
        entries = []
        with open(filepath, "r", encoding=self.encoding) as log_file:
            for line in log_file:
                data = line.split(" ")
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
```

If you have a logfile with a diffrent format, which uses the same or less fields as definded in the model, you can adjust the `read_file` method to load your logfile right. If your log uses diffrent fields as defined in the model, you have to adjust the model first and then the `read_file` method. 
