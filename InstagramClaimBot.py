from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

os.system("cls")

##########################

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

executable_path = os.path.join(ROOT_PATH, "chromedriver.exe")
emails = os.path.join(ROOT_PATH, "emails.txt")

site = "https://help.instagram.com/contact/606967319425038"

##########################

sleepfor = int(input("How long should the program sleep for in seconds: "))

fullname = input("Full Name: ")
instausername = input("Instagram Username: ")

phonenumber = input("Phone Number: ")
reason = input("Let us know why you're appealing: ")

chrome_options = ChromeOptions()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('log-level=3')
driver = webdriver.Chrome(executable_path, chrome_options=chrome_options)

while True:
	a = open(emails,"r").readlines()
	file = [s.rstrip()for s in a]
	for lines in file:
		email = lines.split()[0]

		driver.get(site)

		driver.find_element_by_xpath("//input[@name='name']").send_keys(fullname)
		driver.find_element_by_xpath("//input[@class='inputtext']").send_keys(instausername)
		driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
		driver.find_element_by_xpath("//input[contains(@name,'mobile_number')]").send_keys(phonenumber)
		driver.find_element_by_xpath("//textarea[contains(@name,'appeal_reason')]").send_keys(reason)
		driver.find_element_by_xpath("//button[@type='submit']").click()
		time.sleep(sleepfor)
		driver.refresh()

		print("Reported",email+"!")


	driver.close()
	exit()


