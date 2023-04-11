import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


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
    except StaleElementReferenceException:
        return False
    else:
        print("Nothing went wrong")

def test_l4_ex6(driver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    driver.find_element_by_xpath("//span[normalize-space()='Appearence']").click()
    main_catalog_list = driver.find_element_by_id("box-apps-menu")
    items = main_catalog_list.find_elements_by_tag_name("li")
    print(f"items: {items}")
    for item in items:
        item.click()

        while is_element_present(driver, By.TAG_NAME, "ul"):
            second_catalog_list = driver.find_element_by_tag_name("ul")
            nums = second_catalog_list.find_elements_by_tag_name("li")
            print(f"nums: {nums}")
            for num in nums:
                num.click()