import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
import fake
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
#Go to the main page
    fake = Faker()
    user_email = fake.ascii_free_email()
    user_password = "welcome"
    driver.get("http://localhost:8080/litecart/en/")
    driver.implicitly_wait(3)

    i = 1
    while i < 4:
        driver.find_element_by_css_selector("#box-most-popular .shadow").click()
        print(i)
        i += 1
        if (driver.find_element_by_css_selector("select[name='options[Size]']").size()>0):
            driver.find_element_by_css_selector("select option").click()
        driver.find_element_by_css_selector("button[name='add_cart_product']").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.quantity")))
        driver.back()

    driver.find_element_by_css_selector("div#cart a.link").click()
    driver.find_element_by_css_selector("td.item")

    list_products = driver.find_elements_by_css_selector("td.item")
    for element in list_products:
        driver.find_element_by_css_selector("button[name='remove_cart_item']").click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.quantity")))

        wait.until(ExpectedConditions.numberOfElementsToBe(By.cssSelector("td.item"), i - 1))

