Feature: The map is zoomed out
        Scenario: User can zoom out by clicking on the "-" button on the Map Widget of the FMS Dashboard Driving Data page
            Given Login GSX Cloud
            When Go to Dashboard groups - DC400 - FMS Dashboard
            When Select any device in Landing page to go to Driving Data page
            When Select any device in Devices list of Driving Data page
            Then Click on "-" button on the map widget and verify the map is zoomed out
            
        


