import os
import json
from argparse import Namespace
from py_modules import util
from resources.general.general_enum import DateTimeFormat

def logger():
    return util.utils.get_logger("json_utils")


def parse_json_config_file(filename, outputType='object'):
    if not os.path.isfile(filename):
        print("configuration file does not exist: {!s}".format(filename))
        raise RuntimeError("configuration file does not exist: {!s}".format(filename))

    with open(filename) as f:
        if outputType == 'object':
            data = json.loads(f.read(), object_hook=lambda d: Namespace(**d))
        else:  # outputType == 'dict'
            data = json.loads(f.read())

    return data


def parse_geosensor_config_file(filename):
    data = parse_json_config_file(filename, "dict")
    if "json_write_config_file" in data:
        fName = "%s/%s" % (os.getcwd(), data["json_write_config_file"])
        data["json_write_config"] = parse_json_config_file(fName, 'dict')

    if "json_obd_simulator_config_file" in data:
        fName = "%s/%s" % (os.getcwd(), data["json_obd_simulator_config_file"])
        data["json_obd_simulator_config_file"] = parse_json_config_file(fName, 'dict')

    if "json_ftp_server_file" in data:
        fName = "%s/%s" % (os.getcwd(), data["json_ftp_server_file"])
        data["json_ftp_server"] = parse_json_config_file(fName, 'dict')

    return data


def is_json(myjson):
    try:
        _ = to_json(myjson)
    except ValueError:
        return False
    return True


def to_json(myjson):
    return json.loads(myjson)


def open_json_file(filename):
    with open(filename, "r") as f:
        strJson = f.read()

    return to_json(strJson)


def is_key_existed(jsonstring, key):
    dictionary = jsonstring
    if isinstance(dictionary, dict) is False:
        dictionary = to_json(jsonstring)
    value = dictionary.get(key)
    if value is not None:
        return True
    else:
        logger().info("{0} does not exist".format(key))
    return False


def are_keys_existed(jsonstring, fields):
    are_existed = []
    for field in fields:
        is_existed = is_key_existed(jsonstring, field)
        are_existed.append(is_existed)
    return all(i for i in are_existed)


def get_value(jsonstring, key):
    value = None
    try:
        dictionary = jsonstring
        if isinstance(dictionary, dict) is False:
            dictionary = to_json(jsonstring)
        value = dictionary.get(key)
        return value
    except:
        return value


def get_values(jsonstring, key, is_timestamp=False):
    values = []
    try:
        dictionary = jsonstring
        if isinstance(dictionary, dict) is False:
            dictionary = to_json(jsonstring)
        for item in dictionary:
            value = item.get(key)
            if is_timestamp:
                value = util.utils.convert_to_timestamp(value, fmt=DateTimeFormat.ISO8601.value)
            values.append(item.get(key))
        return values
    except:
        return values


def compare_keys(json_a, json_b):
    if isinstance(json_a, dict) is False:
        json_a = to_json(json_a)
    if isinstance(json_b, dict) is False:
        json_b = to_json(json_b)
    # Compare all keys
    for key in json_a.keys():
        # if key exist in json2:
        if key in json_b.keys():
            # If subjson
            if type(json_a[key]) == dict:
                compare_keys(json_a[key], json_b[key])
        else:
            logger().info("Found new key: %r" % key)
            return False
    return True


def compare(json_a, json_b):
    if isinstance(json_a, dict) is False:
        json_a = to_json(json_a)
    if isinstance(json_b, dict) is False:
        json_b = to_json(json_b)

    # Compare all keys
    for key in json_a.keys():
        # if key exist in json2:
        if key in json_b.keys():
            # If subjson
            if type(json_a[key]) == dict:
                compare_keys(json_a[key], json_b[key])
            else:
                if json_a[key] != json_b[key]:
                    logger().info("These entries are different:")
                    logger().info(json_a[key])
                    logger().info(json_b[key])
                    return False
        else:
            logger().info("Found new key: %r" % key)
            return False
    return True


def dumps(json_string):
    return json.dumps(json_string)


def write_json_file_in_folder(json_data, file_name, folder_path):
    full_file_name = ''.join([file_name, ".json"])
    logger().info("Write result to %s file" % full_file_name)
    with open(os.path.join(folder_path, full_file_name), 'w') as outfile:
        outfile.write(json_data)

