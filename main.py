import page
import time
import json
import pandas as pd
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BooksSearch(unittest.TestCase):

	"""

	- Assert statements should come here 
	- Business Logic here

	"""

	def setUp(self):

	    self.driver = webdriver.Chrome(service=Service("C:\Program Files (x86)\chromedriver.exe"))

	    ''' insert declaration of variables here to export extracted information '''

	    self.info = {
	    	"name"	:[],
	    	"rating":[],
	    	"price"	:[],
	    	"avail"	:[]
	    } 

	def tearDown(self):
		
		# time.sleep(10)
		
		# Close the window that has focus	- driver.close() 
		# Close the browser 				- driver.quit() 
		self.driver.quit()

	def test_search_in_books(self):

		''' insert codes here to specify what to do with the Chrome driver at a high level '''

		pgCnt = 1 
		pgUrl = "https://books.toscrape.com/index.html"

		''' remove line 46 & 54 to try out assertEqual

		try:
			self.driver.get(pgUrl)
			self.assertEqual("All products | Books to Scrape - Sandbox", self.driver.title, "webpage title does not match")

		except Exception as e:
			print(e)

		'''

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

		''' insert codes here to export extracted information '''

		# convert to export format - .csv 
		df_info = pd.DataFrame(data=self.info)
		df_info.to_csv('../out.csv', index=False)

		# convert to export format - .json 
		# df_info.to_json('../out.json', orient='index')

if __name__ == "__main__":
    unittest.main()