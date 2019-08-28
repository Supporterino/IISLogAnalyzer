from DB import DB_connection, LogEntry

db = DB_connection()
db.create_schema()
testlog = LogEntry(date="2019-02-14", time="05:54:15", s_ip="10.212.8.86", cs_method="GET", cs_uri_stem="/Anwendungs-Doku/IT/01_dok/bms/NetHelp/_contextIds.js", cs_uri_query="-", s_port="80", cs_username="-", c_ip="10.2015.9.94", user_agent="Mozilla/5.0+(Windows+NT+6.1;+WOW64;+Trident/7.0;+rv:11.0)+like+Gecko", sc_status="200", sc_substatus="0", sc_win32_status="0", cs_bytes="0", time_taken="15", timestamp="firsttry")
db.session.add(testlog)