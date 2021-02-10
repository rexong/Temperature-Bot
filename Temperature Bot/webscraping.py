from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import xPath
import os

# Set the Chrome Options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")


class myTemperatureBot(object):
    def __init__(self):
        # temperature taking site
        self.URL = "https://temptaking.ado.sg/group/b24b3fa41017a5faab1d2a956962f724"
        # my pin to authenticate that it is me
        self.pin = "1304"

    def setUp(self):  # open up the browser and put my name in
        # set driver to the chrome webdriver path
        self.driver = webdriver.Chrome(executable_path=os.environ.get(
            "CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        self.driver.get(self.URL)
        print("[Page Loading Up]")
        self.getName()
        print("[Getting Name] P1 H W ONG ")

    def tearDown(self):  # close the whole window
        self.driver.quit()
        print("[Page Closed]")

    def getName(self):  # select the name dropdown box and put my name in
        self.name_field = Select(self.driver.find_element_by_id(
            'member-select'))  # get to the name field box
        # put my name in the dropdown box
        self.name_field.select_by_value("506188")

    def setPin(self, startLetter):  # input the 4 digit pin
        for i in range(1, 5):
            pin_input = self.driver.find_element_by_id(
                startLetter + "ep" + str(i))  # startLetter means the extra h in history id
            pin_input.send_keys(self.pin[i-1])
        print("[Pin Entered]")

    def setTemperature(self, temp):  # input the randomise temperature
        for i in range(1, 4):
            temp_input = self.driver.find_element_by_id("td" + str(i))
            temp_input.send_keys(str(temp)[i-1])
        print(f"[Temperature Set] {temp}")

    def checkHistory(self):  # see the history records
        self.historyBtn = self.driver.find_element_by_id(
            "member-history-btn")  # get the history btn
        done = False
        while not done:
            self.historyBtn.click()
            print("[History Page Loading Up]")
            self.driver.implicitly_wait(10)  # wait for the new page to load up
            self.setPin("h")  # enter the pin
            self.authenticateBtn = self.driver.find_element_by_xpath(
                xPath.xPath_AuthenticateBtn())  # get the authenticate btn
            self.authenticateBtn.click()
            print("[Authenticating Pin]")
            try:
                done = False
                # wait for the new page to load up
                self.driver.implicitly_wait(2)
                print("[Pin Authenticated]")
                self.firstRow = []  # init a list [date,AM,PM] to add the info from the first line of table
                # get xPath for the table's first row from xPath.py
                self.dateNtimeTempList = xPath.xPath_dateNtimeTemp()
                # get the inner value of the tags using get_att("innerHTML")
                for i in range(len(self.dateNtimeTempList)):
                    self.firstRow.append(self.driver.find_element_by_xpath(
                        self.dateNtimeTempList[i]).get_attribute("innerHTML"))
                print("[First Row Retrieved]")
                self.closeBtn2 = self.driver.find_element_by_xpath(
                    xPath.xPath_CloseBtn2())
                self.closeBtn2.click()
                print("[History Page Closed]")
                return self.firstRow
            except NoSuchElementException as error:
                print(f"[Error] {error}")
                self.closeBtn1 = self.driver.find_element_by_xpath(
                    xPath.xPath_CloseBtn1())
                self.closeBtn1.click()

    def activateSubmitBtn(self):  # click the submit btn
        self.submitBtn = self.driver.find_element_by_xpath(
            xPath.xPath_SubmitBtn())
        self.submitBtn.click()
        print("[Submitting...]")

    def activateConfirmBtn(self):
        self.confirmBtn = self.driver.find_element_by_xpath(
            xPath.xPath_ConfirmBtn())
        self.confirmBtn.click()
        print("[Confirming...]")
