import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_l4_ex7(driver):
    driver.get("http://localhost:8080/litecart/en/")
    count = len(driver.find_elements(By.CSS_SELECTOR, ".product"))
    print(count)
    items = driver.find_elements(By.CSS_SELECTOR, ".product")

    i=0
    while i<count:
        sticker = len(items[i].find_elements(By.CSS_SELECTOR, ".sticker"))
        assert sticker == 1
        break
