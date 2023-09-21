Feature: GSX-13874
        Scenario: The Internal LED Enable configuration will display with a blue background if the selected setting have been updated on the device\
            Given Login GSX Cloud
            When Go to Dashboard groups - DC400 - FMS Dashboard
            When Select any device then go to Configuration page
            When Select the Intrernal LED Enable configuration with a different value
            When Click the Set button
            #Then The Intrernal LED Enable configuration will display with a blue background