@web @duckduckgo
Feature: DuckDuckGo Web Browsing

	Scenario: Basic DuckDuckGo Search
		Given the DuckDuckGo home page is displayed
		When the user searches for "panda"
		Then results are shown for "panda"