from LogAnalyzer.DB import DB_connection, LogEntry
from LogAnalyzer.utils import Utils
from datetime import datetime
import os
import sys

# db = DB_connection()
# db.create_schema()
# testlog = LogEntry(date="2019-02-14", time="05:54:15", s_ip="10.212.8.86", cs_method="GET", cs_uri_stem="/Anwendungs-Doku/IT/01_dok/bms/NetHelp/_contextIds.js", cs_uri_query="-", s_port="80", cs_username="-", c_ip="10.2015.9.94", user_agent="Mozilla/5.0+(Windows+NT+6.1;+WOW64;+Trident/7.0;+rv:11.0)+like+Gecko", sc_status="200", sc_substatus="0", sc_win32_status="0", cs_bytes="0", time_taken="15", timestamp="firsttry")
# db.session.add(testlog)

# REAL application

utils = Utils()
db = DB_connection()

PATH = None
ENCODING = None
TIMESTAMP = datetime.now()


def configure(path):
    if utils.create_directorys():
        sys.exit("Place log files inside the input directory! ...")
    global PATH
    if os.path.isdir(path):
        print(":: Global path variable set to: '{}'".format(path))
        PATH = path
        utils.check_for_empty_folder(PATH)
        read_encoding()
        initialize_db()
    else:
        raise Exception("Given path is not a direcotry, <" + path + ">")


def read_encoding():
    global ENCODING
    ENCODING = utils.detect_encoding(PATH)['encoding']
    print(":: Encoding set to: '{}'".format(ENCODING))


def initialize_db():
    db.create_schema()


def run():
    global PATH, ENCODING, TIMESTAMP
    print(":: Running log analyses. Your timestamp for this run is: '{}'".format(TIMESTAMP))
    utils.load_files(PATH, ENCODING, db.session, TIMESTAMP)
