import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def are_elements_present(driver, *args):
    return len(driver.find_elements(*args)) > 0

def test_l4_ex6(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

    count_litecart_menu = len(driver.find_elements(By.CSS_SELECTOR, "#app-"))
    print(count_litecart_menu)

    for i in range(count_litecart_menu):
        items = driver.find_elements(By.CSS_SELECTOR, "#app-")
        items[i].click()
        if (are_elements_present(driver, By.XPATH, "//li[contains(@id, 'doc-')]")):
            count_litecart_sub_menu = len(driver.find_elements(By.XPATH, "//li[contains(@id, 'doc-')]"))
            for j in range(count_litecart_sub_menu):
                sub_items = driver.find_elements(By.XPATH, "//li[contains(@id, 'doc-')]")
                sub_items[j].click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1")))