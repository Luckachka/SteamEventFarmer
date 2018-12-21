from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from AccountManager import AccountManager

if __name__ == "__main__":
    opts = Options()
    # opts.headless = True
    browser = Chrome(options=opts, keep_alive=True)

    account_manager = AccountManager(browser, "accounts.txt")
    account_manager.start()
