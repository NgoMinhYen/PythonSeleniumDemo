Feature: DC400 RPC Multiple Devices

    Scenario: GSX-4298	User can set FCWS config for a device in RPC Multiple Devices
        Given Given Login GSX Cloud
        # And Login with username "phat.ngo+tenant-admin@logigear.com", password "Y9!ynp7GY-XHEKWN"
        # And Go to Dashboard groups > DC400 > RPC Multiple Devices DC400
        # And Select an active Device "0203030521054073" on the DC400 devices list
        # When Select "config-set" on RPC Method Description list
        # When Enter "{\"FCWS\":3}" on RPC parameters
        # And Uncheck Clear selection after RPC ?
        # When Click Send RPC button
        # Then Verify RPC command response device: "0203030521054073", parameters: "{\"FCWS\":3}"
        # When Clear response history
        # When Select "config-get" on RPC Method Description list
        # When Enter "FCWS" on RPC parameters
        # When Click Send RPC button
        # Then Verify RPC command get response device: "0203030521054073", params: "FCWS", value: "3"