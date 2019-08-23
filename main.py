from time import time

from lib.analyzer import Analyzer
from lib.helpers import Helpers
from lib.writer import Writer
from lib.grapher import Grapher
from lib.reporter import Reporter

ENCODING = "latin-1"
FILEFORMAT = ".log"


if __name__ == '__main__':
    print("Running Log Auswertung")
    start = time()

    helpers = Helpers(ENCODING, FILEFORMAT)
    helpers.create_directorys()
    analyzer = Analyzer(helpers)
    analyzer.run()
    grapher = Grapher(ENCODING, helpers)
    grapher.run()
    csv_writer = Writer(ENCODING, helpers)
    csv_writer.run_all()
    reporter = Reporter()
    reporter.write_html_doc()

    end = time() - start
    print("Prozess beendet: {:02.0f}:{:02.0f}:{:02.2f}".format(end // 3600, end % 3600 // 60, end % 60))
