import datetime
import os
from time import sleep

from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader

from py_modules.util import utils, json_utils

import matplotlib.pyplot as plt


class PerformanceTestHTMLReport(object):

    def __init__(self):
        self.tests = []
        self.testName = "GeoSensorX"
        self.startTime = ""
        self.endTime = ""
        self.duration = ""
        self.pathFile = "./abc.json"
        self.logger = utils.get_logger("GSX")

    def open_performance_test_result_json(self, path_file):
        result_json = json_utils.open_json_file(path_file)
        return result_json

    def get_testcases(self, result_json):
        return result_json["benchmarks"]

    def get_allure_title(self, testcase_name):
        for (result, own_markers, name) in self.tests:
            if (name[0:name.find("[")] == testcase_name) or (name == testcase_name):
                for marker in own_markers:
                    if marker.name == "allure_title":
                        return marker.args[0]

    def get_test_id(self, testcase_name):
        test_id = testcase_name.split("_")[-2] + "-" + testcase_name.split("_")[-1]

        if "[" in test_id:
            test_id = test_id[0:test_id.find("[")]

        return test_id

    def get_duration_time(self, testcase_name):
        for (result, own_markers, name) in self.tests:
            if name == testcase_name:
                return utils.timedelta_to_string(result.duration)

    def get_result(self, testcase_name):
        for (result, own_markers, name) in self.tests:
            if name == testcase_name:
                return result.outcome.upper()

    def get_message(self, testcase_name):
        message = ""
        for (result, own_markers, name) in self.tests:
            if name == testcase_name:
                if result.longrepr is not None:
                    message = result.longrepr.reprcrash.message
        return message

    def format_duration_time(self, execution_time_delta):
        (h, m, s) = str(execution_time_delta).split(':')
        s = format(float(s), '.3f') if "." in s else int(s)
        return "%s:%s:%s" % (h, m, s)

    def get_max_time_execution(self, arr_results):
        durations = []
        for test in arr_results:
            duration = test["duration"]
            durations.append(duration)

        max_time = max(durations)
        return self.format_duration_time(max_time)

    def get_min_time_execution(self, arr_results):
        durations = []
        for test in arr_results:
            duration = test["duration"]
            durations.append(duration)

        min_time = min(durations)
        return self.format_duration_time(min_time)

    def get_avg_time_execution(self, arr_results):
        durations = []
        for test in arr_results:
            duration = test["duration"]
            durations.append(self.parse_time(duration))

        # time_deltas = [durations[i - 1] + durations[i] for i in range(1, len(durations))]
        average_timedelta = sum(durations, datetime.timedelta(hours=0, minutes=0, seconds=0, microseconds=0)) / (
                    len(durations))
        return self.format_duration_time(average_timedelta)

    def parse_time(self, time_str):
        (h, m, s) = time_str.split(':')

        if "." in s:
            (s, f) = s.split(".")
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s), microseconds=int(f))
        else:
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        return d

    def make_test_cases_table(self, arr_results):
        table = ""
        for test in arr_results:

            testcase_name = test["test_name"]
            if "[" in testcase_name:
                attempt = int(testcase_name[testcase_name.find("[") + 1:len(testcase_name) - 1]) + 1
            else:
                attempt = 1

            # title = self.get_allure_title(testcase_name)
            # title = testcase_name[0:testcase_name.find("[")]
            run_time = test["duration"]
            start_time = test["start_time"]
            note = test["message"]

            table += "<tr>"
            # table += "<td>%s</td>" % self.get_test_id(testcase_name)
            # table += "<td>%s</td>" % title
            table += "<td>%s</td>" % attempt
            table += "<td>%s</td>" % self.format_duration_time(run_time)
            table += "<td>%s</td>" % start_time
            table += "<td>%s</td>" % note
            table += "</tr>"

        return table

    def make_multiple_test_cases_table(self, arr_results):
        table = ""
        for test in arr_results:

            testcase_name = test["test_name"]

            title = self.get_allure_title(testcase_name)
            max_time = test["max_time"]
            min_time = test["min_time"]
            avg_time = test["avg_time"]
            rounds = test["rounds"]
            single_report_name = "'./%s.html'" % testcase_name
            table += '<tr onclick="window.location=%s">' % single_report_name
            table += "<td>%s</td>" % self.get_test_id(testcase_name)
            table += "<td>%s</td>" % title
            table += "<td>%s</td>" % min_time
            table += "<td>%s</td>" % avg_time
            table += "<td>%s</td>" % max_time
            table += "<td>%s</td>" % rounds
            result = self.get_result(''.join([testcase_name, "[0]"]))
            if result == "PASSED":
                table += "<td style='color:#84C830'><b>%s</b></td>" % result
            else:
                table += "<td style=\"color:#c90f24\"><b>%s</b></td>" % result

            message = self.get_message(''.join([testcase_name, "[0]"]))
            table += "<td style=\"text-align: left;word-break: break-all\"><code>%s</code></td>" % message

            table += "</tr>"
        return table

    def parse_results_to_dict(self):
        path = "./performance_result/"
        result_folder_id = '[results]'
        folder_result = os.listdir(path)
        arr_file_path = []

        for folder_name in folder_result:
            if result_folder_id in folder_name:
                pass
            else:
                folder = dict()
                folder["name"] = folder_name
                folder["path"] = path + folder_name
                arr_file_path.append(folder)

        arr_rs = []
        total_passed = 0
        total_failed = 0
        for folder in arr_file_path:
            # Delete all file in the source result folder
            utils.delete_file_in_folder(folder["path"])
            # Move all result file to the source result folder to generate HTML report
            utils.move_file_to_folder(folder["path"] + "[results]", folder["path"])

            rs = dict()
            arr_results = self.get_all_results_of_test_case(folder["path"])
            rs["test_name"] = folder["name"]
            rs["max_time"] = self.get_max_time_execution(arr_results)
            rs["min_time"] = self.get_min_time_execution(arr_results)
            rs["avg_time"] = self.get_avg_time_execution(arr_results)
            rs["rounds"] = len(arr_results)
            result = self.get_result(''.join([rs["test_name"], "[0]"]))
            if result == "PASSED":
                total_passed += 1
            else:
                total_failed += 1
            arr_rs.append(rs)

        rep = dict()
        rep["TEST_NAME"] = "GeoSensorX_Automation_Test"
        rep["TEST_CASES_TOTAL"] = len(arr_file_path)
        rep["START_TIME"] = self.startTime
        rep["END_TIME"] = self.endTime
        rep["DURATION"] = utils.timedelta_to_string(self.duration)
        rep["TEST_CASES_RESULTS_TABLE"] = self.make_multiple_test_cases_table(arr_rs)

        result_folder_path = os.path.join(os.path.abspath("./html_reports"), ''.join([rep["TEST_NAME"], '.png']))
        rep["PIE_CHART_PERFORMANCE_RESULT"] = result_folder_path
        self.create_pie_chart_for_multiple_report(total_passed, total_failed, result_folder_path)
        return rep

    def get_duration_single_result(self, arr_results):
        sum = datetime.timedelta()
        for result in arr_results:
            i = result["duration"]
            (h, m, s) = str(i).split(':')

            if "." in s:
                (s, f) = s.split(".")
                d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s), microseconds=int(f))
            else:
                d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            sum += d
        return sum

    def get_start_time_single_result(self, arr_results):
        last_result = arr_results[0]
        start_time = last_result["start_time"]
        return start_time

    def get_end_time_single_result(self, arr_results):
        last_result = arr_results[len(arr_results) - 1]
        end_time = last_result["start_time"]
        return end_time

    def parse_sing_results_to_dict(self):
        result_folder_id = '[results]'
        path = "./performance_result/"
        folder_result = os.listdir(path)

        arr_file_path = []
        for folder_name in folder_result:
            if result_folder_id in folder_name:
                pass
            else:
                rs_file = dict()
                rs_file["name"] = folder_name
                rs_file["folder_path"] = path + folder_name
                arr_file_path.append(rs_file)

        arr_rep = []
        for file_path in arr_file_path:
            arr_results = self.get_all_results_of_test_case(file_path["folder_path"])

            rep = dict()
            total_passed = 0
            total_failed = 0

            # Get result data from Json file
            duration = self.get_duration_single_result(arr_results)
            max_time_execution = self.get_max_time_execution(arr_results)
            min_time_execution = self.get_min_time_execution(arr_results)
            avg_time_execution = self.get_avg_time_execution(arr_results)
            for result in self.tests:
                test_name = result[2]
                if "[" in test_name:
                    test_name = test_name[0:test_name.find("[")]

                if test_name == file_path["name"]:
                    if result[0].passed:
                        total_passed += 1

                    if result[0].failed:
                        total_failed += 1

            # Result data will display on 'single-performance-testing-report-template.j2'
            rep["REPORT_NAME"] = file_path["name"]
            title = self.get_allure_title(file_path["name"])
            rep["TEST_NAME"] = "%s" % title
            rep["TEST_CASES_TOTAL"] = len(arr_results)
            rep["TEST_CASES_PASSED"] = total_passed
            rep["TEST_CASES_FAILED"] = total_failed
            rep["TEST_CASES_FAILED_BY_BUG"] = 0
            rep["START_TIME"] = self.get_start_time_single_result(arr_results)
            rep["END_TIME"] = self.get_end_time_single_result(arr_results)
            rep["DURATION"] = self.format_duration_time(duration)
            rep["MAX_TIME_EXECUTION"] = max_time_execution
            rep["MIN_TIME_EXECUTION"] = min_time_execution
            rep["AVG_TIME_EXECUTION"] = avg_time_execution
            rep["ROUNDS"] = len(arr_results)
            percent = 100 * rep["TEST_CASES_PASSED"] / float(rep["TEST_CASES_TOTAL"])
            rep["PASS_RATE"] = "%.2f %%" % percent
            rep["TEST_CASES_RESULTS_TABLE"] = self.make_test_cases_table(arr_results)
            arr_rep.append(rep)

        return arr_rep

    def create_pie_chart_for_multiple_report(self, total_passed, total_failed, result_folder_path):
        # Data to plot
        labels = 'Passed', 'Failed'
        sizes = [total_passed, total_failed]
        colors = ["#84C830", "#b10d20"]
        # explode = (0.1, 0)  # explode 1st slice

        # Plot
        # plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        #         autopct='%1.1f%%', shadow=True, startangle=140)

        plt.pie(sizes, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        # Save chart image to "./html_reports" folder
        plt.savefig(result_folder_path, transparent=True)

    def generate_report(self, filename):
        current_directory = os.getcwd()
        env = Environment(loader=FileSystemLoader(current_directory))
        report_template = "resources/performance-testing-report-template.j2"
        single_report_template = "resources/single-performance-testing-report-template.j2"
        # Generate multiple report
        result_dict = self.parse_results_to_dict()
        report_html = env.get_template(report_template).render(**result_dict)
        file_name = "./html_reports/%s.html" % filename
        with open(file_name, 'w') as f:
            f.write(report_html)

        # Generate single report
        result_dicts = self.parse_sing_results_to_dict()
        for result_dict in result_dicts:
            html = env.get_template(single_report_template).render(**result_dict)
            file_name = "./html_reports/%s.html" % (result_dict["REPORT_NAME"])

            with open(file_name, 'w') as f:
                f.write(html)

    def get_all_results_of_test_case(self, result_folder):
        arr_results = []
        files_path = [os.path.abspath(result_folder + "/" + x) for x in os.listdir(result_folder)]
        for file_name in files_path:
            str_json = json_utils.open_json_file(file_name)
            arr_results.append(str_json)
        return arr_results
