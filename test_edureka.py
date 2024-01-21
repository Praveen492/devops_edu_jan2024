from selenium import webdriver


class BaseValidation:

    def open_browser(self, url):
        self.url = "https://facebook.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

    def close_browser(self, driver):
        driver.close()


result = BaseValidation()
# print(result)
