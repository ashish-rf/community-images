"""The selenium test."""
# pylint: skip-file

# Generated by Selenium IDE
import json  # pylint: disable=import-error disable=unused-import
import time  # pylint: disable=import-error disable=unused-import
import pytest  # pylint: disable=import-error disable=unused-import
from selenium import webdriver  # pylint: disable=import-error
from selenium.webdriver.chrome.options import Options  # pylint: disable=import-error
from selenium.webdriver.common.by import By  # pylint: disable=import-error
from selenium.webdriver.common.action_chains import ActionChains  # pylint: disable=import-error disable=unused-import
from selenium.webdriver.support import expected_conditions  # pylint: disable=import-error disable=unused-import
from selenium.webdriver.support.wait import WebDriverWait  # pylint: disable=import-error disable=unused-import
from selenium.webdriver.common.keys import Keys  # pylint: disable=import-error disable=unused-import
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # pylint: disable=import-error disable=unused-import

class TestNewproject():
    """The test word press class for testing wordpress image."""

    def setup_method(self):
        """setup method."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(
            options=chrome_options)  # pylint: disable=attribute-defined-outside-init
        self.driver.implicitly_wait(10)

    def teardown_method(self, method):  # pylint: disable=unused-argument
        """teardown method."""
        self.driver.quit()

    def test_newproject(self, params):
      # Test name: new_project
      # Step # | name | target | value
      # 1 | open | /users/sign_in | 
      self.driver.get(
            "https://{}:{}/users/sign_in".format(
                params["server"],
                params["port"]))  # pylint: disable=consider-using-f-string
      # 2 | setWindowSize | 1920x1080 | 
      self.driver.set_window_size(1920, 1080)
      # 3 | click | id=user_login | 
      self.driver.find_element(By.ID, "user_login").click()
      # 4 | type | id=user_login | root
      self.driver.find_element(By.ID, "user_login").send_keys("root")
      # 5 | click | id=user_password | 
      self.driver.find_element(By.ID, "user_password").click()
      # 6 | type | id=user_password | adminadmin
      self.driver.find_element(By.ID, "user_password").send_keys("adminadmin")
      # 7 | click | name=button | 
      self.driver.find_element(By.NAME, "button").click()
      # 8 | click | linkText=New project | 
      self.driver.find_element(By.LINK_TEXT, "New project").click()
      # 9 | click | css=.new-namespace-panel-wrapper:nth-child(1) .gl-text-gray-900 | 
      self.driver.find_element(By.CSS_SELECTOR, ".new-namespace-panel-wrapper:nth-child(1) .gl-text-gray-900").click()
      # 10 | click | id=project_name | 
      self.driver.find_element(By.ID, "project_name").click()
      # 11 | type | id=project_name | testing1
      self.driver.find_element(By.ID, "project_name").send_keys("testing1")
      # 12 | click | css=.form-group:nth-child(6) .gl-form-radio:nth-child(3) > .custom-control-label | 
      self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(6) .gl-form-radio:nth-child(3) > .custom-control-label").click()
      # 13 | click | name=commit | 
      self.driver.find_element(By.NAME, "commit").click()
      # 14 | click | css=.float-left:nth-child(3) | 
      self.driver.find_element(By.CSS_SELECTOR, ".float-left:nth-child(3)").click()
      # 15 | click | css=.qa-new-file-option .gl-new-dropdown-item-text-wrapper | 
      self.driver.find_element(By.CSS_SELECTOR, ".qa-new-file-option .gl-new-dropdown-item-text-wrapper").click()
      # 16 | click | id=file_name | 
      self.driver.find_element(By.ID, "file_name").click()
      # 17 | type | id=file_name | test.txt
      self.driver.find_element(By.ID, "file_name").send_keys("test.txt")
      # 18 | click | css=.view-lines | 
      self.driver.find_element(By.CSS_SELECTOR, ".view-lines").click()
      # 19 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")
      # 20 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")
      # 21 | runScript | window.scrollTo(0,0) | 
      self.driver.execute_script("window.scrollTo(0,0)")
      # 22 | type | css=.inputarea | this is a simple text file
      self.driver.find_element(By.CSS_SELECTOR, ".inputarea").send_keys("this is a simple text file")
      # 23 | click | id=commit_message-95a74a3d27aaf99dc6e64a2d6f53307f | 
      self.driver.find_element(By.ID, "commit_message-95a74a3d27aaf99dc6e64a2d6f53307f").click()
      # 24 | click | id=branch_name | 
      self.driver.find_element(By.ID, "branch_name").click()
      # 25 | click | css=#commit-changes > .gl-button-text | 
      self.driver.find_element(By.CSS_SELECTOR, "#commit-changes > .gl-button-text").click()
      # 26 | click | css=#js-onboarding-commits-link > span | 
      self.driver.find_element(By.CSS_SELECTOR, "#js-onboarding-commits-link > span").click()
    