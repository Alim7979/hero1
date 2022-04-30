from string import ascii_letters
from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class TestNewTask:

    def test_new_task(self):
        driver = webdriver.Chrome()
        driver.get("https://automate.securelink.com/")
        wait = WebDriverWait(driver, 10, 0.3)
        wait.until(ec.visibility_of_element_located((By.NAME, "username"))).send_keys("user")
        wait.until(ec.visibility_of_element_located((By.NAME, "password"))).send_keys("password")
        wait.until(
            ec.visibility_of_element_located((By.XPATH, "//div[@class='login-form']//button[@type='submit']"))).click()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME, "new-task"))).click()
        rand_text = "".join(choice(ascii_letters) for i in range(12))
        wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//div[@class='task-form-element']/input[@type='text']"))).send_keys(rand_text)
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[. ='Submit']"))).click()
        assert wait.until(ec.visibility_of_element_located((By.XPATH, "//*[. ='" + rand_text + "']")))
        driver.quit()
