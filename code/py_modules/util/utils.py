import shutil
import string
import uuid
import datetime
from tests.data import constants
from paramiko.util import PFilter
import logging
import os, sys
from core import root
import json
from py_modules.util import json_utils
import csv
import random
from datetime import timedelta
import time
from dateutil import parser


# import pytz


def get_file_name(extension='.png'):
    return str(uuid.uuid4()) + extension


def get_screenshot_path(extension='.png'):
    name = get_file_name(extension)
    if "win" in sys.platform:
        screenshotFile = os.path.join(os.path.abspath(root), constants.SCREENSHOT_FOLDER, name)
    else:
        screenshotFile = os.path.join(constants.SCREENSHOT_FOLDER, name)

    return screenshotFile, name


_pfilter = PFilter()


def logger():
    return get_logger("modules_utils")


def get_logger(name):
    logger = logging.getLogger(name)
    logger.addFilter(_pfilter)
    return logger


def current_str_datetime(fmt="%d-%b-%Y %H:%M:%S"):
    d = datetime.datetime.now()
    return d.strftime(fmt)


def current_str_date(fmt="%d-%b-%Y"):
    d = datetime.datetime.now()
    return d.strftime(fmt)


def timedelta_to_string(delta):
    hours, remainder = divmod(delta, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))


def capture_device_json_log(resp):
    end = resp.find("\n", resp.find("TRI:Decode"))
    start = resp.find("{", resp.find("TRI:Decode"), end)
    jsonLog = resp[start:end]

    return json.loads(jsonLog)

def to_json(resp):
    return json.loads(resp)


def capture_device_pid_value(resp):
    end = resp.find("\n", resp.find("pid"))
    start = resp.find(" ", resp.find("pid"), end)
    pid = resp[start:end]
    return pid.strip()


def convert_to_timestamp(date_string, fmt="%Y-%m-%d %H:%M:%S"):
    date_string = format_date(date_string, fmt=fmt)
    date = datetime.datetime.strptime(date_string, fmt)
    time_tuple = date.timetuple()
    timestamp = time.mktime(time_tuple)
    return int(timestamp)


def get_test_data(fol, filename):
    if "win" in sys.platform:
        dataFile = os.path.join(os.path.abspath(root), "tests", "data", "{}".format(fol), "{}.json".format(filename))
    else:
        dataFile = os.path.join("tests", "data", "{}".format(fol), "{}.json".format(filename))

    return json_utils.open_json_file(dataFile)


def get_geosensorx_resource_data(filename):
    if "win" in sys.platform:
        dataFile = os.path.join(os.path.abspath(root), "resources", "geosensorx", "{}.json".format(filename))
    else:
        dataFile = os.path.join("resources", "geosensorx", "{}.json".format(filename))

    return json_utils.open_json_file(dataFile)


def get_obd_protocol(protocol):
    return get_geosensorx_resource_data("obd-protocol")[protocol]


def is_list_ascending(lst, step=1):
    for idx in range(len(lst) - 1):
        if int(lst[idx]) > int(lst[idx + 1]) - step:
            return False
    return True


def read_test_data_from_csv(filename):
    test_data = []
    if "win" in sys.platform:
        dataFile = os.path.join(os.path.abspath(root), "tests", "data", "data-driven", "{}.csv".format(filename))
    else:
        dataFile = os.path.join("tests", "data", "data-driven", "{}.csv".format(filename))

    with open(dataFile) as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data)  # skip header row
        for row in data:
            test_data.append(row)
        return test_data


def get_report_commands():
    return get_geosensorx_resource_data("report-events")


def get_obd_pids():
    return get_geosensorx_resource_data("obd-pids")


def generate_events(size):
    reports = get_report_commands()
    dataList = []
    i = 0
    for i in range(size):
        report = random.choice(list(reports))
        dataList.append(report)
        i += 1
    return dataList


def format_date(date_time, fmt="%Y-%m-%d %H:%M:%S"):
    is_string = isinstance(date_time, str)
    if is_string == False:
        date_time = datetime.datetime.fromtimestamp(date_time).strftime(fmt)
    return date_time


def timestamp_handler(date_time, fmt="%Y-%m-%d %H:%M:%S", seconds=1):
    date_time = format_date(date_time, fmt=fmt)
    date_time = datetime.datetime.strptime(date_time, fmt) + timedelta(seconds=seconds)
    time = date_time.strftime(fmt)
    return convert_to_timestamp(time)


def hex_to_dec(value):
    return int(value, 16)


def convert_kph_to_mph(value):
    mph = 0.62
    return round(value * mph, 2)


# def convert_timezone(dt, tz1, tz2):
#     tz1 = pytz.timezone(tz1)
#     tz2 = pytz.timezone(tz2)
#
#     dt = datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
#     dt = tz1.localize(dt)
#     dt = dt.astimezone(tz2)
#     dt = dt.strftime("%Y-%m-%d %H:%M:%S")
#     return dt


def get_last_days(date=None, days_to_subtract=1, fmt="%Y-%m-%d"):
    if date is None:
        date = current_str_date(fmt)
    date = format_date(date, fmt=fmt)
    date = datetime.datetime.strptime(date, fmt) - timedelta(days=days_to_subtract)
    return date.strftime(fmt)


def get_last_hours(date_time=None, hours_to_subtract=1, fmt="%Y-%m-%d %H:%M:%S"):
    if date_time is None:
        date_time = current_str_datetime(fmt)
    date_time = format_date(date_time, fmt=fmt)
    date = datetime.datetime.strptime(date_time, fmt) - timedelta(hours=hours_to_subtract)
    return date.strftime(fmt)


def current_str_time(fmt="%H:%M"):
    d = datetime.datetime.now()
    return d.strftime(fmt)


def is_in_range(num, x, y):
    num = int(num)
    if x <= num <= y:
        return True
    else:
        return False


def round_fuel_level(value):
    value = float(value) * 100
    level = round(value)
    return int(level)


def round_fuel_rail_pressure(value):
    value = float(value)
    level = round(value)
    return int(level)


def is_correct_datetime_format(date_string, fmt):
    try:
        datetime.datetime.strptime(date_string, fmt).strftime(fmt)
        return True
    except ValueError:
        return False


def is_valid_datetime(date_string):
    try:
        parser.parse(date_string)
        return True
    except ValueError:
        return False


def are_timestamps_in_range(timestamps, start, end, fmt="%Y-%m-%d %H:%M:%S"):
    are_in_range = []
    is_int = isinstance(start, int)
    if is_int == False:
        start = convert_to_timestamp(start, fmt=fmt)
        end = convert_to_timestamp(end, fmt=fmt)

    for timestamp in timestamps:
        is_in_range = timestamp in range(start, end)
        if is_in_range is False:
            logger().info("%s is not in range %s to %s" % (timestamp, start, end))
        are_in_range.append(is_in_range)
    return all(i for i in are_in_range)


def generate_random_string(size=17, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def delete_file_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def move_file_to_folder(src_folder_path, dst_folder_path):
    src_files = os.listdir(src_folder_path)
    for file_name in src_files:
        shutil.move(os.path.join(src_folder_path, file_name), os.path.join(dst_folder_path, file_name))


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        logger().info("Create %s folder" % folder_path)
        os.makedirs(folder_path)
    else:
        pass


def get_current_test_name_from_setup():
    current_test = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0].split('[')[0]
    return current_test.replace(current_test[current_test.find("[")+1:current_test.find("]")+1], "")


def convert_duration_time_to_sec(duration_time):
    hour, min, sec = str(duration_time).split(':')
    total_sec = int(hour) * 3600 + int(min) * 60 + float(sec)
    return float(total_sec)


def calculate_average_response_time(list_response_time, loop):
    total_second = 0
    for sec in list_response_time:
        total_second += sec
    return float(format(total_second / loop, '.3f'))


def convert_hex_to_decimal(values):
    r = []
    for value in values:
        dec_value = int(value, base=16)
        r.append(dec_value)
    return r if len(r) > 1 else r[0]


def calculate_total_engine_hours(data_bytes):
    d0, d1, d2, d3 = convert_hex_to_decimal(data_bytes[:4])
    return (d0 + d1 * 0x100 + d2 * 0x10000 + d3 * 0x1000000) * 0.05


def calculate_total_fuel_used(data_bytes):
    d0, d1, d2, d3 = convert_hex_to_decimal(data_bytes[4:8])
    return (d0 + d1 * 0x100 + d2 * 0x10000 + d3 * 0x1000000) * 0.5
