Project description

“UI test automation framework for a demo login application using Python, Selenium, PyTest and POM.”

Project Overview

This framework automates UI tests for a demo login application:

https://practicetestautomation.com/practice-test-login/

It includes:

Clean and modular POM structure

Reusable BasePage with waits and actions

Centralized driver fixture via conftest.py

Detailed logging to console and log file

Positive and negative test scenarios

HTML reporting support

Easy to extend for additional pages and tests

How to run:

pip install -r requirements.txt
pytest -v
pytest -m smoke
pytest --html=report.html


Example test case:

“Valid login with correct credentials”

“Invalid login: wrong password”

“Invalid login: wrong username”