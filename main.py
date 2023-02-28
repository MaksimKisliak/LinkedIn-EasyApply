from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import Chrome
import os
from dotenv import load_dotenv
import logging


class LinkedInJobApply:
    LOGIN_URL = 'https://www.linkedin.com/login'
    JOB_SEARCH_URL = \
        'https://www.linkedin.com/jobs/search/?currentJobId=3477736514&geoId=105072130&keywords=python%20web%20developer&location=Poland&refresh=true'
    LOGIN_USERNAME_XPATH = '//input[@id="username"]'
    LOGIN_PASSWORD_XPATH = '//input[@id="password"]'
    LOGIN_BUTTON_XPATH = '//button[contains(text(),"Sign in")]'

    def __init__(self):
        """
        Constructor method to initialize class variables
        """
        if "RAILWAY_ENVIRONMENT" in os.environ:
            # Check if the script is running on the Railway platform
            user_name = os.environ.get("USER_NAME")
            password = os.environ.get("PASSWORD")
        else:
            # Load from local .env
            load_dotenv()
            user_name = os.environ.get("USER_NAME")
            password = os.environ.get("PASSWORD")

        # Store credentials and create Selenium driver
        self.username = user_name
        self.password = password
        self.driver = Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.phone = "1234567891"
        self.main_window_id = None

    def login(self):
        """
        Method to log in to LinkedIn account
        """
        self.driver.maximize_window()
        self.driver.get(self.LOGIN_URL)
        # Accept cookies
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "artdeco-global-alert__action"))).click()
            logging.info(f"Cookies accepted.")
        except Exception as e:
            logging.info(f"Cookies button not found. {e}")
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.LOGIN_USERNAME_XPATH))).send_keys(self.username)
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.LOGIN_PASSWORD_XPATH))).send_keys(self.password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.LOGIN_BUTTON_XPATH))).click()
        self.wait.until(EC.url_changes(self.LOGIN_URL))

    def apply_to_job(self, job_element):
        """
        Method to apply for a single job

        :param job_element: WebElement: Job element to apply to
        """
        job_element.click()

        self.driver.switch_to.window(self.main_window_id)
        try:
            easy_apply_click = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.jobs-apply-button--top-card button')))
            easy_apply_click.click()
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fb-single-line-text input")))
            add_number = self.driver.find_element(By.CSS_SELECTOR, '.fb-single-line-text input')
            if add_number.get_attribute("value") == "":
                add_number.send_keys(self.phone)
            submit_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".justify-flex-end button .artdeco-button__text")))
            if submit_button.text == 'Submit application':
                submit_button.click()
                self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.artdeco-modal__dismiss svg')))
                click_cross = self.driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss svg')
                click_cross.click()
            else:
                back_button = self.driver.find_element(By.CSS_SELECTOR, '.artdeco-modal__dismiss')
                back_button.click()
                self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.artdeco-modal__actionbar--confirm-dialog span')))
                discard_button = self.driver.find_element(By.CSS_SELECTOR,
                                                          '.artdeco-modal__actionbar--confirm-dialog span')
                discard_button.click()
        except NoSuchElementException:
            pass
        finally:
            self.driver.switch_to.window(self.main_window_id)
            self.wait.until(EC.number_of_windows_to_be(1))

    def apply_to_all_jobs(self):
        """
        Method to apply to all jobs in the LinkedIn job search page
        """
        self.main_window_id = self.driver.current_window_handle
        self.driver.get(self.JOB_SEARCH_URL)
        self.wait.until(EC.url_contains("search"))
        jobs_block = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'scaffold-layout__list-container')))
        jobs_list = jobs_block.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
        for job in jobs_list:
            self.apply_to_job(job)

    def quit_driver(self):
        """
        Method to quit the Chrome driver
        """
        if self.driver:
            self.driver.quit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    job_applier = LinkedInJobApply()
    job_applier.login()
    job_applier.apply_to_all_jobs()
    job_applier.quit_driver()
