def assert_equal(actual, expected, error_message):
    assert (actual == expected), "%s, Actual: '%s' != Expected: '%s'" % (error_message, actual, expected)


def assert_true(actual, error_message):
    assert actual is True, "%s, Actual: '%s' != True" % (error_message, actual)


def assert_false(actual, error_message):
    assert actual is False, "%s, Actual: '%s' != False" % (error_message, actual)


def assert_greater_equal(actual, expected, error_message):
    assert (actual >= expected), "%s, Actual: '%s' < Expected: '%s'" % (error_message, actual, expected)

    
def assert_greater(actual, expected, error_message):
    assert (actual > expected), "%s, Actual: '%s' <= Expected: '%s'" % (error_message, actual, expected)


def assert_lesser_equal(actual, expected, error_message):
    assert (actual <= expected), "%s, Actual: '%s' > Expected: '%s'" % (error_message, actual, expected)

    
def assert_lesser(actual, expected, error_message):
    assert (actual < expected), "%s, Actual: '%s' >= Expected: '%s'" % (error_message, actual, expected)


def assert_in(actual, expected, error_message):
    assert (expected in actual), "%s, Actual: '%s' not in Expected: '%s'" % (error_message, actual, expected)


def assert_not_in(actual, expected, error_message):
    assert (expected not in actual), "%s, Actual: '%s' in Expected: '%s'" % (error_message, actual, expected)