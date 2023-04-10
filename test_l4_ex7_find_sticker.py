import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False

def test_example(driver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    is_element_present(driver, By.XPATH, "//div[@id='box-most-popular']//div[@class='name'][normalize-space()='Red Duck']//preceding::div[@title='New'][normalize-space()='New']")
    is_element_present(driver, By.XPATH, "//div[@id='box-most-popular']//div[@class='name'][normalize-space()='Green Duck']/..//div[@title='New'][normalize-space()='New']")
    is_element_present(driver, By.XPATH, "//div[@id='box-most-popular']//div[@class='name'][normalize-space()='Blue Duck']/..//div[@title='New'][normalize-space()='New']")
    is_element_present(driver, By.XPATH, "//div[@id='box-most-popular']//div[@class='name'][normalize-space()='Purple Duck']/..//div[@title='New'][normalize-space()='New']")
    is_element_present(driver, By.XPATH, "//div[@id='box-most-popular']//div[@class='name'][normalize-space()='Yellow Duck']//preceding::div[@title='On Sale'][normalize-space()='Sale']")



