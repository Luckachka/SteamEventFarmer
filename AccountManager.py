from SteamLogin import SteamLogin
from DiscoveryQueue import DiscoveryQueue


class AccountManager:
    def __init__(self, browser, account_file):
        self.browser = browser
        self.logger = SteamLogin(browser)
        self.queue = DiscoveryQueue(browser)
        self.accounts = []

        self.get_accounts_from_file(account_file)

    def get_accounts_from_file(self, file):
        out = []
        with open(file, "r") as f:
            data = f.read().split("\n")
        for acc in data:
            out.append((acc.split()[0], acc.split()[1]))
        self.accounts = out

    def start(self):
        for acc in self.accounts:
            if self.logger.login(acc[0], acc[1]):
                print(f"Login success {acc[0]}")
                for x in range(5):
                    self.queue.start()
                self.logger.logout()
            else:
                print(f"Login error {acc[0]}")
            print("----------------------------")
