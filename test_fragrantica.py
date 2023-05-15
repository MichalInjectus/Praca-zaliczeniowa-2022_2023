import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException



class SearchEngineTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait_10_seconds = WebDriverWait(self.driver, 10)
        self.driver.get('https://www.fragrantica.pl/')
        self.action = ActionChains(self.driver)
        perfumy_menu = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul/li[5]')
        szukaj = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/ul/li[5]/ul/li[1]/a/span')
        self.action.move_to_element(perfumy_menu)
        self.action.perform()
        szukaj.click()
        self.wait_10_seconds = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]')))
        cookie_accept_btn = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/button[2]')
        cookie_accept_btn.click()


    def testOpenigSearchEngine(self):
        title = self.driver.title
        print(title)
        assert 'Wyszukiwarka perfum' == title

    def is_element_present(self, how, what):
        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def testPerfumeSearhGender(self):
        self.driver.execute_script('scrollBy(0,500)')
        unisex_checkbox = self.driver.find_element(By.XPATH, '//*[@id="offCanvasLeftOverlap1"]/div/div/div[3]/div[2]/p/div/ul/li[1]/label/input')
        mezczyzna_checkbox = self.driver.find_element(By.XPATH, '//*[@id="offCanvasLeftOverlap1"]/div/div/div[3]/div[2]/p/div/ul/li[3]/label/input')
        self.wait_10_seconds = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="offCanvasLeftOverlap1"]/div/div/div[3]/div[2]/p/div/ul/li[1]/label/input')))
        unisex_checkbox.click()
        mezczyzna_checkbox.click()
        # SPRAWDZENIE OCZEKIWANEGO REZULTATU
        # lista filtrów
        self.assertTrue(self.is_element_present(By.XPATH, '//*[@id="main-content"]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/div/ul/li'))
        # filtr unisex
        self.assertTrue(self.is_element_present(By.XPATH, '//*[@id="main-content"]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/div/ul/li/ul/li[1]/a'))
        # filtr mężczyzna
        self.assertTrue(self.is_element_present(By.XPATH, '//*[@id="main-content"]/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[1]/div/div/ul/li/ul/li[2]/a'))


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()