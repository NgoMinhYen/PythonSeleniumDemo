Feature: DC400 RPC Multiple Devices
    #pytest .\test\step_defs\dc400_rpc_multiple_devices_step.py
    @testcase
    Scenario Outline: GSX-4298	User can set FCWS config for a device in RPC Multiple Devices
        Given Login GSX Cloud with email <email> and password <password>
        And Go to Dashboard groups > DC400 > RPC Multiple Devices DC400
        And Select an active Device <deviceID> on the DC400 devices list
        When Select 'config-set' on RPC Method Description list
        When Enter <parameters> on RPC parameters
        When Uncheck Clear selection after RPC
        When Click Send RPC button
        Then Verify RPC command response device: <deviceID>, parameters: <parameters>
        When Clear response history
        When Select 'config-get' on RPC Method Description list
        When Enter <params> on RPC parameters
        When Click Send RPC button
        Then Verify RPC command get response device: <deviceID>, params: <params>, value: <value>

        Examples:
            | email                              | password         | deviceID         | parameters | params | value |
            | phat.ngo+tenant-admin@logigear.com | Y9!ynp7GY-XHEKWN | 0203030521054073 | {"FCWS":3} | FCWS   | 3     |