from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
	
	''' base class to initialize the base page that will be called from all pages '''

	def __init__(self, driver, info):
		self.driver = driver
		self.info = info

class CurrentPage(BasePage):

	''' insert codes here to specify what to do with the Chrome driver at the implementation level '''

	def get_current_page_info(self):

		try: 
			books = self.driver.find_elements(By.CSS_SELECTOR, "ol > li")

			for book in books:

				# get book name
				book_name = book.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
				self.info["name"].append(book_name)

				# get book rating
				book_rating = book.find_element(By.CSS_SELECTOR, "article > p").get_attribute("class")
				self.info["rating"].append(book_rating)

				# get book price
				book_price = book.find_elements(By.CSS_SELECTOR, ".product_price > p")[0].text
				self.info["price"].append(book_price)

				# get book availability
				book_avail = book.find_elements(By.CSS_SELECTOR, ".product_price > p")[1].text
				self.info["avail"].append(book_avail)
		
		except Exception as e:
			print(e)

		finally:
			return self.info

	def click_next_button(self):
		
		try:
			element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'next')))
			element.click()

		except Exception as e:
			print("no more pages")
			raise

