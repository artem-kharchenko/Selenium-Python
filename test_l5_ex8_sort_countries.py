import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
#login to the admin page
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.implicitly_wait(3)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()

# go to Countries page
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, ".dataTable tbody tr td:nth-child(5)"))
        WebDriverWait(driver, 3).until(element_present)
    except TimeoutException:
        print ('Timed out waiting for page to load')

    list_country = driver.find_elements_by_css_selector(".dataTable tbody tr td:nth-child(5)")
    print(list_country)
    country_names = []
    for element in list_country:
        country_name = element.text
        country_names.append(country_name)

    print(country_names)
    country_names_actual = country_names.copy()
    country_names.sort()
    #Use country_names.sort(reverse=True) for reverse sorting
    assert country_names == country_names_actual








