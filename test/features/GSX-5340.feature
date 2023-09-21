#pytest .\test\step_defs\GSX-5340.py
Feature: The map is zoomed out
        Scenario: User can zoom out by clicking on the "-" button on the Map Widget of the FMS Dashboard Driving Data page
            Given Login GSX Cloud
            When Go to Dashboard groups > DC400 > RPC Multiple Devices DC400
            When Select an active Device '0203030521054067' on the DC400 devices list
            When Select any device in Devices list of Driving Data page
            Then Click on "-" button on the map widget and verify the map is zoomed out
            
        


