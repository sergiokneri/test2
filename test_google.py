from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestGoogleSearchTest:
    driver = None
    
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-web-security')
        options.add_argument(
        '--disk-cache-dir=/var/www/cake2.2.4/app/tmp/cache/selenium-chrome-cache')
        options.add_argument('--no-referrers')
        options.add_argument(
        "'chrome.prefs': {'profile.managed_default_content_settings.images': 2}")

        self.driver = webdriver.Chrome(
            executable_path='/usr/local/bin/chromedriver',
            chrome_options=options)

    # def setup(self):
    #     options = webdriver.Firefox()
    #     options.add_argument('--disable-web-security')
    #     options.add_argument(
    #             '--disk-cache-dir=/var/www/cake2.2.4/app/tmp/cache/selenium-chrome-cache')
    #     options.add_argument('--no-referrers')
    #     options.add_argument(
    #             "'chrome.prefs': {'profile.managed_default_content_settings.images': 2}")
    #
    #     self.driver = webdriver.Firefox(
    #             executable_path='/Users/sergioneri/testjenkins/geckodriver',
    #             firefox_options=options)

    # def setup(self):
        # Create a new Firefox driver instance

        # binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        # # fp = (r'C:\Users\username\AppData\Roaming\Mozilla\Firefox\Profiles\oqmqnsih.default')
        # opts = Options()
        # # opts.profile = fp
        # firefox_capabilities = DesiredCapabilities.FIREFOX
        # firefox_capabilities['marionette'] = True
        # self.driver = webdriver.Firefox(capabilities=firefox_capabilities,
        #                            firefox_binary=binary, firefox_options=opts)


        # firefox_capabilities = DesiredCapabilities.FIREFOX
        # firefox_capabilities['marionette'] = True
        # # you probably don't need the next 3 lines they don't seem to work anyway
        # firefox_capabilities['handleAlerts'] = True
        # firefox_capabilities['acceptSslCerts'] = True
        # firefox_capabilities['acceptInsecureCerts'] = True
        # ffProfilePath = '/usr/local/bin/k53yczi1.default'
        #
        # profile = webdriver.FirefoxProfile(profile_directory=ffProfilePath)
        # geckoPath = '/Users/sergioneri/testjenkins/geckodriver'
        # self.driver = webdriver.Firefox(firefox_profile=profile,
        #                             capabilities=firefox_capabilities,
        #                             executable_path=geckoPath)

        self.driver.implicitly_wait(10)  # 10 seconds

    def teardown(self):
        # Close the browser after running the tests
        self.driver.quit()

    def test_search(self):
        # Trigger a Google Search
        self.driver.get('http://www.google.com')
        searchElement = self.driver.find_element_by_name('q')
        searchElement.send_keys('6020 peaks')
        searchElement.submit()
        # WebDriverWait(self.driver, 10).until(EC.title_contains('6020 peaks'))
