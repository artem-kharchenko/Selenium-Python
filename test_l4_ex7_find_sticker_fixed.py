import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_l4_ex7(driver):
    driver.get("http://localhost:8080/litecart/en/")
    box_most_popular = driver.find_element_by_xpath("//div[@id='box-most-popular']")
    items = box_most_popular.find_elements_by_tag_name("li")
    for item in items:

        if driver.find_element_by_xpath("//div[@id='box-most-popular']//div[contains(@class, 'sticker')]"):
            print("Sticker exists")
        else:
            print("No stickers found")

    box_campaigns = driver.find_element_by_xpath("//div[@id='box-campaigns']")
    iboxes = box_campaigns.find_elements_by_tag_name("li")
    for ibox in iboxes:

        if driver.find_element_by_xpath("//div[@id='box-campaigns']//div[contains(@class, 'sticker')]"):
            print("Sticker exists")
        else:
            print("No stickers found")

    box_latest_products = driver.find_element_by_xpath("//div[@id='box-latest-products']")
    inames = box_latest_products.find_elements_by_tag_name("li")
    for iname in inames:

        if driver.find_element_by_xpath("//div[@id='box-latest-products']//div[contains(@class, 'sticker')]"):
            print("Sticker exists")
        else:
            print("No stickers found")