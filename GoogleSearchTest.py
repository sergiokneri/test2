from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoogleSearchTest:
    driver = None

    def setup(self):
        # Create a new Firefox driver instance
        self.driver = webdriver.Firefox()

    def teardown(self):
        # Close the browser after running the tests
        self.driver.quit()

    def test_search(self):
        # Trigger a Google Search
        self.driver.get('http://www.google.com')
        searchElement = self.driver.find_element_by_name('q')
        searchElement.send_keys('6020 peaks')
        searchElement.submit()
        WebDriverWait(self.driver, 10).until(EC.title_contains('6020 peaks'))
