TRIAL TASK 

To install dependency use

pip install -r requrements.txt

also you need geckodriver to run tests using Firefox https://github.com/mozilla/geckodriver/releases

to run tests use

py.test test_github.py --html=report.html

Options

--browser - Choose browser to run tests