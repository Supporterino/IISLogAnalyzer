# IISLogAnalyzer

## Introduction

This analyzer uses IIS Logs, to create statistics as raw text files and as CSV files. Graphical statistics will be added in a later version, as of right now the analyzer has no dependencies.

## Reports

The following statistics are created by the analyzer in raw text and csv:

|report name|information|csv names|
|-----------|-----------|---------|
|Browser|A list of all browser communicating with the IIS and the amount of http request each browser has made|HitsPerBrowser|
|HitsPerDay|A list with all weekdays and the http request made at this day (whole period)|HitsPerDay|
|HitsPerEndpoint|A list of all endpoints targeted by clients and the request amount|HitsPerEndpoint|
|HitsPerHour|All hours and their http request amounts (whole period)|HitsPerHour|
|HitsPerMonth|A list with all months of the period and their http request during that time|HitsPerMonth|
|HTTPCode206|A list with months where HTTP 206 Codes happend. The amount of that code and which endpoint caused it|HTTP206HitsPerMonth|
|HTTPCodeHits|A list with the hitten HTTP codes and their amount|HitsPerHTTPCode|
|IpHits|Http requests per IP address|HitsPerIP|
|OS|A list of all operating systems hitting the IIS with their hit amounts|HitsPerOS|
|UsersPerMonth|A list of usages[^1] per month|UsagesPerMonth|

[^1]: A usage is defined as the time an IP address communicates with IIS, once a new IP address communicates, another usage is counted.
