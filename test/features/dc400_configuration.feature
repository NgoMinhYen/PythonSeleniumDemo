Feature: Test DC400 Configuration Page
    # @regression
    Scenario Outline: GSX-3529 - User can select Go to configuration option to go to Configuration page
        Given Login GSX Cloud with email <email> and password <password>
        When Go to Dashboard groups > DC400 > RPC Multiple Devices DC400
        When Search device with device id: <deviceID>
        Then Expected: Device: <deviceID> is displayed
        When Click (Go to configuration) icon in device item <deviceID>
        Then Device <deviceID> configuration page is displayed

        Examples:
            | email                              | password         | deviceID         |
            | phat.ngo+tenant-admin@logigear.com | Y9!ynp7GY-XHEKWN | 0203030521054073 |