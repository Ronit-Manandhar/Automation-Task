class Saucedemo:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    button_cart_id = "shopping_cart_container"
    button_continueshopping_id= "continue-shopping"
    textbox_firstname_id = "first-name"
    textbox_lastname_id = "last-name"
    textbox_postalcode_id = "postal-code"
    button_checkout_id = "checkout"
    button_continue_id = "continue"
    button_finish_id = "finish"
    button_hamburger = "react-burger-menu-btn"
    button_logout = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def logincredentials(self, username, password):
        self.driver.find_element_by_id(self.textbox_username_id).click()
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(self.textbox_password_id).click()
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def clickoncart(self):
        self.driver.find_element_by_id(self.button_cart_id).click()

    def continueshopping(self):
        self.driver.find_element_by_id(self.button_continueshopping_id).click()


    def set_inputforcheckout(self, firstname, lastname, postalcode):
        self.driver.find_element_by_id(self.textbox_firstname_id).click()
        self.driver.find_element_by_id(self.textbox_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(firstname)
        self.driver.find_element_by_id(self.textbox_lastname_id).click()
        self.driver.find_element_by_id(self.textbox_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lastname)
        self.driver.find_element_by_id(self.textbox_postalcode_id).click()
        self.driver.find_element_by_id(self.textbox_postalcode_id).clear()
        self.driver.find_element_by_id(self.textbox_postalcode_id).send_keys(postalcode)

    def clickcheckout(self):
        self.driver.find_element_by_id(self.button_checkout_id).click()

    def clickcontinue(self):
        self.driver.find_element_by_id(self.button_continue_id).click()

    def finishcheckout(self):
        self.driver.find_element_by_id(self.button_finish_id).click()

    def clicklogout(self):
        self.driver.find_element_by_id(self.button_hamburger).click()
        self.driver.find_element_by_id(self.button_logout).click()