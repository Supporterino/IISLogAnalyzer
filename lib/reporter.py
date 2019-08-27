# -*- coding: utf-8 -*-
import os
import base64

class Reporter:
    def __init__(self):
        """
        This function initializes the class with the right path for the report.
        """
        self.path = os.getcwd() + "/html_report/"
        self.graph_path = os.getcwd() + "/graphs/"

    @staticmethod
    def gen_main_heading(title):
        """
        This function generates the heading from the given input.
        :param title: Title.
        :return: HTML-String
        """
        return "<h1 class='main_heading'>{0}</h1>".format(title)

    @staticmethod
    def gen_chapter_heading(title):
        """
        This function generates a chapter heading from the given input.
        :param title: Title.
        :return: HTML-String
        """
        return "<h3 class='heading'>{0}</h3>".format(title)

    @staticmethod
    def gen_report(text, pic_src, alt):
        """
        This function generates a report block from the given input.
        :param text: Text for the report.
        :param src_pic: path to img.
        :param alt: alt text for img.
        :return: HTML-String
        """
        return "<div class='report'><p class='text'>{0}</p><img class='normal_img' src='{1}' alt='{2}'></div>".format(text, pic_src, alt)

    @staticmethod
    def gen_report_big(text, pic_src, alt):
        """
        This function generates a report block from the given input with larger image.
        :param text: Text for the report.
        :param src_pic: path to img.
        :param alt: alt text for img.
        :return: HTML-String
        """
        return "<div class='report'><p class='text'>{0}</p><img class='big_img' src='{1}' alt='{2}'></div>".format(text, pic_src, alt)

    @staticmethod
    def gen_definition(name, text):
        """
        This function generates a definition block from the given input.
        :param name: Name of the definied object.
        :param text: Definitiontext.
        :return: HTML-String
        """
        return "<div class='definition'><p class='defname'><b>{0}</b></p><span class='deftext'><i>{1}</i></span></div>".format(name, text)

    @staticmethod
    def gen_start():
        """
        This function create the starting part of the html document with the css in it.
        :return: HTML-String
        """
        return """<html><head><style>.main {width: 50%;margin-left: 25%;margin-right: 25%;margin-top: 0px;margin-bottom: 0px;background-color: #eeeeee;}.main_heading {text-align: center;color: #ff6c4f;}.normal_img {width: 75%;margin-left: 12.5%;margin-right: 12.5%;}.big_img {width: 95%;margin-left: 2.5%;margin-right: 2.5%;}.definition {background-color: #dedede;margin-left: 5px;margin-right: 5px;}.defname {margin: 5px;}.deftext {margin-left: 10px;}.heading {font-size: 125%;color: #ff6c4f;}.text {margin-left: 5px;}body {padding: 0px;margin: 0px;}</style></head><body><div class='main'>"""

    @staticmethod
    def gen_end():
        """
        This function create the ending part of the html document.
        :return: HTML-String
        """
        return "</div></body></html>"

    def write_html_doc(self):
        """
        This function writes the HTML report.
        """
        print(":: Combining charts into HTML report")
        text = self.gen_start()
        text += self.gen_main_heading("Log Auswertung")
        text += self.gen_chapter_heading("Begriffsdefinition")
        text += self.gen_definition("Hit", "Eine HTTP Anfrage an den IIS Server der Webanwendung.")
        text += self.gen_definition("Endpunkt", "Genaues Ziel, bzw. geladene Ressource, beim Aufrufen der Webanwendung/Webseite.")
        text += self.gen_definition("HTTP Statuscode", "Der Statuscode gibt die Art der Antwort des Servers an.")
        text += self.gen_chapter_heading("Nutzungsauswertungen nach Wochentagen")
        with open(self.graph_path + "Hits per Weekday.png", "rb") as img:
            img_string = base64.b64encode(img.read())
        text += self.gen_report("Auswertung des Logs über den gesamten Zeitraum. Aufteilung der Hits nach Wochentagen.", "data:image/png;base64," + img_string.decode('utf-8'), "Graph mit Hits pro Wochentag")
        text += self.gen_chapter_heading("Nutzungsauswertung nach Stunden")
        with open(self.graph_path + "Hits per Hour.png", "rb") as img:
            img_string = base64.b64encode(img.read())
        text += self.gen_report("Auswertung des Logs über den gesamten Zeitraum. Aufteilung der Hits nach Stunden.", "data:image/png;base64," + img_string.decode('utf-8'), "Graph mit Hits in Stundenaufteilung")
        text += self.gen_chapter_heading("Nutzungsauswertung nach Monate")
        with open(self.graph_path + "Hits per Month.png", "rb") as img:
            img_string = base64.b64encode(img.read())
        text += self.gen_report_big("Übersicht der Hits pro Monat über den gesamten Zeitraum des Logs.", "data:image/png;base64," + img_string.decode('utf-8'), "Graph mit Hits pro Monat")
        text += self.gen_chapter_heading("Auswertung der verwendeten Software")
        with open(self.graph_path + "Used Browsers.png", "rb") as img:
            img_string = base64.b64encode(img.read())
        text += self.gen_report_big("Übersicht der verwendeten Browser zum Öffnen der Anwendung.", "data:image/png;base64," + img_string.decode('utf-8'), "Übersicht der Browser")
        with open(self.graph_path + "Operatingsystems.png", "rb") as img:
            img_string = base64.b64encode(img.read())
        text += self.gen_report_big("Übersicht der Betriebssysteme der verbindenden Clients.", "data:image/png;base64," + img_string.decode('utf-8'), "Übersicht der Betriebssysteme")
        text += self.gen_chapter_heading("Übersicht der angesprochenen Endpunkt")
        with open(self.graph_path + "Used Endpoints (Top 10).png", "rb") as img:
            img_string = base64.b64encode(img.read())
        text += self.gen_report_big("Übericht über die am häufigsten aufgerufenen Einstiegspunkte in die Anwendung, sowie der geladenen Ressourcen. Die Übersicht zeigt nur die 10 meistgenutzten Endpunkte.", "data:image/png;base64," + img_string.decode('utf-8'), "Endpointübersicht")
        text += self.gen_chapter_heading("Auswertung HTTP Statuscodes")
        with open(self.graph_path + "HTTP Statuscodes.png", "rb") as img:
            img_string = base64.b64encode(img.read())
        text += self.gen_report_big("Übersicht der Statuscodes, die vom Server an die Clients gesendet wurden. Hierbei weisen einige Statuscodes auf bestimmte Aktionen des Servers hin. <br><b>HTTP Code 304</b> - Weiterleitung durch den Server <br><b>HTTP Code 206</b> - Dateidownload<br><b>HTTP Code 404</b> - Datei nicht vorhanden", "data:image/png;base64," + img_string.decode('utf-8'), "HTTP Statuscodes")
        text += self.gen_end()

        with open(self.path + "report.html", "w+") as output:
            output.write(text)
