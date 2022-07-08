from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
import time

class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()	
	def test_start_list_and_retrieve_it(self):
		self.browser.get(self.live_server_url)
		self.assertIn('E-Leksyon', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('E-LEKSYON', headerText)
		
	#VARIABLES
		inpName = self.browser.find_element_by_id('Firstname')
		btn_button = self.browser.find_element_by_id('button')
		self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
		inpName.click()
		inpName.send_keys('Jalalodin')
		time.sleep(1)

		inpMiddleName = self.browser.find_element_by_id('Middlename')
		inpMiddleName.click ()
		inpMiddleName.send_keys('Paguia')
		time.sleep (1)

		inpSurName = self.browser.find_element_by_id('Surname')
		inpSurName.click ()
		inpSurName.send_keys('Rascal')
		time.sleep(1)

		inpAge = self.browser.find_element_by_id('Age')
		inpAge.click ()
		inpAge.send_keys('17')
		time.sleep(1)

		inpRegVote1 = self.browser.find_element_by_id('Yes')
		inpRegVote1.click ()
		inpRegVote1.send_keys('Yes')
		time.sleep(1)

		inpChar= self.browser.find_element_by_id('What')
		inpChar.click ()
		inpChar.send_keys('Pogi')
		time.sleep(1)

		inpbasis = self.browser.find_element_by_id('basis')
		inpbasis.click ()
		inpbasis.send_keys('Television')
		time.sleep(1)

		inpPres = self.browser.find_element_by_id('Pres')
		inpPres.click ()
		inpPres.send_keys('Ping Lacson')
		time.sleep(1)

		inpVPres = self.browser.find_element_by_id('VPres')
		inpVPres.click ()
		inpVPres.send_keys('Vicente Sotto')
		time.sleep(1)

		self.browser.find_element_by_id('button').click()
#----------------------

		self.assertIn('E-Leksyon', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('E-LEKSYON', headerText)
		
		#VARIABLES
		inpName = self.browser.find_element_by_id('Firstname')
		btn_button = self.browser.find_element_by_id('button')
		self.assertEqual(inpName.get_attribute('placeholder'),'Enter your name here.')
		inpName.click()
		inpName.send_keys('Alemon')
		time.sleep(1)

		inpMiddleName = self.browser.find_element_by_id('Middlename')
		inpMiddleName.click ()
		inpMiddleName.send_keys('Daluma')
		time.sleep (1)

		inpSurName = self.browser.find_element_by_id('Surname')
		inpSurName.click ()
		inpSurName.send_keys('Lomabao')
		time.sleep(1)

		inpAge = self.browser.find_element_by_id('Age')
		inpAge.click ()
		inpAge.send_keys('20')
		time.sleep(1)

		inpRegVote1 = self.browser.find_element_by_id('Yes')
		inpRegVote1.click ()
		inpRegVote1.send_keys('No')
		time.sleep(1)

		inpChar= self.browser.find_element_by_id('What')
		inpChar.click ()
		inpChar.send_keys('Cute')
		time.sleep(1)

		inpbasis = self.browser.find_element_by_id('basis')
		inpbasis.click ()
		inpbasis.send_keys('Research')
		time.sleep(1)

		inpPres = self.browser.find_element_by_id('Pres')
		inpPres.click ()
		inpPres.send_keys('Ping Lacson')
		time.sleep(1)

		inpVPres = self.browser.find_element_by_id('VPres')
		inpVPres.click ()
		inpVPres.send_keys('Willie Ong')
		time.sleep(1)

		self.browser.find_element_by_id('button').click()

		table = self.browser.find_element_by_id('registryTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Jalalodin, Paguia, Rascal, Yes, Pogi, Television, Leni Robredo, Sara Inday Duterte', [row.text for row in rows])
		#self.assertIn('2: Alemon, Daluma, Lomabao, 26, Yes, Cute, Research, Isko Moreno, Willie Ong', [row.text for row in rows])


