import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Page_Object_Model.pageobject import Saucedemo

class Sauce(unittest.TestCase):
    baseURL = "https://www.saucedemo.com"
    username = "standard_user"
    password = "secret_sauce"
    firstname = 'Lorem'
    lastname = 'Ipsum'
    postalcode = 12345

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def test_1_login(self):
        self.sd = Saucedemo(self.driver)
        self.sd.logincredentials(self.username,self.password)
        self.sd.clickLogin()

    def test_2_add_item_to_cart(self):
        self.driver.find_element_by_id('add-to-cart-sauce-labs-backpack').click()
        self.sd = Saucedemo(self.driver)
        self.sd.clickoncart()
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'cart_quantity'))
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'cart_item_label'))
        self.driver.find_element_by_id('remove-sauce-labs-backpack').click()
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'removed_cart_item'))
        self.sd.continueshopping()

    def test_3_add_another_item(self):
        self.driver.find_element_by_id('add-to-cart-test.allthethings()-t-shirt-(red)').click()
        self.sd = Saucedemo(self.driver)
        self.sd.clickoncart()
        self.sd.clickcheckout()
        self.sd.clickcontinue()
        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'error-button'))

    def test_4_checkout(self):
        self.sd = Saucedemo(self.driver)
        self.sd.set_inputforcheckout(self.firstname,self.lastname,self.postalcode)
        self.sd.clickcontinue()
        self.sd.finishcheckout()
        checkout_complete = self.driver.find_element_by_id('checkout_complete_container').is_displayed()
        print('Checkout is completed? : ' + str(checkout_complete))

    def test_5_logout(self):
        self.sd = Saucedemo(self.driver)
        self.sd.clicklogout()
        login_page = self.driver.find_element_by_class_name('login_wrapper').is_displayed()
        print('Back to login page? : ' + str(login_page))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException: return False
        return True

if __name__=='__main__':
    unittest.main()