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
    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, ".dataTable tbody tr td:nth-child(3)"))
        WebDriverWait(driver, 3).until(element_present)
    except TimeoutException:
        print ('Timed out waiting for page to load')

    list_country = driver.find_elements(By.CSS_SELECTOR, ".dataTable tbody tr td:nth-child(3)")

    i=0
    while i<len(list_country):
        list_country[i].click()
        zone = driver.find_elements(By.CSS_SELECTOR, "[name *= zone_code]")
        zone_names = []
        for element in zone:
            zone_name = element.text
            zone_names.append(zone_name)

        print(zone_names)
        zone_names_actual = zone_names.copy()
        zone_names.sort()
        #Use zone_names.sort(reverse=True) for reverse sorting
        assert zone_names == zone_names_actual
        driver.back()

        print(list_country[i])
        i+=1












