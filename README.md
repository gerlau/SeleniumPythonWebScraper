# What is this project about
![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/index-html.png?raw=true)
![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/out-csv.png?raw=true)

Learning how to scrape the web with Selenium in Python.
- Navigate thru each page
- Scrape the details of each book
- Store the extracted information and export it as .csv/.json

# What do we need to get started?
## Pre-requisites 
- Basic knowledge of HTML, CSS
- Basic knowledge of Python

## Installations
> Note: In this guide, we will be using ...
Sublime Text IDE, Chrome browser, and Windows 10 OS.

- pip command
- Chrome Web-Driver
- Selenium

# How did we do it?
1. Set up the Page Objects design pattern.

> setUp() : creates a WebDriver session for Chrome so that we can use it to navigate thru the website. 

> tearDown() : closes all the Chrome windows and terminates the WebDriver session.

```
import page
import unittest
from selenium import webdriver

class BooksSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(...)
        self.info = {...}
    
    def tearDown(self):
        self.driver.quit()
        
    def test_search_in_books(self):
        # actions to take with the webdriver
        
if __name__ == "__main__":
    unittest.main()
```
---
2. Include the high-level implementations for test_search_in_books()
- Each loop, if not main page, we will get a new URL 
- Each page.CurrentPage(...), we call the interactions that we have with CurrentPage class

> Note: The URL of the main page we are going into is https://books.toscrape.com/index.html. However, the subsequent pages follow the format, https://books.toscrape.com/catalogue/page-1.html

```
def test_search_in_books(self):

    pgCnt = 1 
	pgUrl = "https://books.toscrape.com/index.html"
	
	while pgCnt > 0:
    
		if pgCnt > 1: pgUrl = "https://books.toscrape.com/catalogue/page-" + str(pgCnt) + ".html"

		try:
		    self.driver.get(pgUrl)
		    current_page = page.CurrentPage(self.driver, self.info)
		    self.info = current_page.get_current_page_info()
		    current_page.click_next_button()
        
        except Exception as e:
		    print(e)
		    break

		finally:
		    pgCnt += 1

	df_info = pd.DataFrame(data=self.info)
	df_info.to_csv('../out.csv', index=False)
```
---
3. Include the interactions with the web pages
- Each page, we will try to find out all books' detail 
- Each page, we will try to find the next button
```
class BasePage(object):

	def __init__(self, driver):
	    self.driver = driver

class CurrentPage(BasePage):

    def get_current_page_info(self):
    
        try: 
            books = self.driver.find_elements(By.CSS_SELECTOR, "ol > li")

            for book in books:
				book_name = book.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
				self.info["name"].append(book_name)
		
		except Exception as e:
			print(e)

		finally:
			return self.info
    
    def click_next_button(self):
    
        try:
            element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, 'next')))
            element.click()
            
		except Exception as e:
		    print("no more pages")
		    raise
```
---
4. Finally, build and run main.py

> Note: This is the line that defines where the csv file will be generated to.

```
df_info.to_csv('../out.csv', index=False)
```
---
5. Extra: Include assert statements

> :bulb: Page Objects design pattern are used to create test cases. Remove line 46 & 54 from main.py to try out the assert statement.

```
try:
	self.driver.get(pgUrl)
	self.assertEqual("All products | Books to Scrape - Sandbox", self.driver.title, "webpage title does not match")

except Exception as e:
	print(e)
```
![alt text](https://github.com/gerlau/SeleniumPythonWebScraper/blob/main/images/assert-result-example.png?raw=true)

# Acknowledgements
- https://books.toscrape.com/index.html
- https://selenium-python.readthedocs.io/page-objects.html
- https://www.selenium.dev/documentation/webdriver/locating_elements
