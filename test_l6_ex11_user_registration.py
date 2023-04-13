import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import fake
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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

    driver.find_element_by_xpath("//a[normalize-space()='New customers click here']").click()
    driver.find_element_by_css_selector("input[name='firstname']").send_keys(fake.first_name())
    driver.find_element_by_css_selector("input[name='lastname']").send_keys(fake.last_name())
    driver.find_element_by_css_selector("input[name='address1']").send_keys(fake.street_address())
    driver.find_element_by_css_selector("input[name='postcode']").send_keys(fake.postcode())
    driver.find_element_by_css_selector("input[name='city']").send_keys(fake.city())

    driver.find_element_by_css_selector("#select2-country_code-ij-container").click()

    element = driver.find_element_by_css_selector("#select2-country_code-ij-results")
    drp = Select(element)
    drp.select_by_index(2)

    driver.find_element_by_css_selector("input[name='email']").send_keys(user_email)
    driver.find_element_by_css_selector("input[name='phone']").send_keys(fake.phone_number())
    driver.find_element_by_css_selector("input[name='password']").send_keys(user_password)
    driver.find_element_by_css_selector("input[name='confirmed_password']").send_keys(user_password)
    driver.find_element_by_css_selector("button[name='create_account']").click()

    #Logout
    driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()

    driver.find_element_by_css_selector("input[name='email']").send_keys(user_email)
    driver.find_element_by_css_selector("input[name='password']").send_keys(user_password)
    driver.find_element_by_css_selector("button[name='login']").click();

