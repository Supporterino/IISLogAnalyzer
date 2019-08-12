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
