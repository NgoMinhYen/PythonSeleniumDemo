#pytest .\test\step_defs\GSX-5340.py
Feature: The map is zoomed out
    Scenario: GSX-3529 - User can select Go to configuration option to go to Configuration page
        Given Login GSX Cloud with email 'phat.ngo+tenant-admin@logigear.com' and password 'Y9!ynp7GY-XHEKWN'
        When Go to Dashboard groups > DC400 > RPC Multiple Devices DC400
        When Search device with device id: '0203030521054067'
        Then Expected: Device: '0203030521054067' is displayed
        When Click (Go to configuration) icon in device item '0203030521054067'
        Then Device '0203030521054067' configuration page is displayed