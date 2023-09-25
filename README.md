# Welcome to GeoSensorX's UIAutomation

Please follow below steps to setup your environment:

- Install anaconda https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html
- add anaconda to SYSTEM PATH
- Create new env by: conda create -n "uiautomation" python=3.11.5
- Activate "conda activate uiautomation"
- install the dependencies by: pip install -r .\requirements.txt
- Run test case: pytest -m "testcase" --disable-warnings --alluredir=allure-results
- Run allure report: allure serve allure-results