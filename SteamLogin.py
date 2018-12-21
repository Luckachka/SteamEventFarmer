from time import sleep


class SteamLogin:
    def __init__(self, browser):
        self.browser = browser

    def login(self, user, password):
        self.browser.get('https://steamcommunity.com/login/home/')

        username = self.browser.find_element_by_name("username")
        pw = self.browser.find_element_by_name("password")
        send = self.browser.find_element_by_id("SteamLogin")

        username.send_keys(user)
        pw.send_keys(password)
        if self.check_captcha():
            print(f"Please solve the captcha (Please do not sign in)")
            user_in = "n"
            while user_in.lower() != "y":
                user_in = input("Are you done solving? (y/n): ")
        send.click()

        sleep(2.0)
        if self.check_two_factor():
            steam_guard = input("Please enter your 2FA code: ")
            steam_guard_input = self.browser.find_element_by_id("twofactorcode_entry")
            steam_guard_input.send_keys(steam_guard.upper())
            sg_button = self.browser.find_elements_by_xpath("//div[@id='login_twofactorauth_buttonset_entercode']/div[@type='submit']")
            sg_button[0].click()

        sleep(2.0)
        return True

    def check_captcha(self):
        return len(self.browser.find_element_by_id("captchaExplanation").text) > 0

    def check_two_factor(self):
        try:
            steam_guard = self.browser.find_element_by_id("login_twofactorauth_icon")
            return len(str(steam_guard)) > 0
        except:
            return False

    def logout(self):
        self.browser.find_element_by_id("account_pulldown").click()
        self.browser.find_elements_by_xpath("//div[@id='account_dropdown']/div/a[@href='javascript:Logout();']")[0].click()
