import os
import re

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from py_modules.util import utils


def get_allure_title(own_markers):
    for marker in own_markers:
        if marker.name == "allure_title":
            return marker.args[0]


def get_test_id(headline):
    if "[" in headline:
        s = re.search("(?<=\[).+?(?=\])", headline)
        return s.group()
    return headline.split("_")[-2] + "-" + headline.split("_")[-1]


def get_error(error_text):
    global idx
    if error_text:
        lst = error_text.strip().split("\n")

        for i, x in enumerate(lst, 0):
            if x.strip().startswith("def"):
                idx = i
                break
        lst = lst[idx:]
        lst = lst[:lst.index("")]
        return "<br>".join(lst)
    return ""


class HTMLReport(object):

    def __init__(self):
        self.tests = []
        self.testName = "GeoSensorX"
        self.startTime = ""
        self.endTime = ""
        self.duration = ""

    def make_test_cases_table(self):
        table = ""
        for (result, own_markers, name) in self.tests:
            table += "<tr>"
            table += "<td>%s</td>" % get_test_id(result.head_line)
            table += "<td>%s</td>" % get_allure_title(own_markers)

            if result.outcome.upper() == "PASSED":
                table += "<td style='color:#84C830'><b>%s</b></td>" % result.outcome.upper()
            else:
                table += "<td style=\"color:#c90f24\"><b>%s</b></td>" % result.outcome.upper()

            # table += "<td style=\"text-align: left;word-break: break-all\"><code>%s</code></td>" % self.get_error(result.longreprtext)
            message = ""
            if result.longrepr is not None:
                message = result.longrepr.reprcrash.message

            table += "<td style=\"text-align: left;word-break: break-all\"><code>%s</code></td>" % message
            table += "<td>%s</td>" % utils.timedelta_to_string(result.duration)
            table += "</tr>"
        return table

    def parse_results_to_dict(self):
        rep = dict()
        rep["TEST_NAME"] = "GeoSensorX Automation Test"
        rep["TEST_CASES_TOTAL"] = len(self.tests)
        rep["TEST_CASES_PASSED"] = sum(1 for result in self.tests if result[0].passed)
        rep["TEST_CASES_FAILED"] = sum(1 for result in self.tests if result[0].failed)
        rep["TEST_CASES_FAILED_BY_BUG"] = 0
        rep["START_TIME"] = self.startTime
        rep["END_TIME"] = self.endTime
        rep["DURATION"] = utils.timedelta_to_string(self.duration)
        percent = 100 * rep["TEST_CASES_PASSED"]/float(rep["TEST_CASES_TOTAL"])
        rep["PASS_RATE"] = "%.2f %%" % percent
        rep["TEST_CASES_RESULTS_TABLE"] = self.make_test_cases_table()
        return rep

    def generate_overall_report(self, filename):
        current_directory = os.getcwd()
        env = Environment(loader=FileSystemLoader(current_directory))
        template = "resources/single-report-template.j2"
        result_dict = self.parse_results_to_dict()
        html = env.get_template(template).render(**result_dict)
        with open(filename, 'w') as f:
            f.write(html)
