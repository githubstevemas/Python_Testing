import time

from selenium import webdriver

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_and_purchase():

    driver = webdriver.Edge()
    driver.implicitly_wait(10)
    driver.get('http://127.0.0.1:5000')

    email_input = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys("john@simplylift.co")
    email_input.send_keys(Keys.RETURN)

    body_text = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "body"))
    ).text
    assert "Welcome, john@simplylift.co" in body_text

    time.sleep(6)

    driver.get('http://127.0.0.1:5000/book/Spring%20Festival/Simply%20Lift')

    places_input = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.NAME, "places"))
    )
    places_input.send_keys("8")
    places_input.send_keys(Keys.RETURN)

    body_text = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, "body"))
    ).text
    assert "Great-booking complete!" in body_text

    time.sleep(20)