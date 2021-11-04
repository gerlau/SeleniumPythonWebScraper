# Installation Guide
1. [pip command](#pip)
2. [Chrome Web-Driver](#chrome-web-driver)
3. [Selenium in Python](#selenium)

# pip command <a name="pip"></a>

1. Download Python https://www.python.org/downloads/ and remember to check “Add Python to Path”
2. Finally, check by running pip on your command line interface session

![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/pip-download.png?raw=true)
![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/pip-command.png?raw=true)

> Note: this is how you can use it e.g., pip install pandas

# Chrome Web-Driver <a name="chrome-web-driver"></a>

> Note: Assuming that you have already downloaded the Chrome browser on your machine.

1.	Find out the version of your Chrome browser
2.	Download the same version for your Chrome Web-Driver from https://sites.google.com/chromium.org/driver/getting-started?authuser=0 
3.	Download the zip folder that corresponds to your machine operating system
4.	Finally, extract the downloaded zip folder, copy the application file, and paste it in C:\Program Files (x86)

![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/browser-version.png?raw=true)
![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/web-driver-download.png?raw=true)
![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/web-driver-zip.png?raw=true)
![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/web-driver-application.png?raw=true)


# Selenium in Python <a name="selenium"></a>

> For more information: https://selenium-python.readthedocs.io/ 

> Note: Assuming that pip command is already usable on command line interface.

1. Run a command line interface session
2. Execute the command, pip install selenium
3. Run the following python file and verify the output with the following

![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/selenium-running.png?raw=true)

> Note: if you encounter the following warning, include the module Service and replace the argument in webdriver.Chrome()

1. from selenium.webdriver.chrome.service import Service
2. webdriver.Chrome(service=Service("C:\Program Files (x86)\chromedriver.exe"))

![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/selenium-warning.png?raw=true)
