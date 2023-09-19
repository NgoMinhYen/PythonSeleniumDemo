import types
import inspect
import logging
from py_modules.util import utils
from core import selenium
from allure_commons.types import AttachmentType
import allure

_failed_expectations = []
_is_first_call = dict()


def expect(expr, msg=None):
    global _failed_expectations, _is_first_call

    caller = inspect.stack()[1][3]
    if _is_first_call.get(caller, True):
        _failed_expectations = []
        _is_first_call[caller] = False

    if isinstance(expr, types.FunctionType):
        try:
            expr()
        except Exception as e:
            _log_failure(False, e)
    elif not expr:
        _log_failure(False, msg)


def expect_with_screenshot(expr, msg=None):
    global _failed_expectations, _is_first_call

    caller = inspect.stack()[1][3]
    if _is_first_call.get(caller, True):
        _failed_expectations = []
        _is_first_call[caller] = False

    if isinstance(expr, types.FunctionType):
        try:
            expr()
        except Exception as e:
            _log_failure(True, e)
    elif not expr:
        _log_failure(True, msg)


def _attach_screenshot():
    file_path, name = utils.get_screenshot_path()
    logging.info("Screen shot %s" % name)
    selenium.save_screenshot(file_path)
    allure.attach.file(source=file_path, name=name, attachment_type=AttachmentType.PNG)
    return name


def assert_all():
    if _failed_expectations:
        assert False, _report_failures()


def _log_failure(screenshot, msg=None):
    (file_path, line, func_name, context_list) = inspect.stack()[2][1:5]
    context = context_list[0]
    if screenshot:
        name = _attach_screenshot()
        _failed_expectations.append('Failed at %s:%s' % (
            file_path, line) + '", in %s()%s\n%s' %
                                    (func_name, ((
                                            '\n\t' + 'ErrorMessage:' + '\t%s' % msg)),
                                     context) + '\n\tScreenShot: \t%s' % name)
    else:
        _failed_expectations.append('Failed at %s:%s' % (
            file_path, line) + '", in %s()%s\n%s' %
                                    (func_name, ((
                                            '\n\t' + 'ErrorMessage:' + '\t%s' % msg)),
                                     context))


def _report_failures():
    global _failed_expectations
    if _failed_expectations:
        (file_path, line, func_name) = inspect.stack()[2][1:4]
        report = [
            'assert_all() called at"%s:%s"' % (
                file_path, line) + ' in %s()\n' % func_name,
            'Failed Expectations : %s\n' % len(_failed_expectations)]
        for i, failure in enumerate(_failed_expectations, start=1):
            report.append('%d: %s' % (i, failure))
        _failed_expectations = []
        return '\n'.join(report)
